from Scrapping_Reuters import Scrapbot
from Scrapping_each_art import Scrapping_art_page




class Main_program:
    """ Tutaj będziemy puszczać nasz główny program. Narazie to placeholder. """
    Scrapping_begin = Scrapbot("GOOGL")
    Scrapping_begin.openpage()
    Scrapping_begin.scrap_list_of_art(30)
    Scrapping_begin.end()
    Scrapping_art_page().Scrapping_articles('art_list.csv', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36')

Main_program()