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
    return render_template("principal.html")

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

@app.route("/buscar", methods=["GET", "POST"])
def buscar():
    propiedades = []
    if request.method == "POST":
        nombre = request.form["nombre"]
        propiedades = propiedades_controller.buscar_propiedades_por_nombre(nombre)
        return render_template("buscar.html", propiedades=propiedades)
    return render_template("buscar.html", propiedades=[])

from flask import redirect, url_for

@app.route("/eliminar/<int:propiedad_id>", methods=["POST"])
def eliminar_propiedad(propiedad_id):
    try:
        propiedades_controller.delete_property(propiedad_id)
        return redirect(url_for("buscar"))
    except Exception as e:
        mensaje = f"Error al eliminar la propiedad: {e}."
        return render_template("buscar.html", propiedades=[], mensaje=mensaje)

@app.route("/editar/<int:propiedad_id>", methods=["GET", "POST"])
def editar_propiedad(propiedad_id):
    # Usar la función select_property_properties para obtener la propiedad
    propiedad_data = propiedades_controller.select_property_properties(propiedad_id)
    if not propiedad_data:
        mensaje = "Propiedad no encontrada."
        return render_template("editar.html", propiedad=None, mensaje=mensaje)

    # Si select_property_properties imprime y no retorna, deberías modificarla para retornar los datos
    propiedad = propiedad_data  # Ajusta esto según el formato retornado

    if request.method == "POST":
        try:
            estrato = int(request.form["estrato"])
            valor_comercial = float(request.form["valor_comercial"])
            antiguedad = int(request.form["antiguedad"])
            legalidad = request.form["legalidad"].lower() in ["true", "1", "si", "sí"]
            titulo_propiedad = request.form["titulo_propiedad"].lower() in ["true", "1", "si", "sí"]

            propiedades_controller.update_property(
                propiedad_id, estrato, valor_comercial, antiguedad, legalidad, titulo_propiedad
            )
            mensaje = "Propiedad actualizada exitosamente."
            propiedad = propiedades_controller.select_property_properties(propiedad_id)
        except Exception as e:
            print(f"Error al actualizar la propiedad: {e}")
            mensaje = "Error al actualizar la propiedad."
        return render_template("editar.html", propiedad=propiedad, mensaje=mensaje)

    return render_template("editar.html", propiedad=propiedad)



if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 8080)