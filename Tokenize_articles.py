from textblob import TextBlob
from CSV_manipulation import CSV_manipulation
import pandas as pd

art_df = pd.read_csv('art_body_text.csv')

art_head = art_df.loc[:,"title"]
art_body = art_df.loc[:,"body"]
art_date = art_df.loc[:,"date"]


for article in art_body:
    paragraph_list = list(article.split("',"))
  #  print(paragraph_list)
    print('###########################################################3')
    for paragraph in paragraph_list:
        paragraph_blob = TextBlob(paragraph)
        print(paragraph)
        print(paragraph_blob.sentiment)
        print("______________--------------______________")






'''
for article in art_body:
    paragraph_list = list(article.split("',"))
    print(paragraph_list)
    print('###########################################################3')
    for paragraph in paragraph_list:

        print(type(paragraph))
        print(paragraph)
        print("______________--------------______________")
'''
