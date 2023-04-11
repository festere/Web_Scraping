import requests
import json
from bs4 import BeautifulSoup
import urllib3
from http.client import responses
from unidecode import unidecode
from collections import Counter
import folium
import geopandas as gpd
from tkinter import *
from tkinter.messagebox import *
import customtkinter
import os
import random
import urllib3
urllib3.disable_warnings()





websites = {
  "Petit Fute": {
    "URL": "https://www.petitfute.com/v1524-bordeaux-33000/c1122-voyage-transports/c1145-avion-bateau-bus-train-taxi-parking/c1154-transport-urbain/98794-tbm.html",
    "Balise": "div",
    "Class": "comment-truncate"
  },
  "Telephone city": {
    "URL": "https://www.telephone.city/transports-en-commun/tbm-bordeaux-1120766.html",
    "Balise": "div",
    "Class": "cmtx_comment_text"
  },
  "TripAdvisor": {
    "URL": "https://www.tripadvisor.fr/Attraction_Review-g187079-d10344773-Reviews-Le_reseau_de_transports_TBM_Tramway-Bordeaux_Gironde_Nouvelle_Aquitaine.html",
    "Balise": "span",
    "Class": "yCeTE"
  },
  "Pages Jaunes": {
    "URL": "https://www.pagesjaunes.fr/pros/59035126",
    "Balise": "div",
    "Class": "commentaire"
  }
}


user_agent_list = [
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]


user_agent = random.choice(user_agent_list)
headers = {'User-Agent': user_agent}
print(headers)

def check_checkbox():
    if checkbox.get() == 0: # If the checkbox is not checked
        ONE_StartCode(optionmenu.get())
    else: # If the checkbox is checked
        ALL_StartCode()

##########################################################################################################################################################################
##########################################################################################################################################################################
# All websites to scrap
##########################################################################################################################################################################
##########################################################################################################################################################################
def ALL_StartCode():
    for website in websites:
        URL = websites[website]["URL"]
        Balise = websites[website]["Balise"]
        Class_ = websites[website]["Class"]
        try:
            http = urllib3.PoolManager()
            request = http.request('GET', URL, timeout=10.0)
            http_status = request.status
            print(http_status)
        except:
            showwarning(title="Attention", message="Connection à "+ website + " impossible")
        if http_status == 404:
            showwarning(title="Attention", message="Connection à "+ website + " impossible")
        else:
            # Parse the HTML content of the page
            response = requests.get(URL, timeout=10.0)
            soup = BeautifulSoup(response.content, 'html.parser')
            # Parse only the content we want
            spans = soup.find_all(Balise, Class_)
            ExecuteCode(spans)
    showinfo(title="Attention", message="Scraping terminé")





##########################################################################################################################################################################
##########################################################################################################################################################################
# One website to scrap
##########################################################################################################################################################################
##########################################################################################################################################################################
def ONE_StartCode(selected_website):
    URL = websites[selected_website]["URL"]
    Balise = websites[selected_website]["Balise"]
    Class_ = websites[selected_website]["Class"]

    try:
        http = urllib3.PoolManager()
        request = http.request('GET', URL, timeout=10.0)
        http_status = request.status
        print(http_status)
    except:
        showwarning(title="Attention", message="Connection à "+ selected_website + " impossible")
    if http_status == 404:
        showwarning(title="Attention", message="Connection à "+ selected_website + " impossible")
    else:
        try:
            # Parse the HTML content of the page
            response = requests.get(URL, timeout=10.0, headers=headers, verify=False)
            soup = BeautifulSoup(response.content, 'html.parser')
            # Parse only the content we want
            spans = soup.find_all(Balise, Class_)
            ExecuteCode(spans)
        except:
            showwarning(title="Attention", message="Connection à "+ selected_website + " impossible")





##########################################################################################################################################################################
##########################################################################################################################################################################
# User enter the website settings to scrap
##########################################################################################################################################################################
##########################################################################################################################################################################

##########################################################################################################################################################################
# DEF to check if every input as been filled
##########################################################################################################################################################################
def PERSONALIZED_StartCodeURL():
    try:
        http = urllib3.PoolManager()
        request = http.request('GET', url_value_URL.get(), timeout=10.0)
        http_status = request.status
        print(http_status)
    except:
        showwarning(title="Attention", message="Connection au site impossible")
    if http_status == 404:
        showwarning(title="Attention", message="Connection au site impossible")
    else:
        # Parse the HTML content of the page
        response = requests.get(url_value_URL.get(), timeout=10.0)
        soup = BeautifulSoup(response.content, 'html.parser')
        ExecuteCode(soup)

