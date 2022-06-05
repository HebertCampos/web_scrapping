import sqlite3

con = sqlite3.connect(r'ws/olx/db/olx_motos_tt.db')

cur = con.cursor()


def create_anuncios():
    sql_crate = '''
  CREATE TABLE anuncios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    modelo VARCHAR(45) NULL,
    ano VARCHAR(45) NULL,
    km VARCHAR(45) NULL,
    cc VARCHAR(45) NULL,
    cep VARCHAR(45) NULL,
    municipio VARCHAR(45) NULL,
    bairro VARCHAR(45) NULL,
    preco VARCHAR(45) NULL,
    titulo_anuncio VARCHAR(45) NULL,
    descricao VARCHAR(45) NULL,
    url_anuncio VARCHAR(145) NOT NULL,
    estado VARCHAR(45) NULL)
  '''
    cur.execute(sql_crate)


def select():
    cur.execute('select * from anuncios')
    rows = cur.fetchall()
    for row in rows:
        print(row)


def insert_anuncios():
    a = [['HONDA POP 110I', '2020', '19000', '100', '57072000', 'Maceió', 'Cidade Universitária', '8.899', 'Pop 110i 2020', 'Moto sem problemas', 'https://al.olx.com.br/alagoas/autos-e-pecas/motos/pop-110i-2020-1032199508', 'AL'], ['HONDA NXR 160 BROS ESDD FLEXONE', '2018', '0', '150', '57061410', 'Maceió', 'Tabuleiro do Martins', '15.000', 'Bros 160 2018 abaixo da fip otima Oportunidade! ', None, 'https://al.olx.com.br/alagoas/autos-e-pecas/motos/bros-160-2018-abaixo-da-fip-otima-oportunidade-1032197760', 'AL'], ['KAWASAKI Z 1000', '2017', '27300', '1000', '57020210', 'Maceió', 'Centro', '59.500', 'Kawasaki Z1000- 2017', None, 'https://al.olx.com.br/alagoas/autos-e-pecas/motos/kawasaki-z1000-2017-1002902797', 'AL'], ['KAWASAKI Z 1000', '2022', '0', '1000', '57020210', 'Maceió', 'Centro', '73.990', 'Kawasaki Z1000- 2022 **Lançamento**', None, 'https://al.olx.com.br/alagoas/autos-e-pecas/motos/kawasaki-z1000-2022-lancamento-959980046', 'AL'], ['TRIUMPH TIGER 800 XCA', '2020', '23794', '800', '57020210', 'Maceió', 'Centro', '63.900', 'Triumph - Tiger 800 XCA- 2020', None, 'https://al.olx.com.br/alagoas/autos-e-pecas/motos/triumph-tiger-800-xca-2020-998347894', 'AL'], ['SUZUKI GSX-S 750', '2007', '160588', '750', '57084700', 'Maceió', 'Benedito Bentes', '8.500', 'Vendo ou troca uma 750 Suzuki ', 'Vendo ou troco em carro ou outra moto obs. Moto está com moto aberto pra fazer está com emplacamento atrasado tem Recibo e porte já na minha mão só fale se estiver interesse não venha com perguntas bestas passo cartão e dividir em até 10 vezes com o juros pô  conta do comprador qualquer coisa fala no chat que mando mais fotos ',                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 'https://al.olx.com.br/alagoas/autos-e-pecas/motos/vendo-ou-troca-uma-750-suzuki-1032180634', 'AL'], ['HONDA XRE', '2011', '0', '300', '57062043', 'Maceió', 'Petrópolis', '11.500', 'Xre 2011', 'Moto revisada recentemente.\nPronta pra transferir\nJá Emplacada até 2023', 'https://al.olx.com.br/alagoas/autos-e-pecas/motos/xre-2011-1032180311', 'AL'], ['HONDA NXR 160 BROS ESDD FLEXONE', '2019', '30000', '160', '57040600', 'Maceió', 'Jacintinho', '16.900', 'honda nxr bros 160 2019', None, 'https://al.olx.com.br/alagoas/autos-e-pecas/motos/honda-nxr-bros-160-2019-868872961', 'AL'], ['HONDA ELITE 125', '2021', '900', '125', '57025891', 'Maceió', 'Poço', '12.500', 'Honda Elite 125', None, 'https://al.olx.com.br/alagoas/autos-e-pecas/motos/honda-elite-125-1032151607', 'AL'], ['HONDA POP 110I', '2019', '37000', '125', '57052827', 'Maceió', 'Gruta de Lourdes', '9.100', 'POP 110', 'Vendo pop 110 ano 2019\n* único dono \n* 37 mil rodados\n* pneu traseiro novo\n* revisão em dia \n\nTroco por uma Bross e cubro a diferença ', 'https://al.olx.com.br/alagoas/autos-e-pecas/motos/pop-110-1032145318', 'AL'], ['KAWASAKI Z 650', '2013', '25400', '650', '57035060', 'Maceió', 'Ponta Verde', '44.000', 'Zx6r 13/13', 'Zx6r 13/13, dois pneus zero, moto extremamente conservada, revisada, tenho escapamento original, manual, cópia de chave, ipva 2022 pago. Com apenas 25.400km rodada. Golpistas não percam seu tempo, conheço o golpe. ', 'https://al.olx.com.br/alagoas/autos-e-pecas/motos/zx6r-13-13-1019978969', 'AL'], ['SUZUKI AN 125 BURGMAN', '2011', '60000', '125', '57052350', 'Maceió', 'Pitanguinha', '4.500', 'Suzuki 125 2011', None, 'https://al.olx.com.br/alagoas/autos-e-pecas/motos/suzuki-125-2011-1032137771', 'AL']]
    sql_insert = 'insert into anuncios (modelo,ano,km,cc,cep,municipio,bairro,preco,titulo_anuncio,descricao,url_anuncio,estado) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)'
    cur.executemany(sql_insert, a)

    # for rec in a:
    #     cur.execute(sql_insert, rec)
    con.commit()
    
    
def creat_test():
  sql = '''
    CREATE TABLE "test" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"nome"	TEXT,
	"idade"	INTEGER,
	"cidade"	TEXT,
	"salario"	REAL
);
  '''
  cur.execute(sql)
  
  
def insert_test():
  a = [['Paul', 32, 'California', 20000.00],['Paul', 32, 'California', 20000.00]]
  sql_insert = "INSERT INTO test (nome, idade,cidade,salario) VALUES (?,?,?,?)"
  cur.executemany(sql_insert, a)
  # for i, rec in enumerate(a):
  #   rec.append(i)
  #   cur.execute(sql_insert, rec)
  con.commit()

create_anuncios()
# select()
# insert_anuncios()
# creat_test()
# insert_test()
