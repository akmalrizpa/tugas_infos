import json
from bs4 import BeautifulSoup
import requests

html_doc = requests.get('https://ukpim.my.id/event')

soup = BeautifulSoup(html_doc.text, 'html.parser')

title = []
waktu = []
status = []

juduls = soup.select('.item-content')





for judul in soup.select('.item-content'):
    title.append(judul.find('a').get_text())
    waktu.append(judul.find('span', class_='date').text)
    status.append(judul.find('span', class_='badge-pill').text)



vartemp = []
for x in range(len(title)):
    vartemp.append({
                "Nama Event" : title[x],
                "Waktu Event" : waktu[x],
                "Status" : status[x]
    })



# Serializing json 
json_object = json.dumps(vartemp, indent = 4)
  
# Writing to sample.json
with open("akmalrizpa.json", "a") as outfile:
    outfile.write(json_object)