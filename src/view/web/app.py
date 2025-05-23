import sys
sys.path.append(".")

from src.model.inverse_mortage import Person, Property
from src.model.exceptions import *
from src.model.property_value import property_value

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/procesar", methods = ["GET", "POST"])
def procesar():
    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = request.form["edad"]
        genero = request.form["genero"]
        discapacidad = request.form["discapacidad"]
        titulo_propiedad = request.form["titulo_propiedad"]
        estrato = request.form["estrato"]
        valor_comercial = request.form["valor_comercial"]
        antiguedad = request.form["antiguedad"]
        legalidad = request.form["legalidad"]
        print(f"{nombre}, {edad}, {genero}, {discapacidad}, {titulo_propiedad}, {estrato}, {valor_comercial}, {antiguedad}, {legalidad}  ")
    return render_template("index.html")





if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 8080)