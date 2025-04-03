from flask import Flask, jsonify
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

app = Flask(__name__)

def alkuluku(luku):
    on_alku_luku = True

    for jakaja in range(2, luku):
        if luku % jakaja == 0:
            on_alku_luku = False

    return on_alku_luku

@app.route('/kenttä/<icao>', methods=['GET'])
def tarkista(icao):
    sql = f"SELECT name, municipality FROM airport where ident like '{icao}';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()[0]

    return jsonify({
        "ICAO": icao,
        "Name": tulos[0],
        "Municipality": tulos[1],
    })

app.run(debug=True, port=3000)