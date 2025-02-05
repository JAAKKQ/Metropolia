import mariadb
from geopy import distance
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

def sql(kysely):
    kursori = yhteys.cursor()
    kursori.execute(kysely)
    tulos = kursori.fetchall()
    if kursori.rowcount>0 :
        for rivi in tulos:
            return rivi

input1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
input2 = input("Anna toisen lentokentän ICAO-koodi: ")

kysely1 = sql(f"SELECT latitude_deg, longitude_deg FROM airport where ident like '{input1}';")
kysely2 = sql(f"SELECT latitude_deg, longitude_deg FROM airport where ident like '{input2}';")

print("Lenttokenttien etäisyys toisistaan on ", round(distance.distance(f"{kysely1[0]}, {kysely1[1]}", f"{kysely2[0]}, {kysely2[1]}").kilometers), "kilometriä.")

