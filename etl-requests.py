import os
import requests
from bs4 import BeautifulSoup
import re

# Le contenu HTML que vous avez fourni
html_content1 = """
... [votre contenu HTML ici] ...
"""
html_content = requests.get(html_content1)
# Créer un objet BeautifulSoup à partir du contenu HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Trouver tous les éléments <a> avec l'attribut onclick contenant "javascript:openReleve"
onclick_elements = soup.find_all('a', {'onclick': re.compile(r"javascript:openReleve\('.*?'\)")})

# Extraire les codes de chaque attribut onclick
codes = [re.search(r"'(.*?)'", element['onclick']).group(1) for element in onclick_elements]

# Lien de base pour télécharger les fichiers PDF
base_url = "Your-Url-?id={}&..."

# Dossier de destination pour les fichiers PDF téléchargés
download_folder = "pdf_downloads"
os.makedirs(download_folder, exist_ok=True)

# Parcourir les codes extraits et télécharger les fichiers PDF avec requests
for i, code in enumerate(codes, 1):
    pdf_url = base_url.format(code)
    pdf_path = os.path.join(download_folder, f"nom{i}.pdf")
    
    response = requests.get(pdf_url)
    
    if response.status_code == 200:
        with open(pdf_path, 'wb') as pdf_file:
            pdf_file.write(response.content)
        print(f"Fichier olivier{i}.pdf téléchargé.")
    else:
        print(f"Erreur lors du téléchargement du fichier olivier{i}.pdf")

print("Téléchargement terminé.")
