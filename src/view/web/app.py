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
        


if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 8080)