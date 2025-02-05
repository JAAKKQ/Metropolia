import mariadb

import os
from dotenv import load_dotenv
load_dotenv()



yhteys = mariadb.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user= os.getenv('DB_USER'),
         password=os.getenv('DB_PASSWD'),
         autocommit=True
         )

icao = input("Anna lentoaseman ICAO koodi: ")

sql = f"SELECT name, municipality FROM airport where ident like '{icao}';"

kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()

if kursori.rowcount >0 :
    for rivi in tulos:
        print(f"Lentokentän nimi on {rivi[0]} ja sen sijaintikunta on {rivi[1]}")