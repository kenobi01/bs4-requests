import requests
from bs4 import BeautifulSoup

url = "https://pypi.org/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

statistics = soup.find_all(class_="statistics-bar__statistic")

for statistic in statistics:
    print(statistic.text)
