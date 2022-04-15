from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

def url():
    url = "https://al.olx.com.br/alagoas/autos-e-pecas/motos"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
    url_headers = [url,headers]
    return url_headers

def conexaoSoup():
    urL = url()
    try:
        req = Request(urL[0], headers= urL[1])
        response = urlopen(req)
        html = response.read()
    except HTTPError as e:
        print(e.status, e.reason)
    except URLerror as e:
        print(e.reason)
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def getHrefs():
    links_anuncios = []
    for a_href in soup.findAll(class_="kQcyga", href=True):
        links_anuncios.append(a_href['href'])
    return links_anuncios

def nextPage():
    new_page = []
    for a_href in soup.findAll(class_="lfGTeV", href=True):
        new_page.append(a_href['href'])
    return new_page
    
soup = conexaoSoup()
    