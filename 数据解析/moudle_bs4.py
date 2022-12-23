import requests
from bs4 import BeautifulSoup

page = BeautifulSoup(html, "html.parser")

page.find()
page.find_all("div_name", attrs={"class": "class_name"})
