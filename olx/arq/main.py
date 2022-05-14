from get_url_anuncios import *
from get_info_anuncios import *

import sqlite3

con = sqlite3.connect(r'ws/olx/db/olx_motos.db')

cur = con.cursor()


def getAnuncios():
    # url = "https://al.olx.com.br/alagoas/autos-e-pecas/motos" 
    url = "https://se.olx.com.br/sergipe/autos-e-pecas/motos"
    soup = conexaoSoup(url)
    a = []
    for j in range(1):
        hrefs = getHrefs(soup)
        for i in range(len(hrefs)):
            b = []
            soup1 = conexaoSoup(hrefs[i])
            b.append(anuncio(soup1, hrefs[i]))
            if(len(b[0])==12):
                a.append(b[0])
        soup = conexaoSoup(nextPage(soup))
        print(j)
    return a

sql_insert = 'insert into anuncios values (?,?,?,?,?,?,?,?,?,?,?,?)'
recset = getAnuncios()
for rec in recset:
    cur.execute(sql_insert, rec)
con.commit()
con.close()
