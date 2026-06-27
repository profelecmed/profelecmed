from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def form():
  return "<p>Bonjour les CIEL le serveur Flask fonctionne parfaitement</p>"

app.run(debug=True)
