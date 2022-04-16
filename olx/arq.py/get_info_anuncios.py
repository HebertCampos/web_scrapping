from bs4 import BeautifulSoup


def getPreco(*soup):
    s = soup
    preco_html = s.select('.sc-1wimjbb-2')
    preco = [r.string.split() for r in preco_html]
    return preco[0][1]

def getTitulo(*soup):
    s = soup
    titulo_html = s.select('.sc-45jt43-0')
    titulo = [r.string for r in titulo_html]
    return titulo

def getDescricao(*soup):
    s = soup
    descricao_html = s.select('.sc-1sj3nln-1')
    descricao = [r.string for r in descricao_html]
    return descricao

def getDetalhes(*soup):
    s = soup
    list_detalhes_html = s.select('.sc-1f2ug0x-1')
    detalhes = [r.string for r in list_detalhes_html]
    return detalhes

def getAnunciante(*soup):
    s = soup
    anunciante_html = s.select('.sc-fBuWsC')
    anunciante = [r.string for r in anunciante_html]
    return anunciante

def anuncio(soup):
    anuncio = []
    anuncio = getDetalhes(soup)
    anuncio.append(getPreco(soup))
    anuncio.append(getTitulo(soup))
    anuncio.append(getDescricao(soup))
    
    return anuncio
    
    