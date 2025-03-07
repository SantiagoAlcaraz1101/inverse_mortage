from errors.exceptions import *
class Property:
    def __init__(self, stratum: int, commercial_value: float, antiqueness: int, legality: bool):
        self.stratum: int = stratum
        self.commercial_value: float = commercial_value
        self.antiqueness: int = antiqueness
        self.legality: bool = legality

    def is_property_valid(self):
        if self.antiqueness > 25:
            raise PropertyAntiquenessBigger()
        return True
    
    def required_stratum(self) -> bool:
        if self.stratum < 4 or self.stratum > 6:
            raise StratumError()
        return True
    
    def is_value_enough(self) -> bool:
        if self.commercial_value < 600e6 or self.commercial_value >= 800e6:
            raise PropertyValueError()
        return True
    

class Person:
    def __init__(self, name: str, age: int, is_women: bool, discapacity_condition: bool, property: Property, property_title: bool):
        self.name: str = name
        self.age: int = age
        self.is_women: bool = is_women
        self.discapacity_condition: bool = discapacity_condition
        self.property: Property = property
        self.property_title: bool = property_title
        

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
        
