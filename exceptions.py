class OldAgeError(Exception):
    def __init__(self, message = "Edad ingresada no alcanza el rango permitido. Tu edad no está entre 65 y 80"):
        super().__init__(message)

class StratumError(Exception):
    def __init__(self, message = "Estrato erróneo en Colombia. Verifica que esté en el rango 4 - 6"):
        super().__init__(message)
    
class PropertyValueError(Exception):
    def __init__(self, message = "El valor de la propiedad es menor al permitido para acceder a la Hipoteca."):
        super().__init__(message)

class PropertyAntiquenessBigger(Exception):
    def __init__(self, message = "La antiguedad de la propiedad supera el rango permitido. Mayor a 25 años"):
        super().__init__(message)