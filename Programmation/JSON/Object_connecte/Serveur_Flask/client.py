import requests
import time

url = "http://192.168.1.10:5000/etat"

while True:
    try:
        reponse = requests.get(url, timeout=5)
        data = reponse.json()
        print("Bouton :", data["bouton"])
        print("Analogique :", data["analogique"])
        print("-" * 20)
    except Exception as e:
        print("Erreur :", e)

    time.sleep(2)
