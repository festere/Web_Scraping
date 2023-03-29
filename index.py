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



#Target URL
url = "https://www.petitfute.com/v1524-bordeaux-33000/c1122-voyage-transports/c1145-avion-bateau-bus-train-taxi-parking/c1154-transport-urbain/98794-tbm.html"



#Get the HTTP code and status
http = urllib3.PoolManager()
request = http.request('GET', url)
http_status = request.status
http_status_description = responses[http_status]
print("code status:" , http_status , http_status_description)
#Parse the HTML content of the page
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')



#Parse only the content we want
spans = soup.find_all('div', {'class': 'comment-truncate'})



#Export to a JSON file
with open('data.json', 'a', encoding="utf-8") as f:
    count = 0 #Count for the ID
    for span in spans:
        spans_text = [span.get_text()]
        idx = ["id:", count] #IDX
        element = [idx , spans_text] #IDX plus the parsed content
        json.dump(element, f)
        f.write('\n')
        count += 1

# Import the JSON
with open('data.json') as file:
    content = file.read()
    words = content.split()

    # Loop through the list of transport
    bus = ("bus", "BUS")
    tram = ("tram", "tramway", "TRAM", "TRAMWAY")
    v3 = ("v3", "V3", "vcube", "v cube", "vcub", "VCUB", "velo", "velo")
    bus_count = 0
    tram_count = 0
    v3_count = 0


    good = ("j'adore", "meilleure", "pas cher", "pratique", "geniaux")
    bad = ("pas pratique", "très cher", "en retard", "nul", "la pire", "le pire", "les pires", "excecrable ")
    good_count = 0
    bad_count = 0





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

    print("nombre de mention de bus:" , bus_count)
    print("nombre de mention de tram:" , tram_count)
    print("nombre de mention de v3:" , v3_count)


    print("nombre de bonne apreciation:" , good_count)
    print("nombre de mauvaise apreciation:" , bad_count)


    print("nombre de mention de Bordeaux Saint Jean:" , Bordeaux_Saint_Jean_count)
    print("nombre de mention de Bousqua:" , Bousqua_count)
    print("nombre de mention de Martignas:" , Martignas_count)
    print("nombre de mention de Begles:" , Begles_count)
    print("nombre de mention de Villenave:" , Villenave_count)
    print("nombre de mention de Cenon:" , Cenon_count)
    print("nombre de mention de Saint Medard:" , Saint_Medard_count)
    print("nombre de mention de Gradignan:" , Gradignan_count)
    print("nombre de mention de Haillan:" , Haillan_count)
    print("nombre de mention de Cauderan:" , Cauderan_count)
    print("nombre de mention de Floirac Bouliac:" , Floirac_Bouliac_count)
    print("nombre de mention de Parempuyre Blanquefort:" , Parempuyre_Blanquefort_count)
    print("nombre de mention de Lormont:" , Lormont_count)
    print("nombre de mention de Eysines taillan:" , Eysines_taillan_count)
    print("nombre de mention de Antigues:" , Antigues_count)
    print("nombre de mention de Talence:" , Talence_count)
    print("nombre de mention de Lagrave:" , Lagrave_count)
    print("nombre de mention de Bruges:" , Bruges_count)
    print("nombre de mention de Bassens:" , Bassens_count)
    print("nombre de mention de Carbon Blanc:" , Carbon_Blanc_count)
    print("nombre de mention de Pessac:" , Pessac_count)
    print("nombre de mention de Merignac:" , Merignac_count)
    print("nombre de mention de Ambès:" , Ambès_count)