def PERSONALIZED_StartCodeBalise():
    try:
        http = urllib3.PoolManager()
        request = http.request('GET', url_value_Balise.get(), timeout=10.0)
        http_status = request.status
        print(http_status)
    except:
        showwarning(title="Attention", message="Connection au site impossible")
    if http_status == 404:
        showwarning(title="Attention", message="Connection au site impossible")
    else:
        # Parse the HTML content of the page
        response = requests.get(url_value_Balise.get(), timeout=10.0)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Parse only the content we want
        spans = soup.find_all(balise_value_Balise.get(), timeout=10.0)
        ExecuteCode(spans)

def PERSONALIZED_StartCodeClasse():
    try:
        http = urllib3.PoolManager()
        request = http.request('GET', url_value_Classe.get(), timeout=10.0)
        http_status = request.status
        print(http_status)
    except:
        showwarning(title="Attention", message="Connection au site impossible")
    if http_status == 404:
        showwarning(title="Attention", message="Connection au site impossible")
    else:
        # Parse the HTML content of the page
        response = requests.get(url_value_Classe.get(), timeout=10.0)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Parse only the content we want
        spans = soup.find_all(balise_value_Classe.get(), {'class': class_value_Classe.get()}, timeout=10.0)
        ExecuteCode(spans)









##########################################################################################################################################################################
##########################################################################################################################################################################
# General DEF
##########################################################################################################################################################################
##########################################################################################################################################################################

##########################################################################################################################################################################
# DEF of parsing
##########################################################################################################################################################################
datalocation = os.getcwd()
datalocation = os.path.join(datalocation, "Web_Scraping\\result", "data.json")

