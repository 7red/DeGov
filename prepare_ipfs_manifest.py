#!/usr/bin/env python3
import os
import json

HASH_DIR = "DeSwitzerland/DeVAT/data/hashes"
OUT_FILE = "docs/ipfs_manifest.json"

manifest = []

for fname in sorted(os.listdir(HASH_DIR)):
    if not fname.endswith(".sha256"):
        continue
    path = os.path.join(HASH_DIR, fname)
    with open(path) as f:
        line = f.read().strip()
        hash_val, file_json = line.split("  ")
        manifest.append({
            "filename": file_json,
            "sha256": hash_val,
            "ipfs_ready": True
        })

with open(OUT_FILE, "w") as out:
    json.dump(manifest, out, indent=2)

print(f"📦 Manifeste IPFS généré : {OUT_FILE}")
