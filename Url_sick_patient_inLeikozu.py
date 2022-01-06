from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import certifi
import pickle
with open('list_death_all_url', 'rb') as fp:
    pepe = pickle.load(fp)


class Pacienty_url:
    def __init__(self,insert_Address):
        self.insert_Address = insert_Address
    def get_insert_Address(self):
        return self.insert_Address
    def get_urlopen(self):
        open_url = urlopen('https://leikozu.net/help/vy-uzhe-pomogli/',
                           context=ssl.create_default_context(cafile=certifi.where()))
        return open_url
    def parse_HTML(self):
        soup = BeautifulSoup(self.get_urlopen(), 'html.parser')
        return soup
    def pacienty_URL(self):
        C = []
        for link in self.parse_HTML().find_all(class_='item-title'):##Достаем все ссылки
            z = [a['href'] for a in link.find_all('a')]
            C.extend(z)
        for i in range(0, 3):##Удаляем последние три ссылки
            C.pop()
        return C
cu = Pacienty_url('https://leikozu.net/help/vy-uzhe-pomogli/')
tro = cu.pacienty_URL()
print(tro)
class Pars_data_patient:
    def __init__(self,url_patient):
        self.__url_patient = url_patient
    def pars_data_leikoz(self):
        my_list_dict = []##список словарей
        for item in tro:
            try:
                sourse = 'Фонд борьбы с лейкимией'
                B = [] ## Общий список
                z = urlopen(item, context=ssl.create_default_context(cafile=certifi.where()))
                soup = BeautifulSoup(z, 'html.parser')
                for name in soup.find(class_='summary entry-summary').find_all('h1'):
                    B.append(sourse)
                    B.append(name.text)
                for years_old in soup.find(class_='summary entry-summary').find_all('p'):
                    new_years_old = years_old.text.split(',')
                    del new_years_old[2:]
                    B.extend(new_years_old)
                for drug in soup.find('ul', {'class': 'list-unstyled'}).find_all('li'):
                    a = drug.text.split(':')
                    del a[0]
                    B.extend(a) ##Список диагноз, и лечение каким препаратом
                for collected_money in soup.find('div', {'class': 'text-info foundation'}).find_all('strong'):
                    B.append(collected_money.get_text() + ' рублей')  ## Собрано денег
                for need_money in soup.find('div', {'class': 'text-right text-danger foundation'}).find_all('strong'):
                    B.append(need_money.get_text() + ' рублей') ##Нужно денег
            except AttributeError:
                B.append('Сумма собрана')
                B.insert(7, 'Сумма собрана')
            finally:
                my_dict_mrt = {}
                my_dict_mrt[B[0]] = B[1:11]
                print(my_dict_mrt)
                my_list_dict.append(my_dict_mrt)
        with open('leikoz_net_2', 'wb') as fp:
            pickle.dump(my_list_dict, fp)

lo = Pars_data_patient(tro)
pepe = lo.pars_data_leikoz()
print(pepe)