from selenium import webdriver
import time
import csv


class Scrapbot:
    def __init__(self, company=""):
        if company == "":
            print("You have to type short company name")
            exit()
        self.bot = webdriver.Chrome("C:\Pliki własne\webdrivers\chromedriver")
        self.company = company

    #######Funkcja openpage otwiera Reutersa na stronie danej firmy########

    def openpage(self):
        self.bot.get("https://www.reuters.com/companies/{}.OQ".format(self.company))
        time.sleep(1)
        self.bot.find_element_by_id("_evidon-banner-acceptbutton").click()
        time.sleep(1)

    ########Funkcja scrap_list_of_art ściąga ze strony linki do artykułów. Wywołująć funkcję możemy wybrać ilość razy jaką funkcja

    def scrap_list_of_art(self, times_of_scroll=0):
        art_heads_url_list = []
        for x in range(times_of_scroll):
            self.bot.execute_script("window.scrollBy(0,document.body.scrollHeight)")
            time.sleep(2)
        for art_head in self.bot.find_elements_by_class_name('MarketStoryItem-headline-2cgfz'):
            art_heads_url_list.append(art_head.get_attribute("href"))
        print(art_heads_url_list)
        with open('art_list.csv', 'w') as art_list_csv:
            csv_writer = csv.writer(art_list_csv, delimiter = ',')
            csv_writer.writerow(art_heads_url_list)


    #########Funkcja wyłącza webdriver#########

    def end(self):
        self.bot.close()



################# Przykładowe wywołanie #######################

# scrap = Scrapbot("GOOGL")
# scrap.openpage()
# scrap.scrap_list_of_art(10)
# scrap.end()