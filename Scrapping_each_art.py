from bs4 import BeautifulSoup
import requests
import pandas as pd
from CSV_manipulation import CSV_manipulation


def scrapping_articles( art_list_csv_file, web_header):
    """Metoda służąca do wyciągania Nagłówka, Treści oraz Daty z linków artykułów z 'art_list_csv_file'.
    'header' można pobrać z z przeglądarki wpisując 'my user-agent'. """
    art_url_list = CSV_manipulation(art_list_csv_file).read_csv(0)
    art_num = 0
    art_database = []
    for art_url in art_url_list:
        # print(art_url)
        # print("-------------------------------------------------------------------------")
        art_num += 1
        requested_page = requests.get(art_url, headers={'User-Agent': web_header})
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
        df.to_csv("art_body_text.csv", header=True, index=True)
        # return df




################# Przykładowe wywołanie #######################

# scrapping_articles('art_list.csv', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36').head(5))


