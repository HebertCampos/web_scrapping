from pymysql import IntegrityError
from get_url_anuncios import *
from get_info_anuncios import *

import sqlite3

con = sqlite3.connect(r'/home/kr0ck/Documentos/SIAD/ws/olx/db/olx_motos_tt.db')

cur = con.cursor()


def getAnuncios():
    #url = "https://al.olx.com.br/alagoas/autos-e-pecas/motos" 
    url = "https://se.olx.com.br/sergipe/autos-e-pecas/motos"
    soup = conexaoSoup(url)
    a = []
    for j in range(100):
        hrefs = getHrefs(soup)
        for i in range(len(hrefs)):
            b = []
            soup1 = conexaoSoup(hrefs[i])
            b.append(anuncio(soup1, hrefs[i]))
            if(len(b[0])==12):
                a.append(b[0])
        soup = conexaoSoup(nextPage(soup))
        print(j)
    #print(a)
    return a

sql_insert = 'insert into anuncios (modelo,ano,km,cc,cep,municipio,bairro,preco,titulo_anuncio,descricao,url_anuncio,estado) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)'
recset = getAnuncios()
cur.executemany(sql_insert, recset)

con.commit()
con.close()
