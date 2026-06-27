from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

etat = {"interrupteur": "OFF", "lampe": "Eteinte"}

# Page avec le script AJAX intégré
html_template = """
<!DOCTYPE html>
<html>
<body>
    <h1>Tableau de bord AJAX</h1>
    <p>Interrupteur : <strong id="val-int">...</strong></p>
    <p>Lampe : <strong id="val-lampe">...</strong></p>
    
    <button onclick="changerEtat('ON')">ON</button>
    <button onclick="changerEtat('OFF')">OFF</button>

    <script>
        function changerEtat(cmd) {
            fetch('/update', {
                method: 'POST',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                body: 'cmd=' + cmd
            }).then(() => actualiser());
        }

        function actualiser() {
            fetch('/api').then(r => r.json()).then(data => {
                document.getElementById('val-int').innerText = data.interrupteur;
                document.getElementById('val-lampe').innerText = data.lampe;
            });
        }
        setInterval(actualiser, 1000); // Actualise automatiquement toutes les secondes
    </script>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(html_template)

@app.route("/update", methods=["POST"])
def update():
    cmd = request.form.get("cmd")
    etat["interrupteur"] = cmd
    etat["lampe"] = "Allumée" if cmd == "ON" else "Eteinte"
    return "OK"

@app.route("/api", methods=["GET"])
def api():
    return jsonify(etat)

app.run(host="0.0.0.0", port=5000)
