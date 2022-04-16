from get_url_anuncios import *
from get_info_anuncios import *

url = "https://al.olx.com.br/alagoas/autos-e-pecas/motos" 

soup = conexaoSoup(url)
a = []
for i in range(60):
    hrefs = getHrefs(soup)
    for i in range(len(hrefs)):
        soup1 = conexaoSoup(hrefs[i])
        a.append(anuncio(soup1, hrefs[i]))
    soup = conexaoSoup(nextPage(soup))