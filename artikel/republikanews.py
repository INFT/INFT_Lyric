import requests
import datetime
import json
from bs4 import BeautifulSoup

republikanews = {}

all = []

page = requests.get("https://www.republika.co.id/")
obj = BeautifulSoup(page.text,'html.parser');

for headline in obj.find_all('div', class_='teaser_conten1'):
    republikanews["kategori"] = json.dumps(headline.find('h1').text)
    republikanews["tittle"] = json.dumps(headline.find('h2').text)
    date = datetime.datetime.now()
    republikanews["tgl"] = date.strftime("%A")+", "+date.strftime("%d")+" "+date.strftime("%B")+" "+date.strftime("%Y")
    republikanews["waktu"] = json.dumps(headline.find('div', class_='date').text)

    all.append (dict(republikanews))
    v = all
    print(republikanews)

with open ("news.json", "w") as file:
    json.dump(v, file, indent = 4)
