import requests
import spacy
import pandas as pd
from bs4 import BeautifulSoup

nlp = spacy.load("en_core_web_sm")

urls = [
    'https://cryptodaily.co.uk/tag/business'.format(i) for i in range(179)]
hrefs = []


def get_hrefs(page):
    iteration = 1

    page = requests.get(page)
    soup = BeautifulSoup(page.text, "html5lib")
    container = soup.find_all('div', {'class': "post-item-content"})
    container_a = container[0].find_all('a')
    links = [container_a[i].get('href') for i in range(len(container_a))]
    for link in links:
        if link[0]:
            hrefs.append(link)

    for url in urls:
        if url == int:
            get_hrefs(url)
        else:
            iteration += 1


get_hrefs(urls[0])
print(hrefs)
'''
def extract_data():
    rep = []
    url = 'https://cryptodaily.co.uk/tag/business'
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, "html5lib")
    text = soup.get_text()
    gutten_nlp = nlp(text[:99999])

    for token in gutten_nlp.ents:
        print(token, token.label_, token.label)

    for token in gutten_nlp.sents:
        print(token)


extract_data()
'''
