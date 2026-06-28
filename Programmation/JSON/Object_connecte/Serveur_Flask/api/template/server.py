from flask import (
        Flask,
        render_template 
)
 
# Creation de l'instance de l'application
app = Flask(__name__, template_folder="templates")
 
# Création d'une URL pour "/"
@app.route('/')
def home():
        return render_template('home.html')
