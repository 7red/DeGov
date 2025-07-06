#!/usr/bin/env python3
import subprocess

options = {
    "1": ("Import TVA EFV", "python devat_import_all.py"),
    "2": ("Générer SHA256", "python sign_sha256.py"),
    "3": ("Index SHA256 public", "python publish_sha256_in_dapp.py"),
    "4": ("ZIP mensuel", "python zip_monthly_archives.py"),
    "5": ("Manifeste IPFS", "python prepare_ipfs_manifest.py"),
    "6": ("Git push automatique", "python auto_git_push.py"),
    "7": ("🚀 Tout exécuter", "python devat_publish_all.py"),
    "0": ("Quitter", None)
}

def main():
    while True:
        print("\n=== MENU DeVAT ===")
        for key, (desc, _) in options.items():
            print(f"{key}. {desc}")
        choice = input("Choix > ").strip()
        if choice not in options:
            print("❌ Choix invalide.")
            continue
        if choice == "0":
            print("👋 Bye.")
            break
        _, cmd = options[choice]
        print(f"➡️ {cmd}")
        subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    main()
