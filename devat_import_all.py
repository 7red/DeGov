#!/usr/bin/env python3
import os, re, json, requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

BASE_URL = "https://www.efv.admin.ch"
PAGE_URL = BASE_URL + "/efv/fr/home/finanzberichterstattung/bundeshaushalt_ueb/einnahmen.html"
RAW_DIR = "DeSwitzerland/DeVAT/data/raw"
OUT_DIR = "DeSwitzerland/DeVAT/data/processed"
WEB_DIR = "docs/processed"

os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(WEB_DIR, exist_ok=True)

def get_all_xlsx_links():
    print("📡 Chargement des liens Excel depuis le site EFV...")
    resp = requests.get(PAGE_URL, timeout=20)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    links = [BASE_URL + a["href"] for a in soup.find_all("a", href=True) if a["href"].endswith(".xlsx")]
    print(f"🔗 {len(links)} fichiers détectés.")
    return links

def download_file(url):
    fname = url.split("/")[-1]
    local = os.path.join(RAW_DIR, fname)
    if os.path.exists(local):
        return local
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        with open(local, "wb") as f:
            f.write(r.content)
        print(f"✅ Téléchargé : {fname}")
        return local
    except Exception as e:
        print(f"❌ Erreur téléchargement {fname} : {e}")
        return None

def extract_tva(filepath):
    try:
        df = pd.read_excel(filepath, engine="openpyxl")
        df = df.fillna("")
        for i, row in df.iterrows():
            row_str = str(row).lower()
            if "valeur ajoutée" in row_str or "taxe sur la valeur ajoutée" in row_str:
                vals = row.tolist()
                montant = next((float(v) for v in vals if isinstance(v, (int, float))), None)
                mois = re.findall(r"(\d{4}-\d{2})", filepath)
                mois = mois[0] if mois else datetime.today().strftime("%Y-%m")
                return {
                    "mois": mois,
                    "montant_tva": montant,
                    "extrait": row_str
                }
        print(f"⚠️ Aucune ligne TVA trouvée dans {filepath}")
    except Exception as e:
        print(f"💥 Erreur extraction {filepath} : {e}")
    return None

def save_json(data):
    if not data:
        return
    fname = f"TVA-{data['mois']}.json"
    with open(os.path.join(OUT_DIR, fname), "w") as f:
        json.dump(data, f, indent=2)
    with open(os.path.join(WEB_DIR, fname), "w") as f:
        json.dump(data, f, indent=2)
    print(f"📁 Export JSON : {fname}")

def main():
    links = get_all_xlsx_links()
    for url in links:
        fpath = download_file(url)
        if not fpath:
            continue
        data = extract_tva(fpath)
        save_json(data)

if __name__ == "__main__":
    main()
