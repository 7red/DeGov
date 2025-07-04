# devat_bot.py
# Script tout-en-un pour le projet DeVAT (TVA suisse)

import os
import re
import json
import time
import logging
from datetime import datetime
import requests
import pandas as pd
from bs4 import BeautifulSoup

# --- CONFIGURATION ---
BASE_URL = "https://www.efv.admin.ch"
PAGE_URL = BASE_URL + "/efv/fr/home/finanzberichterstattung/bundeshaushalt_ueb/einnahmen.html"
RAW_DIR = "data/raw"
OUT_DIR = "data/processed"
LOG_FILE = "logs/devat.log"

os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs("logs", exist_ok=True)

logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s')

def log(msg):
    print(msg)
    logging.info(msg)

# --- ÉTAPE 1 : SCRAPER TOUS LES LIENS XLSX ---
def get_xlsx_links():
    try:
        resp = requests.get(PAGE_URL, timeout=20)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        links = soup.find_all("a", href=True)
        return [BASE_URL + a['href'] for a in links if a['href'].endswith(".xlsx")]
    except Exception as e:
        log(f"Erreur lors du scraping : {e}")
        return []

# --- ÉTAPE 2 : TÉLÉCHARGER NOUVEAUX FICHIERS ---
def download_new_files(links):
    new_files = []
    for url in links:
        fname = url.split("/")[-1]
        yyyymm = re.findall(r"(\d{4}-\d{2})", fname)
        suffix = yyyymm[0] if yyyymm else datetime.today().strftime("%Y-%m")
        local_file = os.path.join(RAW_DIR, f"tva-{suffix}.xlsx")
        if os.path.exists(local_file):
            continue
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            with open(local_file, "wb") as f:
                f.write(r.content)
            log(f"Nouveau fichier téléchargé : {local_file}")
            new_files.append(local_file)
        except Exception as e:
            log(f"Échec téléchargement {url} : {e}")
    return new_files

# --- ÉTAPE 3 : EXTRAIRE DONNÉES TVA ---
def extract_tva(filepath):
    try:
        df = pd.read_excel(filepath, engine="openpyxl")
        df = df.fillna("")
        for i, row in df.iterrows():
            row_str = str(row).lower()
            if "valeur ajoutée" in row_str:
                vals = row.tolist()
                for v in vals:
                    if isinstance(v, (int, float)):
                        montant = float(v)
                        break
                else:
                    montant = None
                return {
                    "fichier": os.path.basename(filepath),
                    "mois": re.findall(r"(\d{4}-\d{2})", filepath)[0],
                    "montant_tva": montant,
                    "extrait": row_str
                }
        log(f"Aucune ligne TVA trouvée dans {filepath}")
        return None
    except Exception as e:
        log(f"Erreur extraction {filepath} : {e}")
        return None

# --- ÉTAPE 4 : EXPORT JSON ---
def export_json(data):
    if not data:
        return
    out_file = os.path.join(OUT_DIR, f"TVA-{data['mois']}.json")
    with open(out_file, "w") as f:
        json.dump(data, f, indent=2)
    log(f"✅ Données extraites publiées dans {out_file}")

# --- MAIN ---
def main():
    log("--- DÉMARRAGE DU SCRIPT DeVAT ---")
    links = get_xlsx_links()
    new_files = download_new_files(links)
    for f in new_files:
        data = extract_tva(f)
        export_json(data)
    log("--- FIN DU SCRIPT ---\n")

if __name__ == "__main__":
    main()
