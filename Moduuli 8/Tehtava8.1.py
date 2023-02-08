import mysql.connector

def haekayttajansijainti(ICAO):
    sql = "SELECT name, municipality FROM airport "
    sql += "WHERE ident='" + ICAO + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentokentän nimi on {rivi[0]} ja kunta on {rivi[1]}")



yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='juuri1234',
         autocommit=True
         )


ICAO = input("Anna ICAO-koodi: ")
haekayttajansijainti(ICAO)

