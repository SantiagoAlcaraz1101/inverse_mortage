import unittest

from check_process import is_old_enough, required_stratum, is_value_enough, is_property_valid, hope_of_life

normal_testcase_1 = (65, 4, 655e5, 25, True, True)
normal_testcase_2 = (66, 6, 750e5, 7, True, True)
normal_testcase_3 = (71, 4, 655e5, 1, False, True)
extraordinary_testcase_1 = (85, 4, 655e5, 18, False, True)


class inverse_mortage(unittest.TestCase):

    

    def normal_testcase_1(self, age: int, stratum: int, commercial_value: float, antiqueness: int, is_women: bool, is_legal: bool):

        if is_old_enough(age) and required_stratum(stratum) and is_value_enough(commercial_value) and is_property_valid(antiqueness) and hope_of_life(age, is_women) and is_legal:
            return True
        return False
    
    def normal_testcase_value1():
        pass

    #Verifica si puede acceder a la hipoteca inversa
    def test_normal_testcase_1(self):
        age, stratum, commercial_value, antiqueness, is_women, is_legal = normal_testcase_1
        result = self.normal_testcase_1(age, stratum, commercial_value, antiqueness, is_women, is_legal)
        self.assertTrue(result)

    #Caso normal 2
    def normal_testcase_2(self, age: int, stratum: int, commercial_value: float, antiqueness: int, is_women: bool, is_legal: bool):

        if is_old_enough(age) and required_stratum(stratum) and is_value_enough(commercial_value) and is_property_valid(antiqueness) and hope_of_life(age, is_women) and is_legal:
            return True
        return False
    
    def normal_testcase_value2():
        pass

    #Verifica si puede acceder a la hipoteca inversa
    def test_normal_testcase_2(self):
        age, stratum, commercial_value, antiqueness, is_women, is_legal = normal_testcase_2
        result = self.normal_testcase_2(age, stratum, commercial_value, antiqueness, is_women, is_legal)
        self.assertTrue(result)

    #Caso normal 3
    def normal_testcase_3(self, age: int, stratum: int, commercial_value: float, antiqueness: int, is_women: bool, is_legal: bool):

        if is_old_enough(age) and required_stratum(stratum) and is_value_enough(commercial_value) and is_property_valid(antiqueness) and hope_of_life(age, is_women) and is_legal:
            return True
        return False
    
    def normal_testcase_value3():
        pass

    #Verifica si puede acceder a la hipoteca inversa
    def test_normal_testcase_3(self):
        age, stratum, commercial_value, antiqueness, is_women, is_legal = normal_testcase_3
        result = self.normal_testcase_3(age, stratum, commercial_value, antiqueness, is_women, is_legal)
        self.assertTrue(result)

    
    def extraordinary_testcase_1(self, age: int):

        if is_old_enough(age): #and required_stratum(stratum) and is_value_enough(commercial_value) and is_property_valid(antiqueness) and hope_of_life(age, is_women)== 0 and is_legal:
            return True
        return False

    def test_extraordinary_testcase_1(self):
        age= 85
        result = self.extraordinary_testcase_1(age)
        self.assertTrue(result)

