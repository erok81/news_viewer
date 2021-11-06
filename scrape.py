'''
function to scrap webpage for items with paragraph tags
'''

import requests
from bs4 import BeautifulSoup


def get_paragraphs(url):
    page = requests.get(url)
    if page.status_code == 200:

        soup = BeautifulSoup(page.content, "html.parser")
        paragraphs = soup.find_all('p')
    else:
        return 'error'


    return paragraphs

