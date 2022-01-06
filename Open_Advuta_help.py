import time
from urllib.parse import urlsplit, parse_qs, urlencode
start_time = time.time()

class Advita_prs_url:
    def __init__(self, root_adress):
        self.root_adress = root_adress
    def get_start_url(self):
        return self.root_adress
    def part_request(self):
        query = urlsplit(self.root_adress).query
        params = parse_qs(query)
        for key, val in params.items():
            if len(val) == 1:
                params[key] = val[0]
        return params
input_adress = Advita_prs_url('https://advita.ru/podopechnye/?PAGEN_2=1&SECTION_ID=28')
my_url = input_adress.get_start_url()
my_part_reqv = input_adress.part_request()

class Collection_of_all_links:
    def __init__(self,part_req):
        self.part_req = part_req
    def colect_links(self):
        B =[]
        for i in range(1, 35):
            self.part_req['PAGEN_2'] = i
            tro = urlsplit(my_url).scheme + '://' + urlsplit(my_url).netloc + urlsplit(my_url).path + '?' \
                  + urlencode(self.part_req)
            B.append(tro)
        return B

lo = Collection_of_all_links(my_part_reqv)
olol = lo.colect_links()##Cписок всех ссылок