# Load the map of the cities from the JSON file
with open('bordeaux.json', "r") as bordeaux:
    cities_data = json.load(bordeaux)

    feature = cities_data['features'][0]
    if Bordeaux_Saint_Jean_count == 0:
        feature['properties']['fill'] = "#FF6C6C"
    elif Bordeaux_Saint_Jean_count == 1:
        feature['properties']['fill'] = "#FFDCDC"
    elif Bordeaux_Saint_Jean_count == 2:
        feature['properties']['fill'] = "#FFB7B7"
    elif Bordeaux_Saint_Jean_count == 3:
        feature['properties']['fill'] = "#FF8686"
    elif Bordeaux_Saint_Jean_count == 4:
        feature['properties']['fill'] = "#FF6C6C"
    elif Bordeaux_Saint_Jean_count == 5:
        feature['properties']['fill'] = "#FF5D5D"
    elif Bordeaux_Saint_Jean_count == 6:
        feature['properties']['fill'] = "#FF3131"
    else:
        feature['properties']['fill'] = "#FF0000"

        for feature['properties']['code'] in "33110":
            if Bousqua_count == 0:
                feature['properties']['fill'] = "#FFFFFF"
            elif Bousqua_count == 1:
                feature['properties']['fill'] = "#FFDCDC"
            elif Bousqua_count == 2:
                feature['properties']['fill'] = "#FFB7B7"
            elif Bousqua_count == 3:
                feature['properties']['fill'] = "#FF8686"
            elif Bousqua_count == 4:
                feature['properties']['fill'] = "#FF6C6C"
            elif Bousqua_count == 5:
                feature['properties']['fill'] = "#FF5D5D"
            elif Bousqua_count == 6:
                feature['properties']['fill'] = "#FF3131"
            else:
                feature['properties']['fill'] = "#FF0000"

        for feature['properties']['code'] in "33127":
            if Martignas_count == 0:
                feature['properties']['fill'] = "#FFFFFF"
            elif Martignas_count == 1:
                feature['properties']['fill'] = "#FFDCDC"
            elif Martignas_count == 2:
                feature['properties']['fill'] = "#FFB7B7"
            elif Martignas_count == 3:
                feature['properties']['fill'] = "#FF8686"
            elif Martignas_count == 4:
                feature['properties']['fill'] = "#FF6C6C"
            elif Martignas_count == 5:
                feature['properties']['fill'] = "#FF5D5D"
            elif Martignas_count == 6:
                feature['properties']['fill'] = "#FF3131"
            else:
                feature['properties']['fill'] = "#FF0000"
            
        for feature['properties']['code'] in "33130":
            if Begles_count == 0:
                feature['properties']['fill'] = "#FFFFFF"
            elif Begles_count == 1:
                feature['properties']['fill'] = "#FFDCDC"
            elif Begles_count == 2:
                feature['properties']['fill'] = "#FFB7B7"
            elif Begles_count == 3:
                feature['properties']['fill'] = "#FF8686"
            elif Begles_count == 4:
                feature['properties']['fill'] = "#FF6C6C"
            elif Begles_count == 5:
                feature['properties']['fill'] = "#FF5D5D"
            elif Begles_count == 6:
                feature['properties']['fill'] = "#FF3131"
            else:
                feature['properties']['fill'] = "#FF0000"

        for feature['properties']['code'] in "33140":
            if Villenave_count == 0:
                feature['properties']['fill'] = "#FFFFFF"
            elif Villenave_count == 1:
                feature['properties']['fill'] = "#FFDCDC"
            elif Villenave_count == 2:
                feature['properties']['fill'] = "#FFB7B7"
            elif Villenave_count == 3:
                feature['properties']['fill'] = "#FF8686"
            elif Villenave_count == 4:
                feature['properties']['fill'] = "#FF6C6C"
            elif Villenave_count == 5:
                feature['properties']['fill'] = "#FF5D5D"
            elif Villenave_count == 6:
                feature['properties']['fill'] = "#FF3131"
            else:
                feature['properties']['fill'] = "#FF0000"

        for feature['properties']['code'] in "33150":
            if Cenon_count == 0:
                feature['properties']['fill'] = "#FFFFFF"
            elif Cenon_count == 1:
                feature['properties']['fill'] = "#FFDCDC"
            elif Cenon_count == 2:
                feature['properties']['fill'] = "#FFB7B7"
            elif Cenon_count == 3:
                feature['properties']['fill'] = "#FF8686"
            elif Cenon_count == 4:
                feature['properties']['fill'] = "#FF6C6C"
            elif Cenon_count == 5:
                feature['properties']['fill'] = "#FF5D5D"
            elif Cenon_count == 6:
                feature['properties']['fill'] = "#FF3131"
            else:
                feature['properties']['fill'] = "#FF0000"

        for feature['properties']['code'] in "33160":
            if Saint_Medard_count == 0:
                feature['properties']['fill'] = "#FFFFFF"
            elif Saint_Medard_count == 1:
                feature['properties']['fill'] = "#FFDCDC"
            elif Saint_Medard_count == 2:
                feature['properties']['fill'] = "#FFB7B7"
            elif Saint_Medard_count == 3:
                feature['properties']['fill'] = "#FF8686"
            elif Saint_Medard_count == 4:
                feature['properties']['fill'] = "#FF6C6C"
            elif Saint_Medard_count == 5:
                feature['properties']['fill'] = "#FF5D5D"
            elif Saint_Medard_count == 6:
                feature['properties']['fill'] = "#FF3131"
            else:
                feature['properties']['fill'] = "#FF0000"

        for feature['properties']['code'] in "33170":
            if Gradignan_count == 0:
                feature['properties']['fill'] = "#FFFFFF"
            elif Gradignan_count == 1:
                feature['properties']['fill'] = "#FFDCDC"
            elif Gradignan_count == 2:
                feature['properties']['fill'] = "#FFB7B7"
            elif Gradignan_count == 3:
                feature['properties']['fill'] = "#FF8686"
            elif Gradignan_count == 4:
                feature['properties']['fill'] = "#FF6C6C"
            elif Gradignan_count == 5:
                feature['properties']['fill'] = "#FF5D5D"
            elif Gradignan_count == 6:
                feature['properties']['fill'] = "#FF3131"
            else:
                feature['properties']['fill'] = "#FF0000"
            
        for feature['properties']['code'] in "33185":
            if Haillan_count == 0:
                feature['properties']['fill'] = "#FFFFFF"
            elif Haillan_count == 1:
                feature['properties']['fill'] = "#FFDCDC"
            elif Haillan_count == 2:
                feature['properties']['fill'] = "#FFB7B7"
            elif Haillan_count == 3:
                feature['properties']['fill'] = "#FF8686"
            elif Haillan_count == 4:
                feature['properties']['fill'] = "#FF6C6C"
            elif Haillan_count == 5:
                feature['properties']['fill'] = "#FF5D5D"
            elif Haillan_count == 6:
                feature['properties']['fill'] = "#FF3131"
            else:
                feature['properties']['fill'] = "#FF0000"

        for feature['properties']['code'] in "33200":
            if Cauderan_count == 0:
                feature['properties']['fill'] = "#FFFFFF"
            elif Cauderan_count == 1:
                feature['properties']['fill'] = "#FFDCDC"
            elif Cauderan_count == 2:
                feature['properties']['fill'] = "#FFB7B7"
            elif Cauderan_count == 3:
                feature['properties']['fill'] = "#FF8686"
            elif Cauderan_count == 4:
                feature['properties']['fill'] = "#FF6C6C"
            elif Cauderan_count == 5:
                feature['properties']['fill'] = "#FF5D5D"
            elif Cauderan_count == 6:
                feature['properties']['fill'] = "#FF3131"
            else:
                feature['properties']['fill'] = "#FF0000"
            
        for feature['properties']['code'] in "33270":
            if Floirac_Bouliac_count == 0:
                feature['properties']['fill'] = "#FFFFFF"
            elif Floirac_Bouliac_count == 1:
                feature['properties']['fill'] = "#FFDCDC"
            elif Floirac_Bouliac_count == 2:
                feature['properties']['fill'] = "#FFB7B7"
            elif Floirac_Bouliac_count == 3:
                feature['properties']['fill'] = "#FF8686"
            elif Floirac_Bouliac_count == 4:
                feature['properties']['fill'] = "#FF6C6C"
            elif Floirac_Bouliac_count == 5:
                feature['properties']['fill'] = "#FF5D5D"
            elif Floirac_Bouliac_count == 6:
                feature['properties']['fill'] = "#FF3131"
            else:
                feature['properties']['fill'] = "#FF0000"

        for feature['properties']['code'] in "33290":
            if Parempuyre_Blanquefort_count == 0:
                feature['properties']['fill'] = "#FFFFFF"
            elif Parempuyre_Blanquefort_count == 1:
                feature['properties']['fill'] = "#FFDCDC"
            elif Parempuyre_Blanquefort_count == 2:
                feature['properties']['fill'] = "#FFB7B7"
            elif Parempuyre_Blanquefort_count == 3:
                feature['properties']['fill'] = "#FF8686"
            elif Parempuyre_Blanquefort_count == 4:
                feature['properties']['fill'] = "#FF6C6C"
            elif Parempuyre_Blanquefort_count == 5:
                feature['properties']['fill'] = "#FF5D5D"
            elif Parempuyre_Blanquefort_count == 6:
                feature['properties']['fill'] = "#FF3131"
            else:
                feature['properties']['fill'] = "#FF0000"

        for feature['properties']['code'] in "33310":
            if Lormont_count == 0:
                feature['properties']['fill'] = "#FFFFFF"
            elif Lormont_count == 1:
                feature['properties']['fill'] = "#FFDCDC"
            elif Lormont_count == 2:
                feature['properties']['fill'] = "#FFB7B7"
            elif Lormont_count == 3:
                feature['properties']['fill'] = "#FF8686"
            elif Lormont_count == 4:
                feature['properties']['fill'] = "#FF6C6C"
            elif Lormont_count == 5:
                feature['properties']['fill'] = "#FF5D5D"
            elif Lormont_count == 6:
                feature['properties']['fill'] = "#FF3131"
            else:
                feature['properties']['fill'] = "#FF0000"

        for feature['properties']['code'] in "33320":
            if Eysines_taillan_count == 0:
                feature['properties']['fill'] = "#FFFFFF"
            elif Eysines_taillan_count == 1:
                feature['properties']['fill'] = "#FFDCDC"
            elif Eysines_taillan_count == 2:
                feature['properties']['fill'] = "#FFB7B7"
            elif Eysines_taillan_count == 3:
                feature['properties']['fill'] = "#FF8686"
            elif Eysines_taillan_count == 4:
                feature['properties']['fill'] = "#FF6C6C"
            elif Eysines_taillan_count == 5:
                feature['properties']['fill'] = "#FF5D5D"
            elif Eysines_taillan_count == 6:
                feature['properties']['fill'] = "#FF3131"
            else:
                feature['properties']['fill'] = "#FF0000"
        
        for feature['properties']['code'] in "33370":
            if Antigues_count == 0:
                feature['properties']['fill'] = "#FFFFFF"
            elif Antigues_count == 1:
                feature['properties']['fill'] = "#FFDCDC"
            elif Antigues_count == 2:
                feature['properties']['fill'] = "#FFB7B7"
            elif Antigues_count == 3:
                feature['properties']['fill'] = "#FF8686"
            elif Antigues_count == 4:
                feature['properties']['fill'] = "#FF6C6C"
            elif Antigues_count == 5:
                feature['properties']['fill'] = "#FF5D5D"
            elif Antigues_count == 6:
                feature['properties']['fill'] = "#FF3131"
            else:
                feature['properties']['fill'] = "#FF0000"

        for feature['properties']['code'] in "33400":
            if Talence_count == 0:
                feature['properties']['fill'] = "#FFFFFF"
            elif Talence_count == 1:
                feature['properties']['fill'] = "#FFDCDC"
            elif Talence_count == 2:
                feature['properties']['fill'] = "#FFB7B7"
            elif Talence_count == 3:
                feature['properties']['fill'] = "#FF8686"
            elif Talence_count == 4:
                feature['properties']['fill'] = "#FF6C6C"
            elif Talence_count == 5:
                feature['properties']['fill'] = "#FF5D5D"
            elif Talence_count == 6:
                feature['properties']['fill'] = "#FF3131"
            else:
                feature['properties']['fill'] = "#FF0000"

        for feature['properties']['code'] in "33440":
            if Lagrave_count == 0:
                feature['properties']['fill'] = "#FFFFFF"
            elif Lagrave_count == 1:
                feature['properties']['fill'] = "#FFDCDC"
            elif Lagrave_count == 2:
                feature['properties']['fill'] = "#FFB7B7"
            elif Lagrave_count == 3:
                feature['properties']['fill'] = "#FF8686"
            elif Lagrave_count == 4:
                feature['properties']['fill'] = "#FF6C6C"
            elif Lagrave_count == 5:
                feature['properties']['fill'] = "#FF5D5D"
            elif Lagrave_count == 6:
                feature['properties']['fill'] = "#FF3131"
            else:
                feature['properties']['fill'] = "#FF0000"

        for feature['properties']['code'] in "33520":
            if Bruges_count == 0:
                feature['properties']['fill'] = "#FFFFFF"
            elif Bruges_count == 1:
                feature['properties']['fill'] = "#FFDCDC"
            elif Bruges_count == 2:
                feature['properties']['fill'] = "#FFB7B7"
            elif Bruges_count == 3:
                feature['properties']['fill'] = "#FF8686"
            elif Bruges_count == 4:
                feature['properties']['fill'] = "#FF6C6C"
            elif Bruges_count == 5:
                feature['properties']['fill'] = "#FF5D5D"
            elif Bruges_count == 6:
                feature['properties']['fill'] = "#FF3131"
            else:
                feature['properties']['fill'] = "#FF0000"
            
        for feature['properties']['code'] in "33530":
            if Bassens_count == 0:
                feature['properties']['fill'] = "#FFFFFF"
            elif Bassens_count == 1:
                feature['properties']['fill'] = "#FFDCDC"
            elif Bassens_count == 2:
                feature['properties']['fill'] = "#FFB7B7"
            elif Bassens_count == 3:
                feature['properties']['fill'] = "#FF8686"
            elif Bassens_count == 4:
                feature['properties']['fill'] = "#FF6C6C"
            elif Bassens_count == 5:
                feature['properties']['fill'] = "#FF5D5D"
            elif Bassens_count == 6:
                feature['properties']['fill'] = "#FF3131"
            else:
                feature['properties']['fill'] = "#FF0000"

        for feature['properties']['code'] in "33560":
            if Carbon_Blanc_count == 0:
                feature['properties']['fill'] = "#FFFFFF"
            elif Carbon_Blanc_count == 1:
                feature['properties']['fill'] = "#FFDCDC"
            elif Carbon_Blanc_count == 2:
                feature['properties']['fill'] = "#FFB7B7"
            elif Carbon_Blanc_count == 3:
                feature['properties']['fill'] = "#FF8686"
            elif Carbon_Blanc_count == 4:
                feature['properties']['fill'] = "#FF6C6C"
            elif Carbon_Blanc_count == 5:
                feature['properties']['fill'] = "#FF5D5D"
            elif Carbon_Blanc_count == 6:
                feature['properties']['fill'] = "#FF3131"
            else:
                feature['properties']['fill'] = "#FF0000"

        for feature['properties']['code'] in "33600":
            if Pessac_count == 0:
                feature['properties']['fill'] = "#FFFFFF"
            elif Pessac_count == 1:
                feature['properties']['fill'] = "#FFDCDC"
            elif Pessac_count == 2:
                feature['properties']['fill'] = "#FFB7B7"
            elif Pessac_count == 3:
                feature['properties']['fill'] = "#FF8686"
            elif Pessac_count == 4:
                feature['properties']['fill'] = "#FF6C6C"
            elif Pessac_count == 5:
                feature['properties']['fill'] = "#FF5D5D"
            elif Pessac_count == 6:
                feature['properties']['fill'] = "#FF3131"
            else:
                feature['properties']['fill'] = "#FF0000"

        for feature['properties']['code'] in "33700":
            if Merignac_count == 0:
                feature['properties']['fill'] = "#FFFFFF"
            elif Merignac_count == 1:
                feature['properties']['fill'] = "#FFDCDC"
            elif Merignac_count == 2:
                feature['properties']['fill'] = "#FFB7B7"
            elif Merignac_count == 3:
                feature['properties']['fill'] = "#FF8686"
            elif Merignac_count == 4:
                feature['properties']['fill'] = "#FF6C6C"
            elif Merignac_count == 5:
                feature['properties']['fill'] = "#FF5D5D"
            elif Merignac_count == 6:
                feature['properties']['fill'] = "#FF3131"
            else:
                feature['properties']['fill'] = "#FF0000"

        for feature['properties']['code'] in "33810":
            if Ambès_count == 0:
                feature['properties']['fill'] = "#FFFFFF"
            elif Ambès_count == 1:
                feature['properties']['fill'] = "#FFDCDC"
            elif Ambès_count == 2:
                feature['properties']['fill'] = "#FFB7B7"
            elif Ambès_count == 3:
                feature['properties']['fill'] = "#FF8686"
            elif Ambès_count == 4:
                feature['properties']['fill'] = "#FF6C6C"
            elif Ambès_count == 5:
                feature['properties']['fill'] = "#FF5D5D"
            elif Ambès_count == 6:
                feature['properties']['fill'] = "#FF3131"
            else:
                feature['properties']['fill'] = "#FF0000"

    # save the map to an html file
    with open("result.json", 'w+') as f:
        json.dump(cities_data, f, indent=2)

if Merignac_count == 1:
    print("1")
elif Merignac_count == 2:
    print("2")
elif Merignac_count == 3:
    print("3")
