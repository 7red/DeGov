#!/usr/bin/env python3
import subprocess
from datetime import datetime

def run(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout.strip():
        print(result.stdout.strip())
    if result.stderr.strip():
        print(result.stderr.strip())

now = datetime.now().strftime("%Y-%m-%d %H:%M")

print("🔁 Git auto push en cours...")
run("git add -A")
run(f"git commit -m '🔄 MAJ automatique : {now}'")
run("git push")
print("✅ Terminé.")
