from get_url_anuncios import *
from get_info_anuncios import *

url = "https://al.olx.com.br/alagoas/autos-e-pecas/motos" 
# url = "https://al.olx.com.br/alagoas/autos-e-pecas/motos/honda-pop-110i-2016-2017-1020765768"
soup = conexaoSoup(url)
# for i in range(3):
#     print(getHrefs(soup))
#     print(nextPage(soup))
#     soup = conexaoSoup(nextPage(soup))

# print(getDetalhes(soup))

a = []
for i in range(60):
    hrefs = getHrefs(soup)
    for i in range(len(hrefs)):
        soup1 = conexaoSoup(hrefs[i])
        a.append(anuncio(soup1, hrefs[i]))
        
    soup = conexaoSoup(nextPage(soup))
    print(len(a))
print(f'paginas finais: {len(a)}')