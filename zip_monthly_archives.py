#!/usr/bin/env python3
import os
import re
import zipfile
from collections import defaultdict

SRC_DIR = "DeSwitzerland/DeVAT/data/processed"
OUT_DIR = "docs/archives"
os.makedirs(OUT_DIR, exist_ok=True)

grouped = defaultdict(list)

# Grouper les fichiers JSON par mois
for fname in os.listdir(SRC_DIR):
    if not fname.endswith(".json"):
        continue
    match = re.match(r"TVA-(\d{4}-\d{2})\.json", fname)
    if match:
        month = match.group(1)
        grouped[month].append(os.path.join(SRC_DIR, fname))

# Créer un zip par mois
for month, files in grouped.items():
    zipname = os.path.join(OUT_DIR, f"TVA-{month}.zip")
    with zipfile.ZipFile(zipname, "w", zipfile.ZIP_DEFLATED) as zipf:
        for f in files:
            arcname = os.path.basename(f)
            zipf.write(f, arcname)
    print(f"✅ Archive générée : {zipname}")
