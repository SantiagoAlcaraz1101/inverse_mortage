class Persona:
    def __init__(self, name: str, age: int, is_women: bool, discapacity_condition: bool):
        self.name: str = name
        self.age: int = age
        self.is_women: bool = is_women
        self.discapacity_condition: bool = discapacity_condition

    def is_old_enough(self) -> bool:
        return self.age >=65

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
        
class Property:
    def __init__(self, stratum: int, commercial_value: float, antiqueness: int, legality: bool):
        self.stratum: int = stratum
        self.commercial_value: float = commercial_value
        self.antiqueness: int = antiqueness
        self.legality: bool = legality

    def is_property_valid(self):
        return self.antiqueness <= 25
    
    def required_stratum(self) -> bool:
        return self.stratum >= 4
    
    def is_value_enough(self) -> bool:
        return self.commercial_value >= 600e5 and self.commercial_value <= 800e5