from itertools import product
from urllib.parse import urlsplit, parse_qs, urlencode
from bs4 import BeautifulSoup
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
class Collection_link:
    def __init__(self,insert_start_url):
        self.insert_start_url = insert_start_url
    def pars_query(self):
        B = []
        for i in range(2020, 2022):
            for k in range(1, 13):
                query = urlsplit(self.insert_start_url).query
                params = parse_qs(query)
                for key, val in params.items():
                    if len(val) == 1:
                        params[key] = val[0]
                params['year'] = i
                params['month'] = k
                tro = urlsplit(self.insert_start_url).scheme + '://' + urlsplit(self.insert_start_url).netloc\
                      + urlsplit(self.insert_start_url).path + \
                      '?' + urlencode(params)
                B.append(tro)
        return (B)

MY_URL =Collection_link('https://rusfond.ru/reportdestitutes?year=2021&month=12')
all_url = MY_URL.pars_query()



with open('list_ill_sort', 'rb') as fp:
    _const_sort_illness = pickle.load(fp)
class Rusdtafond:
    def __init__(self, reqw):
        self.reqw = reqw

    def get_soup(self):
        driver.get(self.reqw)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        return soup
    def name(self):
        B = []
        for name in self.get_soup().find_all(class_='distribution-person-name'):
            B.append(name.text.replace(',',''))
        return B
    def age(self):
        B = []
        for age in self.get_soup().find_all(class_='distribution-person-age'):
            B.append(age.get_text())
        return B
    def city(self):
        A = []
        city = 'город не указан'
        for col in self.get_soup().find_all(class_='distribution-person-amount_digit collected_digit'):
            A.append(city)
        return A
    def illness(self):
        list_illness = []
        for illness in self.get_soup().find_all(class_='distribution-person'):
            for tro in illness.find_all('td')[1]:
                lo = tro[0].upper() + tro[1:]
                pe = lo.split(',')
                list_illness.append(pe[0])
        return list_illness
    def required(self):
        required = []
        for illness in self.get_soup().find_all(class_='distribution-person'):
            for tro in illness.find_all('td')[1]:
                lo = tro[0].upper() + tro[1:]
                pe = lo.split(',')
                pepe = ', '.join(pe[1:])
                required.append(pepe)
        return required
    def amount_collected(self):
        collected ='сумма собрана'
        a = []
        for col in self.get_soup().find_all(class_='distribution-person-amount_digit collected_digit'):
            a.append(collected)
        return a
    def sum_plus(self):
        A = []
        for sum in self.get_soup().find_all(class_= 'distribution-person-amount_digit collected_digit'):
            A.append(sum.text.replace(u'\xa0', u' '))
        return A
    def uniq(self):
        zipped = [list(t) for t in zip(self.name(), self.age(), self.city(), self.illness(), self.required(),
                                       self.amount_collected(), self.sum_plus())]
        return zipped

my_list_dict = []

for i in all_url:
    print(i)
    tro = Rusdtafond(i)
    name = tro.name()
    age = tro.age()
    citi = tro.city()
    illnes = tro.illness()
    required = tro.required()
    amount_collected = tro.amount_collected()
    sum = tro.sum_plus()
    uniq = tro.uniq()
    for k in uniq:
        print(k[0])
        if k[3] in _const_sort_illness:
            my_dict_mrt = {}
            my_dict_mrt[k[0]] = k[1:11]
            print(my_dict_mrt)
            my_list_dict.append(my_dict_mrt)
    print(my_list_dict)
with open('sort_rusfond_data_dict', 'wb') as fp:
    olol = pickle.dump(my_list_dict, fp)