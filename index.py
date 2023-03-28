import requests
import json
from bs4 import BeautifulSoup
import urllib3
from http.client import responses
from unidecode import unidecode

#Target URL
url = "https://www.petitfute.com/v1524-bordeaux-33000/c1122-voyage-transports/c1145-avion-bateau-bus-train-taxi-parking/c1154-transport-urbain/98794-tbm.html"

#Get the HTTP code
http = urllib3.PoolManager()
request = http.request('GET', url)
http_status = request.status
http_status_description = responses[http_status]
print("code status:" , http_status , http_status_description)


#Parse the HTML content of the page
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
spans = soup.find_all('div', {'class': 'comment-truncate'})

count = 0
with open('data.json', 'a') as f:
    for span in spans:
        spans_text = [span.get_text()]
        element = ["id:", count, ";" , spans_text]
        json.dump(element, f)
        f.write('\n')
        count += 1
