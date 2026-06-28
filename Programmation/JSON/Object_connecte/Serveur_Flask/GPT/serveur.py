from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Etat partagé
etat = {
    "bouton": "OFF"
}


@app.route("/")
def accueil():
    return render_template("index.html")


@app.route("/etat", methods=["GET"])
def get_etat():
    return jsonify(etat)


@app.route("/etat", methods=["POST"])
def set_etat():
    global etat

    data = request.get_json()

    if "bouton" in data:
        etat["bouton"] = data["bouton"]

    return jsonify(etat)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
