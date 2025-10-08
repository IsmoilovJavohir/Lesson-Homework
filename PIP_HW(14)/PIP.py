from os.path import split

import requests
from bs4 import BeautifulSoup

sahifa = "https://www.w3schools.com/python/python_pip.asp"
r = requests.get(sahifa)

soup = BeautifulSoup(r.text,'html.parser')
news = soup.find_all(class_="w3-example")
print(news[0].text)



# №2    \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



link= "https://www.computerhistory.org/tdih/September/09/?utm_source=chatgpt.com"
box = requests.get(link)

quti = BeautifulSoup(box.text,'html.parser')
matin = quti.find_all(class_="chm-tdih-entry-content")

matn= matin[0].text

jumlalar =matn.split('.') #split()- matini ajratib beradi agar beligi(.) yoki bosh joy bersak shunga qarab ajratib beradi

for jumla in jumlalar:
    if jumla.strip():     #strip()- matindagi bosh() joyni yoki berilgan belgini olib tashlash uchun
        print(jumla.strip()+'.')