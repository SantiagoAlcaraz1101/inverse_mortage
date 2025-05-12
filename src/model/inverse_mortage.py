import sys 
sys.path.append("src")
from .exceptions import PropertyAntiquenessBigger, PropertyValueError, StratumError, OldAgeError
import hashlib

class Property:
    def __init__(self, stratum: int, commercial_value: float, antiqueness: int, legality: bool, taxes_ok: bool):
        self.stratum = stratum
        self.commercial_value = commercial_value
        self.antiqueness = antiqueness
        self.legality = legality
        self.taxes_ok = taxes_ok
        self.id_property:int = self.hash_calc()
        
    def hash_calc(self):
        unique_string = f"{self.stratum}-{self.commercial_value}-{self.antiqueness}-{self.legality}-{self.taxes_ok}"
        return hashlib.sha256(unique_string.encode()).hexdigest()

    
    def to_tuple(self):
        return (self.id_property, self.stratum, self.commercial_value, self.antiqueness, self.legality, self.taxes_ok)

    def is_value_enough(self):
        if self.commercial_value < 700_000_000:
            raise PropertyValueError("El valor comercial de la propiedad no es suficiente.")
        return True

    def is_property_valid(self):
        if self.antiqueness > 30:
            raise PropertyAntiquenessBigger("La antigüedad de la propiedad es demasiado alta.")
        if not self.legality:
            raise PropertyValueError("La propiedad no es legal.")
        if not self.taxes_ok:
            raise PropertyValueError("La propiedad no está al día con los impuestos.")
        return True

    def required_stratum(self):
        if self.stratum < 1 or self.stratum > 6:
            raise StratumError("El estrato debe estar entre 1 y 6.")
        return True

    

class Person:
    def __init__(self, name: str, age: int, is_women: bool, discapacity_condition: bool, property_title: bool, property: Property ):
        self.name: str = name
        self.age: int = age
        self.is_women: bool = is_women
        self.discapacity_condition: bool = discapacity_condition
        self.property_title: bool = property_title
        self.property:Property  = property  
        
    def to_tuple(self):
        return (self.name, self.age, self.is_women, self.discapacity_condition, self.property_title, self.property.id_property)
    
    def is_old_enough(self) -> bool:
        if self.age < 65 or self.age >= 80:
            raise OldAgeError()
        return True

    def hope_of_life(self) -> int:
        if self.is_women:
            life_expentancy: int = 78
            if life_expentancy < self.age:
                return 0 

            return life_expentancy - self.age
        else:
            life_expentancy: int = 71
            if life_expentancy < self.age:
                return 0 
            return life_expentancy - self.age
        
