#!/bin/bash

# Crée le fichier Mermaid
cat > flux_financiers.mmd <<'MMD'
flowchart TD
  A[Administration fédérale] -->|18.4 mrd CHF| C[Assurances sociales]
  A -->|3.4 mrd CHF| B[Entreprises de la Confédération]
  B -->|Dividendes / Participations| A
  C -->|Cotisations + Contributions| P[Prestations sociales 66.2 mrd CHF]
  A -->|Impôts / TVA / Recettes fiscales| D[Dépenses publiques générales]
MMD

# Crée le SVG
npx -y @mermaid-js/mermaid-cli -i flux_financiers.mmd -o flux_financiers.svg

# Convertit en PNG
python3 -c 'import cairosvg; cairosvg.svg2png(url="flux_financiers.svg", write_to="flux_financiers.png")'

# Prépare GitHub Pages
mkdir -p docs
cp flux_financiers.svg docs/
cat > docs/index.html <<'HTML'
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Diagramme des flux financiers</title>
  <style>
    body { font-family: sans-serif; padding: 2rem; }
    img { max-width: 100%; height: auto; border: 1px solid #ccc; }
  </style>
</head>
<body>
  <h1>💧 Flux financiers entre secteurs</h1>
  <p>Basé sur le rapport consolidé de la Confédération 2023.</p>
  <img src="flux_financiers.svg" alt="Diagramme flux financiers">
</body>
</html>
HTML

echo -e "✅ Tous les fichiers générés :\n- flux_financiers.mmd\n- flux_financiers.svg\n- flux_financiers.png\n- docs/index.html"
