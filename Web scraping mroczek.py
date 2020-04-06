import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np

# definiowanie URL
ticker = {"MSFT"}
url_test = "https://www.marketwatch.com/investing/stock/{}/profile"
for i in ticker:
    url = url_test.format(i)
    print(url)

# tworzenie requestu
r1 = requests.get(url)
r1.status_code

coverpage = r1.content

soup1 = BeautifulSoup(coverpage, 'html.parser')
coverpage_news = soup1.find_all('li', class_='fnewsitem')
print(len(coverpage_news))

print(coverpage_news[4])
number_of_articles = 1

content_of_news = []
list_of_links = []
list_of_titles = []

for n in np.arange(0, number_of_articles):

    #linki
    link1 = coverpage_news[n].find('a')['href']
    link = "https://www.marketwatch.com" + link1
    list_of_links.append(link)

    #tytuły
    title = coverpage_news[n].find('a').get_text()
    list_of_titles.append(title)

    # Treść
    article = requests.get(link)
    article_content = article.content
    soup_article = BeautifulSoup(article_content, 'html5lib')
    x = soup_article.find_all('p')


    paragraph_list = []
    for p in np.arange(0,len(x)):
        paragraph = x[p].get_text()
        paragraph_list.append(paragraph)
        final_article = " ".join(paragraph_list)

    content_of_news.append(final_article)

df_features = pd.DataFrame(
    {'Article Content': content_of_news
     })

df_show_info = pd.DataFrame(
    {'Article Title': list_of_titles,
     'Article Link': list_of_links})
np.savetxt("articles.csv", ('list_of_links','list_of_titles','content_of_news')