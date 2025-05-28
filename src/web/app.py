import sys
sys.path.append('.')

from flask import Flask, render_template, request
from src.controller.personas_controller import select_person_properties


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/buscar')
def buscar():
    return render_template('buscar.html')


@app.route('/procesar', methods=['GET', 'POST'])
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

@app.route('/buscar_propiedades')
def buscar_propiedades():
    id_property = request.args['cedula']
    property = select_person_properties(id_property)
    return render_template('resultado_busqueda.html', property=property)

        
if __name__ == '__main__':
    app.run(debug=True)