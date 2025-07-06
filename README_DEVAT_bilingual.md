# 📘 Manuel d'utilisation – DeVAT / User Manual

---

## 🇫🇷 Initialisation / 🇬🇧 Initialization

```bash
python3 -m venv ~/DeGov/.venv && source ~/DeGov/.venv/bin/activate && pip install requests pandas openpyxl beautifulsoup4
```

---

## ▶️ 🇫🇷 Import automatique / 🇬🇧 Automatic import

```bash
python ~/DeGov/devat_import_all.py
```

---

## 🔐 🇫🇷 Signature SHA256 / 🇬🇧 SHA256 signature

```bash
python ~/DeGov/sign_sha256.py
```

➡️ Résultats dans / Results in: `DeSwitzerland/DeVAT/data/hashes/`

---

## 🚀 🇫🇷 Publication automatique Git / 🇬🇧 Git auto push

```bash
python ~/DeGov/auto_git_push.py
```

---

## ⏱️ 🇫🇷 Cron job quotidien / 🇬🇧 Daily cron job

```bash
(crontab -l 2>/dev/null; echo "0 7 * * * cd ~/DeGov && ~/DeGov/.venv/bin/python devat_import_all.py && python ~/DeGov/auto_git_push.py") | crontab -
```

Vérifier / Verify:

```bash
crontab -l
```

---

## 🌍 🇫🇷 Interface publique / 🇬🇧 Public interface

[https://7red.github.io/DeGov/](https://7red.github.io/DeGov/)

---

## 📂 🇫🇷 Structure du projet / 🇬🇧 Project structure

```
DeGov/
├── DeSwitzerland/
│   └── DeVAT/
│       ├── data/
│       │   ├── raw/         # 🇫🇷 fichiers bruts / 🇬🇧 raw Excel
│       │   ├── processed/   # 🇫🇷 JSON extraits / 🇬🇧 extracted JSON
│       │   └── hashes/      # 🇫🇷 signatures SHA256
│       └── scripts/
├── docs/
│   ├── index.html
│   └── processed/
│   └── archives/
├── devat_import_all.py
├── sign_sha256.py
└── auto_git_push.py
```

---

## 🧪 🇫🇷 Test manuel complet / 🇬🇧 Full manual test

```bash
cd ~/DeGov && ~/DeGov/.venv/bin/python devat_import_all.py && python sign_sha256.py && python auto_git_push.py
```

---

## 🧼 🇫🇷 Nettoyage / 🇬🇧 Cleanup

```bash
find . -name '__pycache__' -exec rm -rf {} +
```

---

## 🛟 🇫🇷 En cas de problème / 🇬🇧 Troubleshooting

- Vérifier si le fichier est visible dans `/docs/processed/`
- Forcer le rafraîchissement GitHub Pages : `Cmd + Shift + R`
- Réexécuter manuellement le script d'import

