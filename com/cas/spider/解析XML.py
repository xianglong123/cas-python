import requests  # 导入requests包
from bs4 import BeautifulSoup

url = 'http://www.cntour.cn/'
strhtml = requests.get(url)
soup = BeautifulSoup(strhtml.text, 'lxml')
data = soup.findAll('a')

for item in data:
    print(item)
