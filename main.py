from bs4 import BeautifulSoup
import requests
import json
from pprint import pprint

HEADERS = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
url = 'https://zan.tambov.gov.ru'


# ========= Проходимся по 2 страницам =============
for p in range(1,3):

    path = f'https://zan.tambov.gov.ru/Employer/EmployerVacancy/?EmployerId=470df58e-ee6b-11e8-adb0-000c2973da2c&Sort=1\
            &take=10&skip=0&page={p}&pageSize=10'
    response = requests.get(path, headers=HEADERS)
    Js = json.loads(response.text)
    Data_list = Js['Data']


    for i in range(len(Data_list)):
        Profession = Data_list[i]['Profession']
        Required = Data_list[i]['Required']
        salary = BeautifulSoup(Data_list[i]['FromTo'], 'lxml').text
        Date = Data_list[i]['Date']

# ========= Записываем данные в текстовый файл ===========

        with open(f'Вакансии/Вакансии Спецдорсервиса на {Date}.txt', 'a', encoding='utf8') as f:
            f.write(f"Профессия: {Profession}\nКол-во мест: {Required}\nЗарплата: {salary}\n\n")


