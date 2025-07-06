# 📘 Manuel d'utilisation – Projet DeVAT

## 🔧 Initialisation de l'environnement

Créer un environnement virtuel dans le dossier du projet :

```bash
python3 -m venv ~/DeGov/.venv && source ~/DeGov/.venv/bin/activate && pip install requests pandas openpyxl beautifulsoup4
```

---

## ▶️ Exécuter l'import automatique des fichiers TVA

```bash
python ~/DeGov/devat_import_all.py
```

---

## ✅ Signature SHA256 de tous les JSON générés

```bash
python ~/DeGov/sign_sha256.py
```

Les fichiers `.sha256` sont générés dans :

```
DeSwitzerland/DeVAT/data/hashes/
```

---

## 🚀 Publication des fichiers sur GitHub (auto-push)

```bash
python ~/DeGov/auto_git_push.py
```

---

## 🕒 Cron job quotidien (vérifie et publie chaque jour à 7h)

Ajouter le cron :

```bash
(crontab -l 2>/dev/null; echo "0 7 * * * cd ~/DeGov && ~/DeGov/.venv/bin/python devat_import_all.py && python ~/DeGov/auto_git_push.py") | crontab -
```

Vérifier la crontab :

```bash
crontab -l
```

---

## 📦 Structure du projet

```
DeGov/
├── DeSwitzerland/
│   └── DeVAT/
│       ├── data/
│       │   ├── raw/            # Fichiers .xlsx originaux
│       │   ├── processed/      # Fichiers JSON extraits
│       │   └── hashes/         # Fichiers SHA256
│       └── scripts/
├── docs/
│   ├── index.html              # Interface publique GitHub Pages
│   └── processed/              # JSON visibles sur https://7red.github.io/DeGov/
├── devat_import_all.py         # Import massif depuis EFV
├── sign_sha256.py              # Signature SHA256
└── auto_git_push.py            # Publication automatique sur GitHub
```

---

## 🔗 Interface publique GitHub Pages

[https://7red.github.io/DeGov/](https://7red.github.io/DeGov/)

Le tableau charge automatiquement tous les mois détectés dans `/docs/processed/`.

---

## 🧼 Nettoyage (optionnel)

Supprimer tous les fichiers inutiles :

```bash
find . -name '__pycache__' -exec rm -rf {} +
```

---

## ✉️ En cas d'erreur

- Vérifie si le fichier existe (`ls`)
- Recharge GitHub Pages avec `Cmd + Shift + R`
- Relance le script manuellement
