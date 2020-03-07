from selenium import webdriver
import time
from CSV_manipulation import CSV_manipulation


class Scrapbot:
    def __init__(self, company=""):
        if company == "":
            print("You didn't type company name")
            exit()
        self.bot = webdriver.Chrome()
        self.company = company


    def openpage(self):
        ''' Funkcja openpage otwiera Reutersa na stronie danej firmy. '''
        self.bot.get("https://www.reuters.com/companies/{}.OQ".format(self.company))
        time.sleep(1)
        self.bot.find_element_by_id("_evidon-banner-acceptbutton").click()
        time.sleep(1)


    def scrap_list_of_art(self, times_of_scroll=0):
        ''' Funkcja scrap_list_of_art ściąga ze strony linki do artykułów. Wywołująć funkcję możemy wybrać ilość razy jaką funkcja. '''
        art_heads_url_list = []
        for x in range(times_of_scroll):
            self.bot.execute_script("window.scrollBy(0,document.body.scrollHeight)")
            time.sleep(2)
        for art_head in self.bot.find_elements_by_class_name('MarketStoryItem-headline-2cgfz'):
            art_heads_url_list.append(art_head.get_attribute("href"))
        print(art_heads_url_list)

        CSV_manipulation('art_list.csv').write_csv(art_heads_url_list)
        return art_heads_url_list


    def end(self):
        ''' Funkcja wyłącza webdriver. '''
        self.bot.close()



################# Przykładowe wywołanie #######################

#scrap = Scrapbot("GOOGL")
#scrap.openpage()
#scrap.scrap_list_of_art(1)
#scrap.end()