def ExecuteCode(spans):
    # Export to a JSON file
    with open(datalocation, 'a', encoding='utf-8') as f:
        count = 0 # Count for the ID
        for span in spans:
            spans_text = [span.get_text()]
            idx = ["id:", count] # IDX
            element = [idx , spans_text] # IDX plus the parsed content
            json.dump(element, f, ensure_ascii=False)
            f.write('\n')
            count += 1
        f.close()

    # Import the JSON
    with open(datalocation) as file:
        content = file.read()
        words = content.split()
        

        # Loop through the list of transport
        bus = ("bus", "BUS")
        tram = ("tram", "tramway", "TRAM", "TRAMWAY")
        v3 = ("v3", "V3", "vcube", "v cube", "vcub", "VCUB", "velo", "velo")
        bus_count = 0
        tram_count = 0
        v3_count = 0

        # Loop through the list of good and bad words
        good = ("j'adore", "meilleure", "pas cher", "pratique", "geniaux")
        bad = ("pas pratique", "très cher", "en retard", "nul", "la pire", "le pire", "les pires", "excecrable ")
        good_count = 0
        bad_count = 0

        # Loop through the list of every city
        #33 000
        #33 100
        #33 300
        #33 800
        Bordeaux_Saint_Jean = ("Bordeaux-Saint-Jean", "Bordeaux Saint Jean", "Saint-Jean", "Saint Jean", "bordeaux-saint-jean", "bordeaux saint jean", "saint-jean", "saint jean", "la gare")
        Bordeaux_Saint_Jean_count = 0
        #33 110
        Bousqua = ("Bousqua", "bousqua")
        Bousqua_count = 0
        #33 127
        Martignas = ("Martignas", "martignas", "Martignas-sur-Jalle", "Martignas sur Jalle", "martignas-sur-jalle", "martignas sur jalle", "martignas sur", "martignas-sur", "martignas", "Martignas", "jalle", "Jalle")
        Martignas_count = 0
        #33 130
        Begles = ("Bègles", "Begles", "bègles", "begles")
        Begles_count = 0
        #33 140
        Villenave = ("Villenave-d'Ornon", "Villenave d'Ornon", "villenave-d'ornon", "villenave d'ornon", "villenave-d", "villenave d", "villenave", "Villenave", "ornon", "Ornon")
        Villenave_count = 0
        #33 150
        Cenon = ("Cenon", "cenon")
        Cenon_count = 0
        #33 160
        Saint_Medard = ("Saint-Médard-en-Jalles", "Saint Médard en Jalles", "saint-médard-en-jalles", "saint médard en jalles", "saint-médard", "saint médard", "saint-medard", "saint medard", "Saint-Aubin-de-Medoc", "Saint Aubin de Medoc", "saint-aubin-de-medoc", "saint aubin de medoc", "saint-aubin", "saint aubin", "saint-aubin-de", "saint aubin de", "saint-aubin de", "saint-aubin", "saint aubin")
        Saint_Medard_count = 0
        #33 170
        Gradignan = ("Gradignan", "gradignan")
        Gradignan_count = 0
        #33 185
        Haillan = ("Haillan", "haillan", "Le Haillan", "Le haillan", "le haillan", "le Haillan", "le haillan")
        Haillan_count = 0
        #33 200
        Cauderan = ("Cauderan", "cauderan", "Pains-Franc", "pain-franc", "pain franc")
        Cauderan_count = 0
        #33 270
        Floirac_Bouliac = ("Floirac", "floirac", "Bouliac", "bouliac")
        Floirac_Bouliac_count = 0
        #33 290
        Parempuyre_Blanquefort = ("Parempuyre", "parempuyre", "Blanquefort", "blanquefort")
        Parempuyre_Blanquefort_count = 0
        #33 310
        Lormont = ("Lormont", "lormont")
        Lormont_count = 0
        #33 320
        Eysines_taillan = ("Eysines", "eysines", "Taillan-Medoc", "Taillan Medoc", "taillan-medoc", "taillan medoc", "taillan", "Taillan", "medoc", "Medoc")
        Eysines_taillan_count = 0
        #33 370
        Antigues = ("Antigues", "antigues")
        Antigues_count = 0
        #33 400
        Talence = ("Talence", "talence")
        Talence_count = 0
        #33 440
        Lagrave = ("Lagrave", "lagrave", "Saint-Louis de Montferrand", "Saint Louis de Montferrand", "saint-louis de montferrand", "saint louis de montferrand", "saint-louis", "saint louis", "montferrand", "Montferrand", "Saint-Vincent de Paul", "Saint Vincent de Paul", "saint-vincent de paul", "saint vincent de paul", "saint-vincent", "saint vincent", "paul", "Paul")
        Lagrave_count = 0
        #33 520
        Bruges = ("Bruges", "Bruges")
        Bruges_count = 0
        #33 530
        Bassens = ("Bassens", "bassens")
        Bassens_count = 0
        #33 560
        Carbon_Blanc = ("Carbon-Blanc", "Carbon Blanc", "carbon-blanc", "carbon blanc")
        Carbon_Blanc_count = 0
        #33 600
        Pessac = ("Pessac-Centre", "Pessac Centre", "Pessac","pessac-centre", "pessac centre", "pessac")
        Pessac_count = 0
        #33 700
        Merignac = ("Merignac-Arlac", "Merignac Arlac", "Arlac", "Merignac", "merignac-arlac", "merignac arlac", "arlac", "merignac")
        Merignac_count = 0
        #33 810
        Ambès = ("Ambès", "Ambes", "ambès", "ambes")
        Ambès_count = 0

        # Check if each word is in the list, if so: add 1 to the count      
        for word in words:
            if word in bus:
                bus_count += 1
            elif word in tram:
                tram_count += 1
            elif word in v3:
                v3_count += 1

            elif word in good:
                good_count += 1
            elif word in bad:
                bad_count += 1

            elif word in Bordeaux_Saint_Jean: #33 000 / 33 100 / 33 300 / 33 800
                Bordeaux_Saint_Jean_count += 1
            elif word in Bousqua: #33 110
                Bousqua_count += 1
            elif word in Martignas: #33 127
                Martignas_count += 1
            elif word in Begles: #33 130
                Begles_count += 1
            elif word in Villenave: #33 140
                Villenave_count += 1
            elif word in Cenon: #33 150
                Cenon_count += 1
            elif word in Saint_Medard: #33 160
                Saint_Medard_count += 1
            elif word in Gradignan: #33 170
                Gradignan_count += 1
            elif word in Haillan: #33 185
                Haillan_count += 1
            elif word in Cauderan: #33 200
                Cauderan_count += 1
            elif word in Floirac_Bouliac: #33 270
                Floirac_Bouliac_count += 1
            elif word in Parempuyre_Blanquefort: #33 290
                Parempuyre_Blanquefort_count += 1
            elif word in Lormont: #33 310
                Lormont_count += 1
            elif word in Eysines_taillan: #33 320
                Eysines_taillan_count += 1
            elif word in Antigues: #33 370
                Antigues_count += 1
            elif word in Talence: #33 400
                Talence_count += 1
            elif word in Lagrave: #33 440
                Lagrave_count += 1
            elif word in Bruges: #33 520
                Bruges_count += 1
            elif word in Bassens: #33 530
                Bassens_count += 1
            elif word in Carbon_Blanc: #33 560
                Carbon_Blanc_count += 1
            elif word in Pessac: #33 600
                Pessac_count += 1
            elif word in Merignac: #33 700
                Merignac_count += 1
            elif word in Ambès: #33 810
                Ambès_count += 1


        # Create a dictionary with the counts
        city_counts = {
            "Bordeaux_Saint_Jean": Bordeaux_Saint_Jean_count,
            "Bousqua": Bousqua_count,
            "Martignas": Martignas_count,
            "Begles": Begles_count,
            "Villenave": Villenave_count,
            "Cenon": Cenon_count,
            "Saint_Medard": Saint_Medard_count,
            "Gradignan": Gradignan_count,
            "Haillan": Haillan_count,
            "Cauderan": Cauderan_count,
            "Floirac_Bouliac": Floirac_Bouliac_count,
            "Parempuyre_Blanquefort": Parempuyre_Blanquefort_count,
            "Lormont": Lormont_count,
            "Eysines_taillan": Eysines_taillan_count,
            "Antigues": Antigues_count,
            "Talence": Talence_count,
            "Lagrave": Lagrave_count,
            "Bruges": Bruges_count,
            "Bassens": Bassens_count,
            "Carbon_Blanc": Carbon_Blanc_count,
            "Pessac": Pessac_count,
            "Merignac": Merignac_count,
            "Ambès": Ambès_count
        }
        for city_name, count in city_counts.items():
            label.textbox1.insert("0.0", city_name + " : " + str(count) + "\n") # Display the results in the GUI


    # Load the map of the cities from the JSON file
    bordeauxlocation = os.getcwd()
    bordeauxlocation = os.path.join(bordeauxlocation, "Web_Scraping\\bin", "bordeaux.json")
    with open(bordeauxlocation, "r") as bordeaux:
        cities_data = json.load(bordeaux)

        # Cities with their index from the JSON file
        count_dict = {
            Bordeaux_Saint_Jean_count: 6,
            Bordeaux_Saint_Jean_count: 16,
            Bordeaux_Saint_Jean_count: 24,
            Bordeaux_Saint_Jean_count: 25,
            Bousqua_count: 14,
            Martignas_count: 10,
            Begles_count: 7,
            Villenave_count: 21,
            Cenon_count: 4,
            Saint_Medard_count: 1,
            Gradignan_count: 9,
            Haillan_count: 16,
            Cauderan_count: 3,
            Floirac_Bouliac_count: 5,
            Parempuyre_Blanquefort_count: 18,
            Lormont_count: 19,
            Eysines_taillan_count: 23,
            Antigues_count: 8,
            Talence_count: 11,
            Lagrave_count: 20,
            Bruges_count: 0,
            Bassens_count: 17,
            Carbon_Blanc_count: 22,
            Pessac_count: 2,
            Merignac_count: 15,
            Ambès_count: 12
        }

        #add fill color #ffffff to all the features
        for feature in cities_data['features']:
            feature['properties']['fill'] = "#ffffff"

        #change the fill color of the features with the count
        for city, feature_idxs in count_dict.items():
            feature = cities_data['features'][feature_idxs]
            if city == 1:
                feature['properties']['fill'] = "#FFDCDC"
            elif city == 2:
                feature['properties']['fill'] = "#FFB7B7"
            elif city == 3:
                feature['properties']['fill'] = "#FF8686"
            elif city == 4:
                feature['properties']['fill'] = "#FF6C6C"
            elif city == 5:
                feature['properties']['fill'] = "#FF5D5D"
            elif city == 6:
                feature['properties']['fill'] = "#FF3131"
            elif city >= 6:
                feature['properties']['fill'] = "#FF0000"

        # save the map into a geojson file
        maplocation = os.getcwd()
        maplocation = os.path.join(maplocation, "Web_Scraping\\result", "map.json")
        with open(maplocation, 'w+') as f:
            json.dump(cities_data, f, indent=2)


        with open(datalocation, "r", encoding="utf-8") as json_str:
            for line in json_str:
                label.textbox2.insert("0.0", line + "\n") # Display the results in the GUI










