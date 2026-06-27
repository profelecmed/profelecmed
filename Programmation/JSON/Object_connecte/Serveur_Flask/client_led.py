import requests
import time

url = "http://192.168.1.10:5000/led"

try:
    requests.post(url, json={"led": True}, timeout=5)
    print("DEL allumée")
    time.sleep(5)
    requests.post(url, json={"led": False}, timeout=5)
    print("DEL éteinte")
except Exception as e:
    print("Erreur :", e)
