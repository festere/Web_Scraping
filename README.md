## 1. Description
Cet outil permet de récupérer des données sur des sites web (même ceux comportant une sécurité(cloudflare, datadome..)) et de les exporter sous 3 options:
- Un seul site web prédéfini.
- Tous les sites web prédéfinis.
- Un site web personnalisé sous 3 formats:
  1. URL: Tout le site web.
  2. div: Uniquement les divs de l'URL donnée.
  3. classes: Uniquement les classes des div dans l'URL donnée.

<br>
   
Exportation des données suivantes:
- Un fichier JSON pour les commentaires. (aussi affiché dans le GUI)
- Un fichier geoJSON pour une [heat map](https://geojson.io/#map=5.28/46.563/2.071) des villes citées.

<br>
<br>
<br>

## 2. Installation
### 2.1 Windows
1. Installer la derniere version de [Python 3](https://www.python.org/downloads/).
2. Installer l'outil de [Web_Scraping](https://github.com/festere/Web_Scraping/archive/refs/heads/main.zip).
3. Dezipper le dossier.
5. Verifier que le dernier fichier s'appelle bien `Web_Scraping` et non `Web_Scraping-main`.
6. Ouvrir le dossier `Web_Scraping`.
7. Faire un clic droit dans le dossier et cliquer sur "Ouvrir dans le terminal".
8. Taper la commande `pip install -r requirements.txt` et appuyer sur entrer.
9. Exécution du programme avec la commande `python3 index.py`.
10. Utiliser [geo JSON](https://geojson.io/#map=5.28/46.563/2.071) pour visualiser la heat map.

<br>

### 2.2 Linux
1. Installer la derniere version de [Python 3](https://docs.python-guide.org/starting/install3/linux)
2. Installer la derniere version de pip avec `apt install python3-pip`
3. Installer git avec la commande `sudo apt install git`.
4. Installer l'outil avec la commande `git clone https://github.com/festere/Web_Scraping.git`.
5. Ouverture du dossier avec la commande `cd Web_Scraping`.
6. Taper la commande `sudo apt-get install python3-tk` et appuyer sur entrer.
7. Taper la commande `pip install -r requirements.txt` et appuyer sur entrer.
8. Exécution du programme avec la commande `python3 index.py`.
9. Utiliser [geo JSON](https://geojson.io/#map=5.28/46.563/2.071) pour visualiser la heat map.
