import requests
from bs4 import BeautifulSoup


indeed_python = requests.get(
    "https://www.indeed.com/jobs?as_and=python&limit=50")
indeed_soup = BeautifulSoup(indeed_python.text, 'html.parser')

pagination = indeed_soup.find("div", {"class": "pagination"})

links = pagination.find_all('a')
pages = []
for link in links[0:-1]:
    pages.append(int(link.string))

max_page = pages[-1]

# print(indeed_python.text)
# print(pagination)
# print(pages)
