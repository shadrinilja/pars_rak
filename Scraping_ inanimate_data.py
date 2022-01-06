import pickle
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import certifi
import time
start_time = time.time()

with open('list_ill_sort', 'rb') as fp:
    l = pickle.load(fp)
with open('list_death_all_url', 'rb') as fp:
    pepe = pickle.load(fp)

A = []
my_list_dict = []  ##список словарей
for all_url in pepe:
    try:
        sourse ='Advita'
        years_old = 'умер'
        drug = '------'
        collected_money = 'none'
        citi = '------'
        help_p = 'none'
        B = []
        open_url = urlopen(all_url, context=ssl.create_default_context(cafile=certifi.where()))
        soup = BeautifulSoup(open_url, 'html.parser')
        for name in soup.find(class_='wp-patient__name').find_all('h1'):
            B.append(sourse)
            B.append(name.text)
            B.append(years_old)
            B.append(citi)
            B.append(help_p)
            B.append(collected_money)
        for text_ullness in soup.find_all(class_ = 'element-detail__desc'):
            tro = text_ullness.text.replace('\n',' ')
            B.append(tro)
    except AttributeError:
        pass
    finally:
        my_dict_mrt = {}
        my_dict_mrt[B[0]] = B[1:11]
        print(my_dict_mrt)
        my_list_dict.append(my_dict_mrt)
    with open('Advita_dict_death_2', 'wb') as fp:
        pickle.dump(my_list_dict, fp)

