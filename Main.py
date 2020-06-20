from Scrapping_Reuters import Scrapbot
from Scrapping_each_art import scrapping_articles
import Modifing_csv_data as modif_csv
import Tokenize_articles as tok
import pandas



class Main_program:
    """ Tutaj będziemy puszczać nasz główny program. Narazie to placeholder. """
    Scrapping_begin = Scrapbot("GOOGL")
    Scrapping_begin.openpage()
    Scrapping_begin.scrap_list_of_art(30)
    Scrapping_begin.end()
    scrapping_articles('art_list.csv', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36')
    modif_csv.modifing_reuters_date("art_body_text.csv")
    modif_csv.mergingstooqwithart("art_body_text_2.csv")
    tok.adding_sentiment_of_art_to_df("art_body_text_2.csv")


# Main_program()