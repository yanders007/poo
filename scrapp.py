import requests
from bs4 import BeautifulSoup

# 1. L'URL du site à scraper
url = "https://Google.com/"

print(f"[*] Connexion à {url}...")

try:
    # 2. Envoi de la requête HTTP GET
    response = requests.get(url)
    
    # On vérifie si la requête a réussi (Code 200)
    if response.status_code == 200:
        print("[+] Page récupérée avec succès ! Analyse en cours...\n")
        
        # 3. Parser le contenu HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 4. Trouver tous les blocs de citations
        # Sur ce site, chaque citation est dans un div avec la classe 'quote'
        quotes = soup.find_all('div', class_='quote')
        
        # 5. Boucler sur les résultats pour extraire le texte et l'auteur
        for i, quote in enumerate(quotes, 1):
            texte = quote.find('span', class_='text').text
            auteur = quote.find('small', class_='author').text
            
            print(f"{i}. {texte}")
            print(f"   — Par : {auteur}\n")
            
    else:
        print(f"[-] Erreur de chargement : Code {response.status_code}")

except Exception as e:
    print(f"[-] Une erreur est survenue : {e}")

