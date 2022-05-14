import sqlite3

con = sqlite3.connect(r'ws/olx/db/olx_motos.db')

cur = con.cursor()

def create_anuncios():
  sql_crate = '''
  CREATE TABLE anuncios (
    modelo VARCHAR(45) NULL,
    ano VARCHAR(45) NULL,
    km VARCHAR(45) NULL,
    cc VARCHAR(45) NULL,
    cep VARCHAR(45) NULL,
    municipio VARCHAR(45) NULL,
    bairro VARCHAR(45) NULL,
    preco VARCHAR(45) NULL,
    titulo_anuncio VARCHAR(45) NULL,
    descrição VARCHAR(45) NULL,
    url_anuncio VARCHAR(145) NOT NULL,
    estado VARCHAR(45) NULL,
    PRIMARY KEY (url_anuncio))
  '''
  cur.execute(sql_crate)

def select():
  cur.execute('select * from anuncios')
  rows = cur.fetchall()
  for row in rows:
    print(row)

create_anuncios()


