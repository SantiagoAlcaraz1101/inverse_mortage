import unittest

class inverse_mortage(unittest.TestCase):

    def is_old_enough(self, age: int) -> bool:
        return age >=65
    
    def required_stratum(self, stratum: int) -> bool:
        return stratum >= 4

    def is_value_enough(self, commercial_value: float) -> bool:
        return commercial_value >= 655e5
    
    def hope_of_life(self, age: int, is_women: bool) -> int:
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
    
    def is_property_valid(self, antiqueness:int ):
        return antiqueness <= 25
    

    
    
    def normal_testcase_1(self, age: int, stratum: int, commercial_value: float, antiqueness: int, is_women: bool, is_legal: bool):
        pass 
        


    

