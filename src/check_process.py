def is_old_enough(age: int) -> bool:
        return age >=65
    
def required_stratum(stratum: int) -> bool:
        return stratum >= 4

def is_value_enough(commercial_value: float) -> bool:
        return commercial_value >= 655e5
    
def hope_of_life(age: int, is_women: bool) -> int:
        if is_women:
            life_expentancy: int = 78
            if life_expentancy < age:
                return 0 

            return life_expentancy - age
        else:
            life_expentancy: int = 71
            if life_expentancy < age:
                return 0 
            return life_expentancy - age
    
def is_property_valid(antiqueness:int ):
        return antiqueness <= 25
