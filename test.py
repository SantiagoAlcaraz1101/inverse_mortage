import unittest
from inverse_mortage import Person, Property


normal_testcase_Property_1 = Property(4, 655e5, 25, True)
normal_testcase_Person_1 = Person("Pepito Perez Vaquero", 65, True, False, normal_testcase_Property_1)

normal_testcase_Property_2 = Property(6, 750e5, 7, True)
normal_testcase_Person_2 = Person("Sol Baquero", 66, True, False, normal_testcase_Property_2)



normal_testcase_Property_3 = Property(4, 655e5, 1, False)
normal_testcase_Person_3 = Person("Anastacia Caly", 71, True,False, normal_testcase_Property_3)

extraordinary_testcase_Property_1 = Property(4, 655e5, 25, True)
extraordinary_testcase_Person_1 = Person("Pepito Perez Vaquero", 85, True, False, extraordinary_testcase_Property_1)



class inverse_mortage(unittest.TestCase):
    
    def test_normal_1(self):
        self.assertTrue(normal_testcase_Person_1.is_old_enough())
        self.assertTrue(normal_testcase_Property_1.required_stratum())
        self.assertTrue(normal_testcase_Property_1.is_value_enough())
        self.assertTrue(normal_testcase_Property_1.is_property_valid())
        self.assertEqual(normal_testcase_Person_1.hope_of_life(), 13)

    def test_normal_2(self):
        self.assertTrue(normal_testcase_Person_2.is_old_enough())
        self.assertTrue(normal_testcase_Property_2.required_stratum())
        self.assertTrue(normal_testcase_Property_2.is_value_enough())
        self.assertTrue(normal_testcase_Property_2.is_property_valid())
        self.assertEqual(normal_testcase_Person_2.hope_of_life(), 12)

    def test_normal_3(self):
        self.assertTrue(normal_testcase_Person_3.is_old_enough())
        self.assertTrue(normal_testcase_Property_3.required_stratum())
        self.assertTrue(normal_testcase_Property_3.is_value_enough())
        self.assertTrue(normal_testcase_Property_3.is_property_valid())
        self.assertEqual(normal_testcase_Person_3.hope_of_life(), 7)

    def test_extraordinary_1(self):
        self.assertTrue(extraordinary_testcase_Person_1.is_old_enough())
        self.assertTrue(extraordinary_testcase_Property_1.required_stratum())
        self.assertTrue(extraordinary_testcase_Property_1.is_value_enough())
        self.assertTrue(extraordinary_testcase_Property_1.is_property_valid())
        self.assertEqual(extraordinary_testcase_Person_1.hope_of_life(), 0)

    

if __name__ == "__main__":
    unittest.main()
