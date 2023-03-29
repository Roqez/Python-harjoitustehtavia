import mysql.connector
from flask import Flask, Response
import json
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='juuri1234',
         autocommit=True
         )

app = Flask(__name__)
@app.route('/kenttä/<ICAO>')
def kenttä(ICAO):
    try:
        sql = "SELECT name, municipality FROM airport "
        sql += "WHERE ident='" + ICAO + "'"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        if kursori.rowcount > 0:
            tilakoodi = 200
            vastaus = {
            "ICAO": ICAO,
            "Name" : tulos[0][0],
            "Municipality" : tulos[0][1]
            }


    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen yhteenlaskettava"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)





