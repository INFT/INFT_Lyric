import requests
import json
import time
from bs4 import BeautifulSoup


my_dict = {}

page = requests.get("https://www.republika.co.id/")
obj = BeautifulSoup(page.text, 'html.parser')
all = []
for headline in obj.find_all('div',class_='teaser_conten1'):
    x = json.dumps(headline.find('h1').text)
    y = json.dumps(headline.find('h2').text)
    z = json.dumps(headline.find('div', class_='date').text)
    u = json.dumps(time.time())
    my_dict['Kategori']=x
    my_dict['Judul']=y
    my_dict['Waktu']=z   
    my_dict['pengambilan']=u
    
    all.append( dict(my_dict))    
    

dict_web = all
with open('scrap.json', 'w') as file:
    json.dump(dict_web, file, indent=5)


   
