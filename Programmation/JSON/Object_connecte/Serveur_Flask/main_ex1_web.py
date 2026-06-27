from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

# État global du système (partagé entre Web et API)
etat = {
    "bouton": 0,
    "analogique": 512,
    "led": False
}

# Interface HTML (Vue utilisateur)
html_page = """
<!DOCTYPE html>
<html>
<head>
    <style>
        .etat-led { font-weight: bold; color: {{ 'green' if led_status else 'red' }}; }
    </style>
</head>
<body>
    <h1>Tableau de bord IoT</h1>
    
    <h3>1. Contrôle du bouton (Entrée)</h3>
    <form action="/set_bouton" method="post">
        <button name="etat" value="0">Bouton 0</button>
        <button name="etat" value="1">Bouton 1</button>
    </form>

    <h3>2. Contrôle de la LED (Sortie)</h3>
    <form action="/set_led" method="post">
        <button name="led" value="on">Allumer LED</button>
        <button name="led" value="off">Éteindre LED</button>
    </form>
    
    <p>État actuel de la LED : <span class="etat-led">{{ "ALLUMÉE" if led_status else "ÉTEINTE" }}</span></p>
    
    <hr>
    <a href="/">Actualiser la page</a>
</body>
</html>
"""

# --- ROUTES ---

@app.route("/", methods=["GET"])
def index():
    """Affiche l'interface utilisateur web."""
    return render_template_string(html_page, led_status=etat["led"])

@app.route("/etat", methods=["GET"])
def get_etat():
    """API JSON pour les clients (scripts Python)."""
    return jsonify(etat)

@app.route("/set_bouton", methods=["POST"])
def set_bouton():
    """Mise à jour du bouton via le formulaire Web."""
    etat["bouton"] = int(request.form.get("etat"))
    return "Bouton mis à jour. <br><a href='/'>Retour</a>"

@app.route("/set_led", methods=["POST"])
def set_led():
    """Mise à jour de la LED via le formulaire Web ou API JSON."""
    # Supporte aussi bien le formulaire web que le JSON
    if request.is_json:
        data = request.get_json()
        etat["led"] = data.get("led", False)
    else:
        commande = request.form.get("led")
        etat["led"] = True if commande == "on" else False
    return "LED mise à jour. <br><a href='/'>Retour</a>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
