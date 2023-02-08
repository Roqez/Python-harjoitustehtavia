
def etaisyyslaskuri(ICAO1,ICAO2):
    ekasql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident ='"+ICAO1+"';"
    kursori = yhteys.cursor()
    kursori.execute(ekasql)
    ekatkordinaatit = kursori.fetchall()
    tokasql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident ='" + ICAO2 + "';"
    kursori = yhteys.cursor()
    kursori.execute(tokasql)
    tokatkordinaatit = kursori.fetchall()
    etaisyys = (distance.distance(ekatkordinaatit,tokatkordinaatit).kilometers)
    return etaisyys

def main():
    print("Syötä kaksi eri ICAO koodia niin lasken kyseisten lentokenttien välisen etäisyyden")
    ICAO1 = input("Anna ensimmäinen ICAO koodi:")
    ICAO2 = input("Anna toinen ICAO koodi:")
    etaisyys = etaisyyslaskuri(ICAO1,ICAO2)

    print("Etäisyys näiden lentokenttien välillä on: "+str(etaisyys)+" kilometria")

import mysql.connector

from geopy import distance

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='juuri1234',
         autocommit=True
         )

main()