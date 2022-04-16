from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
import time
from get_info_anuncios import *


def conexaoSoup(url):
    url = url
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
    try:
        req = Request(url, headers= headers)
        response = urlopen(req)
        html = response.read()
    except HTTPError as e:
        print(e.status, e.reason)
    except URLerror as e:
        print(e.reason)
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def getHrefs(soup):
    soup = soup
    links_anuncios = []
    for a_href in soup.findAll(class_="kQcyga", href=True):
        links_anuncios.append(a_href['href'])
    return links_anuncios

def nextPage(soup):
    soup = soup
    new_page = []
    for a_href in soup.findAll(class_="lfGTeV", href=True):
        new_page.append(a_href['href'])
    return new_page[0]

def infoAnuncio(soup):
    soup = soup
    getPreco(soup)
    getTitulo(soup)
    getDescricao(soup)
    getDetalhes(soup)
    
def info():
    info = []
    info.append(getPreco())
    info.append(getTitulo())
    info.append(getDescricao())
    detalhes =getDetalhes()
    for i in detalhes:
        info.append(detalhes[i])