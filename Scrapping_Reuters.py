from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import json


class Scrapbot:
    def __init__(self, company=""):
        if company == "":
            print("You have to type short company name")
            exit()
        self.bot = webdriver.Chrome("C:\Pliki własne\webdrivers\chromedriver")
        self.company = company

    #######Funkcja openpage otwiera Reutersa na stronie danej firmy########

    def openpage(self):
        url = "https://www.reuters.com/companies/{}.OQ".format(self.company)
        bot = self.bot
        bot.get(url)
        time.sleep(1)
        cockie = bot.find_element_by_id("_evidon-banner-acceptbutton")
        cockie.click()
        time.sleep(1)

    ########Funkcja scrap_list_of_art ściąga ze strony linki do artykułów. Wywołująć funkcję możemy wybrać ilość razy jaką funkcja

    def scrap_list_of_art(self, times_of_scroll=0):
        bot = self.bot
        art_heads_url_list = []
        for x in range(times_of_scroll):
            bot.execute_script("window.scrollBy(0,document.body.scrollHeight)")
            time.sleep(2)
        art_heads = bot.find_elements_by_class_name('MarketStoryItem-headline-2cgfz')
        for art_head in art_heads:
            art_head_url = art_head.get_attribute("href")
            art_heads_url_list.append(art_head_url)
        art_url_list_json = json.dumps(art_heads_url_list)
        with open('art_list_json.json', 'w') as art_list_json:
            json.dump(art_heads_url_list, art_list_json, indent=2)

    #########Funkcja wyłącza webdriver#########

    def end(self):
        bot = self.bot
        bot.close()
