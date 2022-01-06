from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import certifi
import Open_Advuta_help
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pickle
import time
start_time = time.time()

chrome_option = Options()
prefs = {'profile.default_content_setting_values': {'images': 0,
                            'plugins': 1, 'fullscreen': 1}}

chrome_option.add_experimental_option('prefs', prefs)
chrome_option.add_argument('headless')
chrome_option.add_argument('window-size=0x0')
chrome_option.add_argument("disable-infobars")
chrome_option.add_argument("--disable-extensions")
driver = webdriver.Chrome('C:\\Users\\777\\PycharmProjects\\prob\\webdrivers\chromedriver.exe',
                          options=chrome_option)

all_links = Open_Advuta_help.olol
class Advita_url_help:
    def __init__(self,insert_Address):
        self.insert_Address = insert_Address

    def get_urlopen(self):
        C = []
        for i in self.insert_Address:
            open_url = urlopen(i,
                               context=ssl.create_default_context(cafile=certifi.where()))
            soup = BeautifulSoup(open_url, 'html.parser')
            for link in soup.find_all(class_='card__name'):  ##Достаем все ссылки
                z = [a['href'] for a in link.find_all('a')]
                for tro in z:
                    a = 'https://advita.ru/podopechnye' + tro.replace('.', '')
                    C.append(a)
        with open('list_death_all_url', 'wb') as fp:
            return pickle.dump(C, fp)
help_url = Advita_url_help(all_links)
my_list_help = help_url.get_urlopen()
print('1:'+str(start_time-time.time()))

