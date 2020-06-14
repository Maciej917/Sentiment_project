from bs4 import BeautifulSoup, SoupStrainer
import requests
import pandas as pd
import pickle
import numpy as np

#Scraping danych z RSS Google (bez pełnej treści)
url = 'https://www.google.com/alerts/feeds/06940609537670719478/16876315740763892156'

resp = requests.get(url)
soup = BeautifulSoup(resp.content, "lxml")
items = soup.findAll('entry')
news_items = []
print(items)

for entry in items:
    news_item = {}
    news_item['title'] = entry.title.text,
    news_item['preview'] = entry.content.text,
    news_item['published'] = entry.published.text,
    news_item['updated'] = entry.updated.text,
    news_item['link'] = entry.link['href']
    news_items.append(news_item)

pickle.dump(scraping,outfile)
outfile.close()

# stworzyć funkcję do automatycznej aktualizacji i usuwania duplikatów a potem dodającą unique ID