import mysql.connector

def haekentat(maakoodi):
    sql = "SELECT TYPE, COUNT(iso_country) FROM airport WHERE iso_country ='"+maakoodi+ "' GROUP BY TYPE;"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentokentän tyyppi on {rivi[0]} ja niiden lukumäärä on {rivi[1]}")

def main():
    maakoodi = input("Anna maakoodi: ")
    haekentat(maakoodi)



yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port= 3306,
        database='flight_game',
        user='root',
        password='juuri1234',
        autocommit=True
         )
main()

