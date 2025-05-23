import sys
sys.path.append(".")

from src.model.inverse_mortage import Person, Property
from src.model.exceptions import *
from src.model.property_value import property_value
from src.controller import personas_controller 
from src.controller import propiedades_controller

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/procesar", methods=["GET", "POST"])
def procesar():
    if request.method == "POST":
        try:
            nombre = request.form["nombre"]
            edad = int(request.form["edad"])
            genero = request.form["genero"].lower() in ["true", "1", "si", "sí"]
            discapacidad = request.form["discapacidad"].lower() in ["true", "1", "si", "sí"]
            titulo_propiedad = request.form["titulo_propiedad"].lower() in ["true", "1", "si", "sí"]
            estrato = int(request.form["estrato"])
            valor_comercial = float(request.form["valor_comercial"])
            antiguedad = int(request.form["antiguedad"])
            legalidad = request.form["legalidad"].lower() in ["true", "1", "si", "sí"]

            propiedad = Property(estrato, valor_comercial, antiguedad, legalidad, titulo_propiedad)
            persona = Person(nombre, edad, genero, discapacidad, titulo_propiedad, propiedad)

            propiedades_controller.insert_property(propiedad)
            personas_controller.insert_person(persona)
            mensaje = "Persona registrada exitosamente."
        except Exception as e:
            print(f"Error al procesar el formulario: {e}")
            mensaje = "Error al registrar la persona."

        return render_template("index.html", mensaje=mensaje)

    return render_template("index.html")





if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 8080)