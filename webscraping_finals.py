from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font



webpage = 'https://registrar.web.baylor.edu/exams-grading/spring-2023-final-exam-schedule'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req= Request(url=webpage, headers=headers)

page = urlopen(req)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)

myclasses=['MW 1:00 p.m.','TR 2:00 p.m.']

table_rows= soup.findAll("tr")

for x in table_rows:
    final = x.findAll('td')
    if final:
        myclass = final[0].text
        date= final[1].text
        time= final[2].text
        if myclass in myclasses:
            print(f'For Class{myclass} the date is {date} and the time is {time}')
