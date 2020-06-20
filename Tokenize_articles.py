from textblob import TextBlob
from CSV_manipulation import CSV_manipulation
import nltk
from nltk.corpus import stopwords
import pandas as pd
from nltk.tokenize import TabTokenizer
import Modifing_csv_data as modif_csv
# nltk.downloader('punkt')



def word_tokenizer(text):

        words_not_cleared = nltk.word_tokenize(text)
        print(words_not_cleared)
        words_semi_clear = []
        for word in words_not_cleared:
            if word not in set(stopwords.words("english")):
                if word.isalnum():
                    stem_word = nltk.PorterStemmer(word)
                    # lemma_word = nltk.WordNetLemmatizer(word)
                    # lem_word = lemitazer.lemmatize(word)
                    words_semi_clear.append(stem_word)
            print(words_semi_clear)
        return words_not_cleared

def textblob_sent(text):
    tokenizer = TabTokenizer()
    textblob = TextBlob(text, tokenizer=tokenizer).sentiment
    # if textblob[0] > 0.2:
    #     print('Positive -- {}'.format(textblob))
    # elif textblob[0] < 0.2:
    #     print('Negative -- {}'.format(textblob))
    return textblob

def adding_sentiment_of_art_to_df(file):
    article_df = modif_csv.extract_df_from_file(file)
    art_sentiment = []
    art_sentiment_value = []
    for article in article_df.loc[:,'body']:
        if textblob_sent(article)[0] > 0.1:
            art_sentiment.append('Positive')
            art_sentiment_value.append(textblob_sent(article))

        elif textblob_sent(article)[0] < -0.2:
            art_sentiment.append('Negative')
            art_sentiment_value.append(textblob_sent(article))
        else:
            # print('Neutral -- {}'.format(tok.textblob_sent(article)))
            art_sentiment.append('Neutral')
            art_sentiment_value.append(textblob_sent(article))
    article_df.insert(3, 'Sentiment', art_sentiment)
    article_df.insert(4, 'Sentiment value', art_sentiment_value)
    article_df.to_csv("art_data_with_sentiment.csv", header=True, index=True)

# print(textblob_sent("this is great computer"))
# print(textblob_sent("this is bad computer"))


