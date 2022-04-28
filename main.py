from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
from pprint import pprint

HEADERS = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
url = 'https://zan.tambov.gov.ru'


column = ["Профессия", "Кол-во мест", "Зарплата", "Дата"]
data = []
# ====== Парсинг 2 страниц =======
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
        temp = [Profession, Required, salary, Date]
        data.append(temp)

df = pd.DataFrame(data, columns=column)
df.to_csv('Вакансии.csv', sep=';', encoding='1251')


