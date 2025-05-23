import sys
sys.path.append('.')

from flask import Flask, render_template, request
from src.controller.personas_controller import select_person_properties


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('principal.html')


@app.route('/buscar')
def buscar():
    return render_template('buscar.html')

@app.route('/buscar_propiedades')
def buscar_propiedades():
    id_property = request.args['cedula']
    property = select_person_properties(id_property)
    return render_template('resultado_busqueda.html', property=property)

        
if __name__ == '__main__':
    app.run(debug=True)