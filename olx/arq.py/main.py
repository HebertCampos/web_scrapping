from get_url_anuncios import *
from get_info_anuncios import *

url = "https://al.olx.com.br/alagoas/autos-e-pecas/motos"  
soup = conexaoSoup(url)
# for i in range(3):
#     time.sleep(5)
#     print(getHrefs(soup))
#     print(nextPage())
#     soup = conexaoSoup(nextPage())
# print(getHrefs(soup))