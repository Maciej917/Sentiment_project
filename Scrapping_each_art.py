import csv
from bs4 import BeautifulSoup
import requests
import pandas as pd




class Scrapping_art_page:

    def __init__(self, art_list_csv_file):
        art_url_list = []
        with open(art_list_csv_file, 'r') as art_list_csv:
            art_url_reader = csv.reader(art_list_csv)
            for x in art_url_reader:
                art_url_list.append(x)
        self.art_url_list = art_url_list[0]

    def Scrapping(self, header):
        art_num = 0
        art_database = []
        for art_url in  self.art_url_list:
            art_num += 1
            requested_page = requests.get(art_url, headers = {'User-Agent': header})
            page_soup = BeautifulSoup(requested_page.content, 'html.parser')
            art_title = page_soup.find('h1', class_='ArticleHeader_headline')
            art_date = page_soup.find('div', class_='ArticleHeader_date')
            art_body = page_soup.find('div', class_='StandardArticleBody_body')
            article_title = art_title.get_text()
            article_date = art_date.get_text()
            art_paragraps = []
            try:
                p_num = 0
                for p in art_body:
                    if p.name == 'p':
                        p_num += 1
                        art_paragraps.append(p.get_text())
            except TypeError:
                print("Something has fucked up")
            art_database.append([article_title, article_date, art_paragraps])

        df = pd.DataFrame(art_database, columns = ['title', 'date', 'body'])
        return df



################# Przykładowe wywołanie #######################

# scrap = Scrapping_art_page('art_list.csv')
# scrap.Scrapping('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36')







