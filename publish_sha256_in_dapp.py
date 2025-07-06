#!/usr/bin/env python3
import os
import json

HASH_DIR = "DeSwitzerland/DeVAT/data/hashes"
OUTPUT_FILE = "docs/sha256_index.json"

index = []

for fname in sorted(os.listdir(HASH_DIR)):
    if fname.endswith(".sha256"):
        with open(os.path.join(HASH_DIR, fname)) as f:
            content = f.read().strip()
            hash_val, file_json = content.split("  ")
            index.append({
                "fichier": file_json,
                "sha256": hash_val
            })

with open(OUTPUT_FILE, "w") as out:
    json.dump(index, out, indent=2)

print(f"✅ Index SHA256 public généré : {OUTPUT_FILE}")
