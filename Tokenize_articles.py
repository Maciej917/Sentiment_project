from textblob import TextBlob
from CSV_manipulation import CSV_manipulation
import nltk
from nltk.corpus import stopwords
import pandas as pd


###################To nie ma jeszcze class, nie patrz##############################
art_df = pd.read_csv('art_body_text.csv')

art_head = art_df.loc[:,"title"]
art_body = art_df.loc[:,"body"]
art_date = art_df.loc[:,"date"]

stopwords = set(stopwords.words("english"))
ps = nltk.PorterStemmer()
#lemitazer = nltk.WordNetLemmatizer()

for article in art_body:
    sentences = nltk.sent_tokenize(article)
    words_not_cleared = nltk.word_tokenize(article)
    words_semi_clear= []
    for word in words_not_cleared:
        if word not in stopwords:
            stem_word = ps.stem(word)
           # lem_word = lemitazer.lemmatize(word)
            words_semi_clear.append(stem_word)
    print(words_semi_clear)




    # print(words)
    # print("------------------------------------------------")






# for article in art_body:
#     paragraph_list = list(article.split("',"))
#   #  print(paragraph_list)
#     print('###########################################################3')
#     for paragraph in paragraph_list:
#         paragraph_blob = TextBlob(paragraph)
#         print(paragraph)
#         print(paragraph_blob.sentiment)
#         print("______________--------------______________")




