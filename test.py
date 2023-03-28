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


    Pessac_Centre = ("Pessac-Centre", "Pessac Centre", "Pessac","pessac-centre", "pessac centre", "pessac")
    Bordeaux_Saint_Jean = ("Bordeaux-Saint-Jean", "Bordeaux Saint Jean", "Saint-Jean", "Saint Jean", "bordeaux-saint-jean", "bordeaux saint jean", "saint-jean", "saint jean", "la gare")
    Merignac_Arlac = ("Merignac-Arlac", "Merignac Arlac", "Arlac", "Merignac", "merignac-arlac", "merignac arlac", "arlac", "merignac")
    Cauderan_Merignac = ("Cauderan-Merignac", "Cauderan Merignac", "Cauderan", "Merignac", "cauderan-merignac", "cauderan merignac", "cauderan", "merignac")
    Bruges = ("Bruges", "Bruges")
    Blanquefort = ("Blanquefort", "blanquefort")
    Parempuyre = ("Parempuyre", "parempuyre")
    Eysines = ("Eysines", "eysines")
    Pessac_Centre_count = 0
    Bordeaux_Saint_Jean_count = 0
    Merignac_Arlac_count = 0
    Cauderan_Merignac_count = 0
    Bruges_count = 0
    Blanquefort_count = 0
    Parempuyre_count = 0
    Eysines_count = 0



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


        elif word in Pessac_Centre:
            Pessac_Centre_count += 1

        elif word in Bordeaux_Saint_Jean:
            Bordeaux_Saint_Jean_count += 1

        elif word in Merignac_Arlac:
            Merignac_Arlac_count += 1

        elif word in Cauderan_Merignac:
            Cauderan_Merignac_count += 1

        elif word in Bruges:
            Bruges_count += 1

        elif word in Blanquefort:
            Blanquefort_count += 1

        elif word in Parempuyre:
            Parempuyre_count += 1

        elif word in Eysines:
            Eysines_count += 1
    

    print("nombre de mention de bus:" , bus_count)
    print("nombre de mention de tram:" , tram_count)
    print("nombre de mention de v3:" , v3_count)


    print("nombre de bonne apressiation:" , good_count)
    print("nombre de mauvaise apressiation:" , bad_count)


    print("nombre de mention parlant de Pessac-Centre:" , Pessac_Centre_count)
    print("nombre de mention parlant de Bordeaux-Saint-Jean" , Bordeaux_Saint_Jean_count)
    print("nombre de mention parlant de Merignac-Arlac" , Merignac_Arlac_count)
    print("nombre de mention parlant de Cauderan-Merignac" , Cauderan_Merignac_count)
    print("nombre de mention parlant de Bruges" , Bruges_count)
    print("nombre de mention parlant de Blanquefort" , Blanquefort_count)
    print("nombre de mention parlant de Parempuyre" , Parempuyre_count)
    print("nombre de mention parlant de Eysines" , Eysines_count)


# Load the map of the cities from the JSON file
with open('cities.json') as bordeaux:
    cities_data = json.load(bordeaux)

# Create a folium.Map object with the coordinates of the center of the map and the initial zoom level
center = [40.7128, -74.0060] # Coordinates for New York City
zoom = 10
map = folium.Map(location=center, zoom_start=zoom)

# Iterate through the cities data and create a folium.CircleMarker object for each city with a radius proportional to the number of points in that city
max_points = max(city['points'] for city in cities_data)
for city in cities_data:
    name = city['name']
    latitude = city['latitude']
    longitude = city['longitude']
    points = city['points']
    radius = points / max_points * 10
    color = 'red'
    fill_color = 'red'
    fill_opacity = 0.5
    folium.CircleMarker(location=[latitude, longitude], radius=radius, color=color, fill_color=fill_color, fill_opacity=fill_opacity, popup=name).add_to(map)

# Save the map to an HTML file
map.save('heatmap.html')