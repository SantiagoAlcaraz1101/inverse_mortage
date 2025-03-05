import unittest
from inverse_mortage import Person, Property
from exceptions import *


# Casos normales

normal_testcase_Property_1 = Property(4, 655e5, 25, True)
normal_testcase_Person_1 = Person("Pepito Perez Vaquero", 65, True, False, normal_testcase_Property_1, True)

normal_testcase_Property_2 = Property(6, 750e5, 7, True)
normal_testcase_Person_2 = Person("Sol Baquero", 66, True, False, normal_testcase_Property_2, True)

normal_testcase_Property_3 = Property(4, 655e5, 1, False)
normal_testcase_Person_3 = Person("Anastacia Caly", 71, True,False, normal_testcase_Property_3, True)

# Casos extraordinarios

extraordinary_testcase_Property_1 = Property(4, 655e5, 25, True)
extraordinary_testcase_Person_1 = Person("Pepito Perez Vaquero", 85, False, False, extraordinary_testcase_Property_1, True)

extraordinary_testcase_Property_2 = Property(5, 655e5, 15, False)
extraordinary_testcase_Person_2 = Person("Juanito Monsalve Castrillon", 70, False, False, extraordinary_testcase_Property_2, True)

extraordinary_testcase_Property_3 = Property(5, 655e5, 15, True)
extraordinary_testcase_Person_3 = Person("Carlos Sanchez", 60, False, True, extraordinary_testcase_Property_3, True)

# Casos de fallo

fail_testcase_Property_1 = Property(4, 655e5, 25, True)
fail_testcase_Person_1 = Person("Pepito Perez Vaquero", 65, True, False, fail_testcase_Property_1, False)

fail_testcase_Property_2 = Property(7, 750e5, 18, True)
fail_testcase_Person_2 = Person("Sol Baquero", 66, True, False, fail_testcase_Property_2, True)

fail_testcase_Property_3 = Property(4, 1000e5, 1, False)
fail_testcase_Person_3 = Person("Anastacia Caly", 71, True,False, fail_testcase_Property_3, True)


class inverse_mortage(unittest.TestCase):
    
    def test_normal_1(self):
        with self.assertRaises(PropertyValueError):
            normal_testcase_Property_1.is_value_enough()
        self.assertTrue(normal_testcase_Person_1.is_old_enough())
        self.assertTrue(normal_testcase_Property_1.required_stratum())
        self.assertTrue(normal_testcase_Property_1.is_property_valid())
        self.assertEqual(normal_testcase_Person_1.hope_of_life(), 13)

    def test_normal_2(self):
        with self.assertRaises(PropertyValueError):
            normal_testcase_Property_2.is_value_enough()
        self.assertTrue(normal_testcase_Person_2.is_old_enough())
        self.assertTrue(normal_testcase_Property_2.required_stratum())
        self.assertTrue(normal_testcase_Property_2.is_property_valid())
        self.assertEqual(normal_testcase_Person_2.hope_of_life(), 12)

    def test_normal_3(self):
        with self.assertRaises(PropertyValueError):
            normal_testcase_Property_3.is_value_enough()
        self.assertTrue(normal_testcase_Person_3.is_old_enough())
        self.assertTrue(normal_testcase_Property_3.required_stratum())
        self.assertTrue(normal_testcase_Property_3.is_property_valid())
        self.assertEqual(normal_testcase_Person_3.hope_of_life(), 7)

    def test_extraordinary_1(self):
        self.assertTrue(extraordinary_testcase_Property_1.required_stratum())
        self.assertEqual(extraordinary_testcase_Person_1.hope_of_life(), 0)
        with self.assertRaises(OldAgeError):
            extraordinary_testcase_Person_1.is_old_enough()
        with self.assertRaises(PropertyValueError):
            extraordinary_testcase_Property_1.is_value_enough()

    def test_extraordinary_2(self):
        with self.assertRaises(PropertyValueError):
            extraordinary_testcase_Property_2.is_value_enough()
        self.assertTrue(extraordinary_testcase_Property_2.required_stratum())
        self.assertTrue(extraordinary_testcase_Property_2.is_property_valid())
        self.assertEqual(extraordinary_testcase_Person_2.hope_of_life(), 1)

    def test_extraordinary_3(self):
        with self.assertRaises(OldAgeError):
            extraordinary_testcase_Person_3.is_old_enough()
        with self.assertRaises(PropertyValueError):
            extraordinary_testcase_Property_3.is_value_enough()
        with self.assertRaises(PropertyValueError):
            extraordinary_testcase_Property_3.is_value_enough()
        self.assertTrue(extraordinary_testcase_Property_3.required_stratum())
        self.assertEqual(extraordinary_testcase_Person_3.hope_of_life(), 11)

    def test_fail_1(self):
        with self.assertRaises(PropertyValueError):
            fail_testcase_Property_1.is_value_enough()
        self.assertTrue(fail_testcase_Person_1.is_old_enough())
        self.assertTrue(fail_testcase_Property_1.required_stratum())
        self.assertTrue(fail_testcase_Property_1.is_property_valid())
        self.assertEqual(fail_testcase_Person_1.hope_of_life(), 13)

    def test_fail_2(self):
        with self.assertRaises(PropertyValueError):
            fail_testcase_Property_2.is_value_enough()
        self.assertTrue(fail_testcase_Person_2.is_old_enough())
        self.assertTrue(fail_testcase_Property_2.is_property_valid())
        self.assertEqual(fail_testcase_Person_2.hope_of_life(), 12)

    def test_fail_3(self):
        with self.assertRaises(PropertyValueError):
            fail_testcase_Property_2.is_value_enough()
        self.assertTrue(fail_testcase_Person_3.is_old_enough())
        self.assertTrue(fail_testcase_Property_3.required_stratum())
        self.assertTrue(fail_testcase_Property_3.is_property_valid())
        self.assertEqual(fail_testcase_Person_3.hope_of_life(), 7)
    

if __name__ == "__main__":
    unittest.main()


