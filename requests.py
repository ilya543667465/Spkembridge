from bs4 import BeautifulSoup
import requests
import wget


url = 'http://spospk.ru/rasp.html'
response = requests.get(url)
print(response)

soup = BeautifulSoup(response.text, "html.parser")

allNews = []
filteredNews = []
c = 'Расписание занятий'

allNews = soup.findAll('div', class_='static-box')

for a in soup.findAll('a', target='_blank'):
    if a.text == c:
        url_rasp = a.get('href')
        print(url_rasp, a.text)

wget.download(url_rasp, 'Расписание спк.xlsx')
