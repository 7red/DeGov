# DeVAT – Décentralisation des recettes TVA suisses

Ce projet automatise la récupération, l'extraction et la publication mensuelle des données de TVA perçue par la Confédération suisse. Il fait partie de l'initiative DeGov > DeSwitzerland > DeVAT.

## Fonctionnalités

- Téléchargement automatique des fichiers mensuels de recettes TVA (.xlsx)
- Extraction de la ligne TVA et transformation en JSON
- Publication automatique dans le dépôt Git
- Visualisation simple via un frontend HTML

## Utilisation

```bash
python3 devat_bot.py
```

## Cron mensuel conseillé

```cron
0 7 12,20 * * /usr/bin/python3 /chemin/vers/devat/devat_bot.py >> /chemin/vers/devat/logs/devat.log 2>&1
```