##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
# GUI
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
root = customtkinter.CTk()
root.title("OnePoint - Scraping")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
root.geometry('715x730')
root.resizable(False, False)





###################################################################################
###################################################################################
# Tabview for "ONE websites to scrap"
###################################################################################
###################################################################################
root.tabview = customtkinter.CTkFrame(root)
root.tabview.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
# Label for the title
label = customtkinter.CTkLabel(root.tabview, text="Prédéfinis:")
label.pack()

# Get the names of the website to scrap
website_names = list(websites.keys())
optionmenu = customtkinter.CTkOptionMenu(root.tabview, values=website_names)
optionmenu.pack()

# Checkbox to select if the user wants to scrap all the pages
checkbox = customtkinter.CTkCheckBox(root.tabview, text="Tous les sites")
checkbox.pack(pady=(60, 0))

#Button to take start ONE_StartCode with the website selected
button = customtkinter.CTkButton(root.tabview, text="Commencer le scaping", command=check_checkbox)
button.pack(pady=(60, 0))





###################################################################################
###################################################################################
# Tabview for "personalized website to scrap"
###################################################################################
###################################################################################
# Label and Entry for the type of content to scrap
root.tabview = customtkinter.CTkTabview(root, width=250)
root.tabview.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
root.tabview.add("URL")
root.tabview.add("Balise")
root.tabview.add("Classe")
# configure grid of individual tabs
root.tabview.tab("URL").grid_columnconfigure(0, weight=1)
root.tabview.tab("Balise").grid_columnconfigure(0, weight=1)
root.tabview.tab("Classe").grid_columnconfigure(0, weight=1)

