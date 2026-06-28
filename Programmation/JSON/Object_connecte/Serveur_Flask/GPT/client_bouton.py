import requests
import threading
import time

URL = "http://127.0.0.1:5000/etat"

etat_local = "OFF"


def lecture():
    global etat_local

    while True:

        try:
            r = requests.get(URL)

            etat = r.json()["bouton"]

            if etat != etat_local:
                etat_local = etat
                print("\nEtat synchronisé :", etat_local)

        except:
            pass

        time.sleep(2)


threading.Thread(target=lecture, daemon=True).start()


while True:

    print("\nEtat actuel :", etat_local)

    input("Entrée pour changer d'état")

    if etat_local == "OFF":
        etat_local = "ON"
    else:
        etat_local = "OFF"

    requests.post(URL, json={"bouton": etat_local})
