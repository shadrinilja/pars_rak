from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pickle
import operator
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
with open('list_ill_sort', 'rb') as fp:
    _const_illness = pickle.load(fp)

class Sorting_list_life:
    def __init__(self, lil):
        self.lil = lil

    def open_picle_file(self):
        with open(self.lil, 'rb') as fp:
            list_life = pickle.load(fp)
        return list_life
    def sort_iln(self):
        sorted_list_url = []
        for item in self.open_picle_file():
            try:
                A = []
                B = []
                driver.get(item)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                for citi in soup.find_all(class_='patient__property'):
                    B.append(citi.get_text())
                new_list = [j for i, j in enumerate(B) if i not in [2, 3, 5, 6]]
                print(new_list)
                diagnos = new_list[2].split(':')
                tro = diagnos[1].lstrip(' ')
                print(tro)
                if tro in _const_illness:
                    sorted_list_url.append(item)
                    print('добавленно')
            except IndexError:
                A.append(' ')
        with open('sort_need_help_nou_url_list', 'wb') as fp:
            return pickle.dump(sorted_list_url, fp)
SORT_URL = Sorting_list_life('Need_help_now_url_list')
op = SORT_URL.open_picle_file()
all_sorted_url = SORT_URL.sort_iln()
print('1:'+str(start_time-time.time()))

