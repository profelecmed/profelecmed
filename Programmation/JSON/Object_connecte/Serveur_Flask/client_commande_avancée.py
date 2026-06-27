import requests

url = "http://192.168.1.10:5000/commande"

commande = {
    "marche": True,
    "frequence": 1000,
    "pourcentage": 50
}

try:
    reponse = requests.post(url, json=commande, timeout=5)
    print(reponse.json())
except Exception as e:
    print("Erreur :", e)
