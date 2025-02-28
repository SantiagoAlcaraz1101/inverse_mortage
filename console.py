from inverse_mortage import Person, Property
from exceptions import *
#Variables de entrada:
"""
--------Propietario---------
Nombre: str
Edad: int
gender: Bool (is_women)
Condición de Discapacidad: Bool
Título de propiedad(Si/No)-> Bool

-------Propiedad---------
Estrato: int
Valor Comercial: float
Antiguedad: int
Legalidad: Bool
"""
def input_data_person():
    print("------------Bienvenido-----------\n-Calculadora de Hipoteca Inversa-")
    name = str(input("Ingresa tu nombre: "))
    age = int(input("Ingresa tu edad: "))
    gender = str(input("Ingrese S: Si eres mujer, N:Si eres Hombre"))
    if gender.lower == "s":
        is_women = True
    else: 
        is_women = False
    condition = str(input("Ingrese S: Si tienes discapacidad física\n N:No tienes discapacidad\n:"))
    if condition.lower() == "s":
        discapacity_condition = True
    else: 
        discapacity_condition = False


    title = str(input("Ingresa S: Si la propiedad está a tu nombre:\n: No está a tu nombre:\n: "))
    if title.lower() == "s":
        title_property = True
    else:
        title_property = False

    return name, age, is_women, discapacity_condition, title_property

def input_data_property():
    print("---Datos de la propiedad")
    stratum = int(input("Ingresa el estrato de la propiedad: "))
    commercial_value = float(input("Ingresa el valor comercial de la propiedad: "))
    antiqueness = int(input("Ingresa la antiguedad de la propiedad: "))
    legal_property = str(input("Ingresa S: Si la propiedad está al día con los impuestos:\n: No está al día con los impuestos\n: "))
    if legal_property.lower() == "s":
        legality = True
    else:
        legality = False
    
    

    return stratum, commercial_value, antiqueness, legality


def console(persona:Person, propiedad: Property):
    try:
        persona.is_old_enough()
        persona.hope_of_life()
    except:
        raise OldAgeShorter()




if __name__ == "__main__":
    name, age, is_women, discapacity_condition, title_property = input_data_person()
    stratum, commercial_value, antiqueness, legality = input_data_property()
    propiedad = Property(stratum=stratum, commercial_value=commercial_value, antiqueness=antiqueness, legality=legality)
    usuario= Person(name=name, age=age, is_women=is_women, discapacity_condition=discapacity_condition, property=propiedad, property_title=title_property)
    input_data_person()
    input_data_property()
    console(usuario, propiedad)




