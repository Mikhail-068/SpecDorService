from bs4 import BeautifulSoup
import requests
import json
from pprint import pprint

HEADERS = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
p = 1
url = 'https://zan.tambov.gov.ru'

path = f'https://zan.tambov.gov.ru/Employer/EmployerVacancy/?EmployerId=470df58e-ee6b-11e8-adb0-000c2973da2c&Sort=1\
        &take=10&skip=0&page={p}&pageSize=10'

# path2 = input('Введите адрес ссылки:\n')


response = requests.get(path, headers=HEADERS)


Json = json.loads(response.text)

pprint(Json)
