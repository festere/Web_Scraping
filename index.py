import requests
import json
from bs4 import BeautifulSoup
import urllib3
from http.client import responses
from unidecode import unidecode
from collections import Counter
import folium
from folium.plugins import HeatMap
import geopandas as gpd
from tkinter import *
from tkinter.messagebox import *
import customtkinter



##########################################################################################################################################################################
# DEF of parsing
##########################################################################################################################################################################
def ExecuteCode():
    # Parse the HTML content of the page
    response = requests.get(url_value.get())
    soup = BeautifulSoup(response.content, 'html.parser')

    # Parse only the content we want
    spans = soup.find_all(balise_value.get(), {'class': class_value.get()})


    # Export to a JSON file
    with open('./result/data.json', 'a', encoding="utf-8") as f:
        count = 0 # Count for the ID
        for span in spans:
            spans_text = [span.get_text()]
            idx = ["id:", count] # IDX
            element = [idx , spans_text] # IDX plus the parsed content
            json.dump(element, f)
            f.write('\n')
            count += 1

    # Import the JSON
    with open('./result/data.json') as file:
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
            print(f"nombre de mention de {city_name}: {count}") # Print the counts


    # Load the map of the cities from the JSON file
    with open('./bin/bordeaux.json', "r") as bordeaux:
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
        with open("./result/map.json", 'w+') as f:
            json.dump(cities_data, f, indent=2)



##########################################################################################################################################################################
# DEF to get the HTTP status code and show a warning if the HTTP status code is not 200
##########################################################################################################################################################################
def HTTPerror():
    http = urllib3.PoolManager()
    request = http.request('GET', url_value.get())
    http_status = request.status

    if http_status != 200:
        showwarning("Connection au site impossible")
        root.destroy()



##########################################################################################################################################################################
# DEF to check if every input as been filled
##########################################################################################################################################################################
def StartCode():
    if url_value.get() == "":
        showwarning("Attention", "Veuillez entrer une URL")
    elif balise_value.get() == "":
        showwarning("Attention", "Veuillez entrer une balise")
    elif class_value.get() == "":
        showwarning("Attention", "Veuillez entrer une classe")
    else:
        HTTPerror()
        ExecuteCode()



##########################################################################################################################################################################
# GUI
##########################################################################################################################################################################
root = customtkinter.CTk()
root.title("OnePoint - Scraping")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
root.geometry('600x300')
root.resizable(False, False)


label = customtkinter.CTkLabel(root, text="URL:")
label.pack()
url_value = customtkinter.CTkEntry(root, width= 500)
url_value.pack()

label = customtkinter.CTkLabel(root, text="Balise:")
label.pack()
balise_value = customtkinter.CTkEntry(root, width= 100)
balise_value.pack()

label = customtkinter.CTkLabel(root, text="Classe:")
label.pack()
class_value = customtkinter.CTkEntry(root, width= 200)
class_value.pack()

Button = customtkinter.CTkButton (root, text="Commencer le scaping", command=StartCode)
#padding top
Button.pack(padx=10, pady=30)



root.mainloop()
