"""
drop table on cascade placas;
create table placas (
	placa varchar(8) not null,
	estado varchar(2)
);

alter table placas add constraint placas_pk  primary key (placa,estado);

"""

import queplaca
#import psycopg2
import sqlite3 as lite
#conn = psycopg2.connect(user="postgres", password='abc123',host="localhost", database="queplaca")
conn = lite.connect("/Users/eduardo/Dev/queplaca/sql/queplaca.sql")
cur = conn.cursor()

q = queplaca.QuePlaca()
q = q.quePlaca

alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
cur.execute("create table placas( placa varchar(3) not null, uf varchar(2))")

for letra_0 in alfabeto:
	for letra_1 in alfabeto:
		for letra_2 in alfabeto:
			placa = "%s%s%s" % (letra_0,letra_1,letra_2)
			estado = q(placa)
			if estado == None or estado == False: estado = ""
			
			cur.execute("insert into placas values ('%s','%s');" % (placa,estado))
conn.commit()
			
