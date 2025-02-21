class OldAgeBigger(Exception):
    def __init__(self, message = "Edad ingresada supera el rango que permite acceder a la Hipoteca. Lo sentimos"):
        self.message = message

class OldAgeShorter(Exception):
    def __init__(self, message = "Edad ingresada no alcanza el rango permitido. No eres mayor de 65 años"):
        self.message = message

class StratumBigger(Exception):
    def __init__(self, message = "Estrato mayor al permitido en Colombia. Verifica e ingresa de nuevo"):
        self.message = message
    
class InsufficientPropertyValue(Exception):
    def __init__(self, message = "El valor de la propiedad es menor al permitido para acceder a la Hipoteca."):
        self.message = message

class InsufficientPropertyValue(Exception):
    def __init__(self, message = "El valor de la propiedad es menor al permitido para acceder a la Hipoteca."):
        self.message = message

class PropertyAntiquenessBigger(Exception):
    def __init__(self, message = "La antiguedad de la propiedad supera el rango permitido. Mayor a 25 años"):
        self.message = message