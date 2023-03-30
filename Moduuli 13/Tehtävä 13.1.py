from flask import Flask, Response
import json

app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    try:
        isprime = True
        luku = int(luku)
        if luku == 1:  # Koska ykkönen ei ole alkuluku
            isprime = False
        elif luku == 2:
            isprime = True
        elif luku > 1:
            for i in range(2,luku):  # Käy läpi onko luku jaollinen kahdella tai jollakin luvulla syötettyä lukua edeltävään lukuun saakka
                if (luku % i) == 0:
                    isprime = False
        tilakoodi = 200
        vastaus = {
        "number": luku,
        "isPrime": isprime,
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

