import json
from bs4 import BeautifulSoup
from http.client import responses
from tkinter import *
from tkinter.messagebox import *
import customtkinter
import os
import cloudscraper
import urllib3
from alive_progress import alive_it
urllib3.disable_warnings()


websites = {
  "Exemple 1": {
    "URL": "https://www.example.com",
    "Balise": "div",
    "Class": "exemple"
  },
  "Exemple 2": {
    "URL": "https://www.example.com",
    "Balise": "div",
    "Class": "exemple"
  },
}


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
    count = 1
    for website in alive_it(websites):
        EnumerateWebsite = len(websites)
        if count == EnumerateWebsite:
            showinfo(title="Attention", message="Scraping terminé")
        else:
            try: 
                URL = websites[website]["URL"]
                Balise = websites[website]["Balise"]
                Class_ = websites[website]["Class"]

                http = urllib3.PoolManager()
                request = http.request('GET', URL, timeout=5.0)
                http_status = request.status
                print(http_status)
                    
                # Parse the HTML content of the page
                scraper = cloudscraper.create_scraper(delay=10, interpreter='nodejs')
                response = scraper.get(URL).text
                soup = BeautifulSoup(response, 'html.parser')

                # Parse only the content we want
                spans = soup.find_all(Balise, Class_)
                ExecuteCode(spans)
                count += 1
            except:
                showwarning(title="Attention", message="Connection à "+ website + " impossible")
                count += 1
                continue

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
        request = http.request('GET', URL, timeout=5.0)
        http_status = request.status
        print(http_status)
    except:
        showwarning(title="Attention", message="Connection à "+ selected_website + " impossible")
    if http_status == 404:
        showwarning(title="Attention", message="Connection à "+ selected_website + " impossible")
    else:
        try:
            # Parse the HTML content of the page
            scraper = cloudscraper.create_scraper(delay=10, interpreter='nodejs')
            response = scraper.get(URL).text
            soup = BeautifulSoup(response, 'html.parser')
            # Parse only the content we want
            spans = soup.find_all(Balise, Class_)
            ExecuteCode(spans)
            showinfo(title="Attention", message="Scraping terminé")
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
        request = http.request('GET', url_value_URL.get(), timeout=5.0)
        http_status = request.status
        print(http_status)
    except:
        showwarning(title="Attention", message="Connection au site impossible")
    if http_status == 404:
        showwarning(title="Attention", message="Connection au site impossible")
    else:
        # Parse the HTML content of the page
        scraper = cloudscraper.create_scraper(delay=10, interpreter='nodejs')
        response = scraper.get(url_value_URL.get()).text

        soup = BeautifulSoup(response, 'html.parser')
        ExecuteCode(soup)
        showinfo(title="Attention", message="Scraping terminé")

def PERSONALIZED_StartCodeBalise():
    try:
        http = urllib3.PoolManager()
        request = http.request('GET', url_value_Balise.get(), timeout=5.0)
        http_status = request.status
        print(http_status)
    except:
        showwarning(title="Attention", message="Connection au site impossible")
    if http_status == 404:
        showwarning(title="Attention", message="Connection au site impossible")
    else:
        # Parse the HTML content of the page
        scraper = cloudscraper.create_scraper(delay=10, interpreter='nodejs')
        response = scraper.get(url_value_Balise.get()).text

        soup = BeautifulSoup(response, 'html.parser')
        # Parse only the content we want
        spans = soup.find_all(balise_value_Balise.get(), timeout=5.0)
        ExecuteCode(spans)
        showinfo(title="Attention", message="Scraping terminé")

def PERSONALIZED_StartCodeClasse():
    try:
        http = urllib3.PoolManager()
        request = http.request('GET', url_value_Classe.get(), timeout=5.0)
        http_status = request.status
        print(http_status)
    except:
        showwarning(title="Attention", message="Connection au site impossible")
    if http_status == 404:
        showwarning(title="Attention", message="Connection au site impossible")
    else:
        # Parse the HTML content of the page
        scraper = cloudscraper.create_scraper(delay=10, interpreter='nodejs')
        response = scraper.get(url_value_Classe.get()).text
        
        soup = BeautifulSoup(response, 'html.parser')
        # Parse only the content we want
        spans = soup.find_all(balise_value_Classe.get(), {'class': class_value_Classe.get()}, timeout=5.0)
        ExecuteCode(spans)
        showinfo(title="Attention", message="Scraping terminé")


##########################################################################################################################################################################
##########################################################################################################################################################################
# General DEF
##########################################################################################################################################################################
##########################################################################################################################################################################

datalocation = os.getcwd()
datalocation = os.path.join(datalocation, "result", "data.json")

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

##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
# GUI
##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################
root = customtkinter.CTk()
root.title("Hower - Web-scraping")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
root.geometry('715x500')
root.resizable(False, False)





###################################################################################
###################################################################################
# Tabview for "ONE websites to scrap"
###################################################################################
###################################################################################
root.tabview = customtkinter.CTkFrame(root)
root.tabview.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")
# Label for the title
label = customtkinter.CTkLabel(root.tabview, text="Predefined:")
label.pack()

# Get the names of the website to scrap
website_names = list(websites.keys())
optionmenu = customtkinter.CTkOptionMenu(root.tabview, values=website_names)
optionmenu.pack()

# Checkbox to select if the user wants to scrap all the pages
checkbox = customtkinter.CTkCheckBox(root.tabview, text="Every websites")
checkbox.pack(pady=(60, 0))

#Button to take start ONE_StartCode with the website selected
button = customtkinter.CTkButton(root.tabview, text="Start the scaping", command=check_checkbox)
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
Button = customtkinter.CTkButton(root.tabview.tab("URL"), text="Start the scaping", command=PERSONALIZED_StartCodeURL)
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
Button = customtkinter.CTkButton(root.tabview.tab("Balise"), text="Start the scaping", command=PERSONALIZED_StartCodeBalise)
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
Button = customtkinter.CTkButton(root.tabview.tab("Classe"), text="Start the scaping", command=PERSONALIZED_StartCodeClasse)
Button.grid(padx=10, pady=30)





###################################################################################
###################################################################################
# Tabview to show the result 
###################################################################################
###################################################################################
label.textbox2 = customtkinter.CTkTextbox(root)
label.textbox2.grid(row=2, column=0, columnspan=3, padx=(20, 0), pady=(20, 0), sticky="nsew")


root.mainloop()