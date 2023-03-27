import requests
import json
from bs4 import BeautifulSoup

# URL of the page to scrape
url = 'https://www.tripadvisor.fr/Attraction_Review-g187079-d10344773-Reviews-Le_reseau_de_transports_TBM_Tramway-Bordeaux_Gironde_Nouvelle_Aquitaine.html'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the <div> element with the specified class
div = soup.find('div', {'class': 'biGQs _P pZUbB KxBGd'})

# Find all <span> elements with the specified class within the <div>
spans = div.find_all('span', {'class': 'yCeTE'})

# Convert the list of <span> elements to a list of their text content
spans_text = [span.get_text() for span in spans]

# Create a dictionary containing the list of <span> texts
data = {'text': spans_text}

# Export the data as JSON to a file
with open('output.json', 'w') as file:
    json.dump(data, file)


print(response)