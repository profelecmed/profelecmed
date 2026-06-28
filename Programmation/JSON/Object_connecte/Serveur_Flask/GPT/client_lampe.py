import requests
import time

URL = "http://127.0.0.1:5000/etat"

etat = ""


while True:

    try:

        r = requests.get(URL)

        nouvel_etat = r.json()["bouton"]

        if nouvel_etat != etat:

            etat = nouvel_etat

            if etat == "ON":
                print("🟢 Lampe VERTE")
            else:
                print("🔴 Lampe ROUGE")

    except:
        print("Serveur indisponible")

    time.sleep(1)