###################################################################################
# Frame for the input "URL"
###################################################################################
# Label and Entry for the URL
label = customtkinter.CTkLabel(root.tabview.tab("URL"), text="URL:")
url_value_URL = customtkinter.CTkEntry(root.tabview.tab("URL"), width= 500)
label.grid()
url_value_URL.grid()
# Button to start the scraping
Button = customtkinter.CTkButton(root.tabview.tab("URL"), text="Commencer le scaping", command=PERSONALIZED_StartCodeURL)
Button.grid(padx=10, pady=30)

###################################################################################
# Frame for the input "Balise"
###################################################################################
# Label and Entry for the URL
label = customtkinter.CTkLabel(root.tabview.tab("Balise"), text="URL:")
url_value_Balise = customtkinter.CTkEntry(root.tabview.tab("Balise"), width= 500)
label.grid()
url_value_Balise.grid()
# Label and Entry for the balise
label = customtkinter.CTkLabel(root.tabview.tab("Balise"), text="Balise:")
balise_value_Balise = customtkinter.CTkEntry(root.tabview.tab("Balise"), width= 100)
label.grid()
balise_value_Balise.grid()
# Button to start the scraping
Button = customtkinter.CTkButton(root.tabview.tab("Balise"), text="Commencer le scaping", command=PERSONALIZED_StartCodeBalise)
Button.grid(padx=10, pady=30)

###################################################################################
# Frame for the input "Classe"
###################################################################################
# Label and Entry for the URL
label = customtkinter.CTkLabel(root.tabview.tab("Classe"), text="URL:")
url_value_Classe = customtkinter.CTkEntry(root.tabview.tab("Classe"), width= 500)
label.grid()
url_value_Classe.grid()
# Label and Entry for the balise
label = customtkinter.CTkLabel(root.tabview.tab("Classe"), text="Balise:")
balise_value_Classe = customtkinter.CTkEntry(root.tabview.tab("Classe"), width= 100)
label.grid()
balise_value_Classe.grid()
# Label and Entry for the class
label = customtkinter.CTkLabel(root.tabview.tab("Classe"), text="Classe:")
class_value_Classe = customtkinter.CTkEntry(root.tabview.tab("Classe"), width= 200)
label.grid()
class_value_Classe.grid()
# Button to start the scraping
Button = customtkinter.CTkButton(root.tabview.tab("Classe"), text="Commencer le scaping", command=PERSONALIZED_StartCodeClasse)
Button.grid(padx=10, pady=30)





###################################################################################
###################################################################################
# Tabview to show the result 
###################################################################################
###################################################################################
label.textbox1 = customtkinter.CTkTextbox(root)
label.textbox1.grid(row=1, column=0, columnspan=3, padx=(20, 0), pady=(20, 0), sticky="nsew")

label.textbox2 = customtkinter.CTkTextbox(root)
label.textbox2.grid(row=2, column=0, columnspan=3, padx=(20, 0), pady=(20, 0), sticky="nsew")


root.mainloop()
