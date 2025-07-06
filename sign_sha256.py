#!/usr/bin/env python3
import hashlib
import os

TARGET_DIR = "DeSwitzerland/DeVAT/data/processed"
HASH_DIR = "DeSwitzerland/DeVAT/data/hashes"
os.makedirs(HASH_DIR, exist_ok=True)

def sha256sum(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

for filename in os.listdir(TARGET_DIR):
    if filename.endswith(".json"):
        path = os.path.join(TARGET_DIR, filename)
        hash_value = sha256sum(path)
        hash_file = os.path.join(HASH_DIR, filename.replace(".json", ".sha256"))
        with open(hash_file, "w") as f:
            f.write(f"{hash_value}  {filename}\n")
        print(f"✅ SHA256: {filename} -> {hash_file}")
