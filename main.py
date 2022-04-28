import pandas as pd
from bs4 import BeautifulSoup
import requests
import json
from pprint import pprint
from time import sleep

HEADERS = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

url = 'https://zan.tambov.gov.ru'


# ===== Кол-во работодателей и страниц =====
def CountPage(path):
    response = requests.get(path, headers=HEADERS).text
    soup = BeautifulSoup(response, 'lxml')
    stroka = soup.find(class_='k-header k-grid-toolbar k-grid-top').find('label')
    s1 = list(stroka)
    s2 = []
    s1.pop(1)
    for i in s1:
        s2.append(i.strip())
    Text = ' '.join(s2)
    s1 = Text.split(' ')
    count_page = []
    for i in s1:
        if i.isdigit():
            count_page.append((int(i)))
    return count_page


# ===== Выцепляем названия столбцов =====
def CreateColumns(path):
    response = requests.get(path, headers=HEADERS).text
    soup = BeautifulSoup(response, 'lxml')
    Columns = soup.find('table').find('thead').find_all('th')

    column = []
    for i in Columns:
        s = i['data-title']
        if '<br/>' in i['data-title']:
            s = s.replace('<br/>', ' ')
            column.append(s)
        else:
            column.append(s)
    return column


# ===== Выцепляем данные столбцов
def CreateData(path):
    data = []
    response = requests.get(path, headers=HEADERS).text
    soup = BeautifulSoup(response, 'lxml')
    body = soup.find('table').find('tbody').find_all('tr')
    for i in body:
        temp = []
        for n in i:
            temp.append(n.text.strip())
        data.append(temp)
    return data
# path_1 = f'https://zan.tambov.gov.ru/employer/index?Grid-sort=&Grid-page=1&Grid-pageSize=10&Grid-group=&Grid-filter='
# count_page = CountPage(path_1)
# column = CreateColumns(path_1)
# data = []

# for p in range(count_page[1]+1):
for p in range(89):
    path = f'https://zan.tambov.gov.ru/employer/index?Grid-sort=&Grid-page={p}&Grid-pageSize=10&Grid-group=&Grid-filter='

    response = requests.get(path, headers=HEADERS).text
    with open(f'PAGES/Page_{p}.html', 'w', encoding='utf8') as file:
        file.write(response)
    print(f"Страница: {p+1}")
    sleep(1)




#     data.append(CreateData(path))
#
# pprint(data)
# # df = pd.DataFrame(data, columns=column)
# # df.to_csv('Организации.csv', sep=';', encoding='1251')
