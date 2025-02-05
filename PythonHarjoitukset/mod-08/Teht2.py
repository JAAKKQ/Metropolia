import mariadb
import os
from dotenv import load_dotenv
load_dotenv()



yhteys = mariadb.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user=os.getenv('DB_USER'),
         password=os.getenv('DB_PASSWD'),
         autocommit=True
         )

input = input("Anna maakoodi: ")

sql = f"SELECT type FROM airport where iso_country like '{input}';"

kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()

kentat = []

if kursori.rowcount >0 :
    for rivi in tulos:
        kentat.append(rivi[0])

kentta_tyypit = {}

for kentta in kentat:
    if kentta in kentta_tyypit.keys():
        kentta_tyypit[kentta]+=1
    else:
        kentta_tyypit[kentta]=1

for nimi, lukumaara in kentta_tyypit.items():
    print(nimi, lukumaara)

