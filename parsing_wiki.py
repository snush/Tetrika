import requests
from bs4 import BeautifulSoup

url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
page = requests.get(url).text

animals = {
    'А': 0,
    'Б': 0,
    'В': 0,
    'Г': 0,
    'Д': 0,
    'Е': 0,
    'Ё': 0,
    'Ж': 0,
    'З': 0,
    'И': 0,
    'Й': 0,
    'К': 0,
    'Л': 0,
    'М': 0,
    'Н': 0,
    'О': 0,
    'П': 0,
    'Р': 0,
    'С': 0,
    'Т': 0,
    'У': 0,
    'Ф': 0,
    'Х': 0,
    'Ц': 0,
    'Ч': 0,
    'Ш': 0,
    'Щ': 0,
    'Э': 0,
    'Ю': 0,
    'Я': 0,
    'A': 0
}


while animals['A'] == 0:
    soup = BeautifulSoup(page, "html.parser")
    links = soup.find('div', id='mw-pages').find_all('a')
    for a in links:
        if a.text == 'Следующая страница':
            url = 'https://ru.wikipedia.org/' + a.get('href')
            page = requests.get(url).text
        elif a.text != 'Предыдущая страница' and a.text[0] in animals.keys():
            animals[a.text[0]] = animals[a.text[0]] + 1

del animals['A']
for key, value in animals.items():
  print(f'{key}: {value}')


answer = {
    'А': 1146,
    'Б': 1599,
    'В': 515,
    'Г': 984,
    'Д': 739,
    'Е': 99,
    'Ё': 2,
    'Ж': 392,
    'З': 619,
    'И': 337,
    'Й': 3,
    'К': 2184,
    'Л': 679,
    'М': 1240,
    'Н': 451,
    'О': 766,
    'П': 1730,
    'Р': 555,
    'С': 1737,
    'Т': 968,
    'У': 242,
    'Ф': 189,
    'Х': 270,
    'Ц': 218,
    'Ч': 658,
    'Ш': 267,
    'Щ': 146,
    'Э': 213,
    'Ю': 133,
    'Я': 209
}
