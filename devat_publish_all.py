#!/usr/bin/env python3
import subprocess

def run(title, cmd):
    print(f"\n🚀 {title}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout.strip())
    if result.stderr:
        print(result.stderr.strip())

# Étapes automatisées
run("1. Import TVA EFV", "python devat_import_all.py")
run("2. Génération SHA256", "python sign_sha256.py")
run("3. Index SHA256 public", "python publish_sha256_in_dapp.py")
run("4. ZIP mensuel", "python zip_monthly_archives.py")
run("5. Manifeste IPFS", "python prepare_ipfs_manifest.py")
run("6. Git auto-push", "python auto_git_push.py")
