from flask import Flask, jsonify, request

app = Flask(__name__)

etat_bouton = 1
valeur_analogique = 512
etat_led = False

@app.route("/etat", methods=["GET"])
def etat():
    return jsonify({
        "bouton": etat_bouton,
        "analogique": valeur_analogique
    })

@app.route("/led", methods=["POST"])
def led():
    global etat_led
    data = request.get_json()
    etat_led = data.get("led", False)
    return jsonify({
        "led": etat_led,
        "message": "LED mise à jour"
    })

@app.route("/commande", methods=["POST"])
def commande():
    data = request.get_json()
    marche = data.get("marche", False)
    frequence = data.get("frequence", 0)
    pourcentage = data.get("pourcentage", 0)

    if marche:
        message = "Sortie active"
    else:
        message = "Sortie inactive"

    return jsonify({
        "marche": marche,
        "frequence": frequence,
        "pourcentage": pourcentage,
        "message": message
    })

app.run(host="0.0.0.0", port=5000)
