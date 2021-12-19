import requests
from bs4 import BeautifulSoup as bs

user = input('Input User: ')
url = 'https://github.com/'+user
req = requests.get(url)
soup = bs(req.content, 'html.parser')
html_output = soup.find('img', {'alt': 'Avatar'})['src']
print(html_output)
