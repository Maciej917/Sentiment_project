
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import PorterStemmer
from nltk import PunktSentenceTokenizer
from nltk.corpus import state_union

print("----------------------Go fuck yourself-----------------------")
data = pd.read_csv("microinvop.csv", delimiter=";", engine='python')

df = pd.DataFrame(data, columns=['ws_order', 'ws_url', 'link', 'link_href', 'tekst', 'date'])
tekst_label = df.loc[:, 'tekst']
link_label = df.loc[:, 'link']

df["word count"] = tekst_label.apply(lambda x: len(str(x).split(" ")))
df["word lenght"] = tekst_label.apply(lambda x: len(str(x)))
df["tekst"] = df["tekst"].str.lower()

tokenized_tekst = [word_tokenize(str(sentence)) for sentence in tekst_label ]
sent_token_tekst = [sent_tokenize(str(sentence)) for sentence in tekst_label]


############-Scrypt do znajdowania przymiotnikow/rzeczownikow/symboli itp. w tekscie-################
stop_words = stopwords.words('english')
data_tagged = []
for line in sent_token_tekst:
    for sentence in line:
        data_tagged = data_tagged + nltk.pos_tag(word_tokenize(sentence))
print(data_tagged)
for word in data_tagged:
    if word[1] == "NN":
        print(word)


############-Scrypt do tokenizacji słów w tekscie-################

New_list = []
for sentence in tokenized_tekst:
    for word in sentence:
        if word not in stop_words:
            New_list.append(word)

ps = PorterStemmer()
stemed_list = [ps.stem(str(sentence)) for sentence in New_list]

print(tokenized_tekst)
print(stemed_list)





'''url = "https://www.investing.com/news/"
header = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
uClient = urlopen(url)
pagehtml = uClient.read()

#html parsing
page_soup = soup(pagehtml, "html.parser")


#grabs each news

news = page_soup.findAll('div', {"class":"largeTitle marginAfterTabs"})
newslen = len(news)
print(newslen)'''

'''with open('DBtest.csv', mode = 'wb')as DBfile:
    DBwriter = csv.writer(DBfile,delimiter = ',')
    for line in page_soup:
        DBwriter.writerow(line)'''

