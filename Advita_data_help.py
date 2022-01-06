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

with open('sort_need_help_nou_url_list', 'rb') as fp:
    l = pickle.load(fp)

my_list_dict = []  ##список словарей
for item in l:
    try:
        HP = 'нужна помощь'
        sourse = 'Advita'
        B = [] ## Общий список
        driver.get(item)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        for name in soup.find(class_='wp-patient__name').find_all('h1'):
            B.append(sourse)
            B.append(name.text)
        for years_old in soup.find_all(id='patient__property_age', class_='patient__property'):
            new_y = years_old.text.replace(',','')
            B.append(new_y)
        for citi in soup.find_all(class_='patient__property'):
            B.append(citi.get_text())
        new_list = [j for i, j in enumerate(B) if i not in [3, 5, 6]]
        diagnos = new_list[4].split(':')
        required = new_list[5].split(':')
        del diagnos[0]
        del required[0]
        new_diagnos = diagnos
        new_required = required
        makeitastring = ''.join(map(str, new_diagnos))
        makeitastring_2 = ''.join(map(str, new_required))
        new_list[4] = makeitastring
        new_list[5] = makeitastring_2
        new_list.append(HP)
        new_list.append(HP)
    except IndexError:
        diagnos = new_list[4].split(':')
        del diagnos[0]
        new_diagnos = diagnos
        makeitastring = ''.join(map(str, new_diagnos))
        new_list[4] = makeitastring
        new_list.append('Здоров')
        new_list.append('сумма собрана')
        new_list.append('сумма собрана')
    finally:
        my_dict_mrt = {}
        my_dict_mrt[new_list[0]] = new_list[1:11]
        print(my_dict_mrt)
        my_list_dict.append(my_dict_mrt)
    with open('Advita_need_helped_data_dict', 'wb') as fp:
        pickle.dump(my_list_dict, fp)
print('1:'+str(start_time-time.time()))