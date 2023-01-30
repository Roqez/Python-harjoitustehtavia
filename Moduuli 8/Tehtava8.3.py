import mysql.connector

from geopy import distance
#newport_ri = (41.49008, -71.312796)
#cleveland_oh = (41.499498, -81.695391)
#print(distance.distance(newport_ri, cleveland_oh).miles)

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='juuri1234',
         autocommit=True
         )

def etaisyyslaskuri(ICAO1,ICAO2):
    ekasql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident ='"+ICAO1+"';"
    print(ekasql)
    kursori = yhteys.cursor()
    kursori.execute(ekasql)
    ekatkordinaatit = kursori.fetchall()
    tokasql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident ='" + ICAO2 + "';"
    print(tokasql)
    kursori = yhteys.cursor()
    kursori.execute(tokasql)
    tokatkordinaatit = kursori.fetchall()
    etaisyys = (distance.distance(ekatkordinaatit,tokatkordinaatit).kilometers)
    return etaisyys

def main():
    print("Syötä kaksi eri ICAO koodia niin lasken kyseisten lentokenttien välisen etäisyyden")
    ICAO1 = input("Anna ICAO koodi:")
    ICAO2 = input("Anna ICAO koodi:")
    etaisyys = etaisyyslaskuri(ICAO1,ICAO2)

    print("Etäisyys näiden lentokenttien välillä on: "+str(etaisyys)+" kilometria")

main()