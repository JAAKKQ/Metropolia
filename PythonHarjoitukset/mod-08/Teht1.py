import mariadb

import os
from dotenv import load_dotenv
load_dotenv()



yhteys = mariadb.connect(
         host='127.0.0.1',
         port= 3306,
         database='ankkalinna',
         user= os.getenv('DB_USER'),
         password=os.getenv('DB_PASSWD'),
         autocommit=True
         )

icao = input("Anna lentoaseman ICAO koodi: ")

sql = f"SELECT iata_code FROM airport;"

kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()

print(tulos)