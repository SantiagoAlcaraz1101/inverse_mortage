import unittest
import sys 
sys.path.append("src")

from src.model.inverse_mortage import Person, Property
from src.model.exceptions import *

class TestInverseMortage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #Normal Cases
        cls.normal_testcase_Property_1 = Property(4, 655e5, 25, True)
        cls.normal_testcase_Person_1 = Person("Pepito Perez Vaquero", 65, True, False, cls.normal_testcase_Property_1, True)

        cls.normal_testcase_Property_2 = Property(6, 750e5, 7, True)
        cls.normal_testcase_Person_2 = Person("Sol Baquero", 66, True, False, cls.normal_testcase_Property_2, True)

        cls.normal_testcase_Property_3 = Property(4, 655e5, 1, False)
        cls.normal_testcase_Person_3 = Person("Anastacia Caly", 71, True,False, cls.normal_testcase_Property_3, True)

        # Extraordinary Cases
        cls.extraordinary_testcase_Property_1 = Property(4, 655e5, 25, True)
        cls.extraordinary_testcase_Person_1 = Person("Pepito Perez Vaquero", 85, False, False, cls.extraordinary_testcase_Property_1, True)

        cls.extraordinary_testcase_Property_2 = Property(5, 655e5, 15, False)
        cls.extraordinary_testcase_Person_2 = Person("Juanito Monsalve Castrillon", 70, False, False, cls.extraordinary_testcase_Property_2, True)

        cls.extraordinary_testcase_Property_3 = Property(5, 655e5, 15, True)
        cls.extraordinary_testcase_Person_3 = Person("Carlos Sanchez", 60, False, True, cls.extraordinary_testcase_Property_3, True)

        # Fail Cases

        cls.fail_testcase_Property_1 = Property(4, 655e5, 25, True)
        cls.fail_testcase_Person_1 = Person("Pepito Perez Vaquero", 65, True, False, cls.fail_testcase_Property_1, False)

        cls.fail_testcase_Property_2 = Property(7, 750e5, 18, True)
        cls.fail_testcase_Person_2 = Person("Sol Baquero", 66, True, False, cls.fail_testcase_Property_2, True)

        cls.fail_testcase_Property_3 = Property(4, 1000e5, 1, False)
        cls.fail_testcase_Person_3 = Person("Anastacia Caly", 71, True,False, cls.fail_testcase_Property_3, True)

    @classmethod
    def tearDownClass(cls):
        del cls.normal_testcase_Property_1
        del cls.normal_testcase_Person_1
        del cls.normal_testcase_Property_2
        del cls.normal_testcase_Person_2
        del cls.normal_testcase_Property_3
        del cls.normal_testcase_Person_3
        del cls.extraordinary_testcase_Property_1
        del cls.extraordinary_testcase_Person_1
        del cls.extraordinary_testcase_Property_2
        del cls.extraordinary_testcase_Person_2
        del cls.extraordinary_testcase_Property_3
        del cls.extraordinary_testcase_Person_3
        del cls.fail_testcase_Property_1
        del cls.fail_testcase_Person_1
        del cls.fail_testcase_Property_2
        del cls.fail_testcase_Person_2
        del cls.fail_testcase_Property_3
        del cls.fail_testcase_Person_3


    
    def test_normal_1(self):
        with self.assertRaises(PropertyValueError):
            self.normal_testcase_Property_1.is_value_enough()
        self.assertTrue(self.normal_testcase_Person_1.is_old_enough())
        self.assertTrue(self.normal_testcase_Property_1.required_stratum())
        self.assertTrue(self.normal_testcase_Property_1.is_property_valid())
        self.assertEqual(self.normal_testcase_Person_1.hope_of_life(), 13)

    def test_normal_2(self):
        with self.assertRaises(PropertyValueError):
            self.normal_testcase_Property_2.is_value_enough()
        self.assertTrue(self.normal_testcase_Person_2.is_old_enough())
        self.assertTrue(self.normal_testcase_Property_2.required_stratum())
        self.assertTrue(self.normal_testcase_Property_2.is_property_valid())
        self.assertEqual(self.normal_testcase_Person_2.hope_of_life(), 12)

    def test_normal_3(self):
        with self.assertRaises(PropertyValueError):
            self.normal_testcase_Property_3.is_value_enough()
        self.assertTrue(self.normal_testcase_Person_3.is_old_enough())
        self.assertTrue(self.normal_testcase_Property_3.required_stratum())
        self.assertTrue(self.normal_testcase_Property_3.is_property_valid())
        self.assertEqual(self.normal_testcase_Person_3.hope_of_life(), 7)

    def test_extraordinary_1(self):
        self.assertTrue(self.extraordinary_testcase_Property_1.required_stratum())
        self.assertEqual(self.extraordinary_testcase_Person_1.hope_of_life(), 0)
        with self.assertRaises(OldAgeError):
            self.extraordinary_testcase_Person_1.is_old_enough()
        with self.assertRaises(PropertyValueError):
            self.extraordinary_testcase_Property_1.is_value_enough()

    def test_extraordinary_2(self):
        with self.assertRaises(PropertyValueError):
            self.extraordinary_testcase_Property_2.is_value_enough()
        self.assertTrue(self.extraordinary_testcase_Property_2.required_stratum())
        self.assertTrue(self.extraordinary_testcase_Property_2.is_property_valid())
        self.assertEqual(self.extraordinary_testcase_Person_2.hope_of_life(), 1)

    def test_extraordinary_3(self):
        with self.assertRaises(OldAgeError):
            self.extraordinary_testcase_Person_3.is_old_enough()
        with self.assertRaises(PropertyValueError):
            self.extraordinary_testcase_Property_3.is_value_enough()
        with self.assertRaises(PropertyValueError):
            self.extraordinary_testcase_Property_3.is_value_enough()
        self.assertTrue(self.extraordinary_testcase_Property_3.required_stratum())
        self.assertEqual(self.extraordinary_testcase_Person_3.hope_of_life(), 11)

    def test_fail_1(self):
        with self.assertRaises(PropertyValueError):
            self.fail_testcase_Property_1.is_value_enough()
        self.assertTrue(self.fail_testcase_Person_1.is_old_enough())
        self.assertTrue(self.fail_testcase_Property_1.required_stratum())
        self.assertTrue(self.fail_testcase_Property_1.is_property_valid())
        self.assertEqual(self.fail_testcase_Person_1.hope_of_life(), 13)

    def test_fail_2(self):
        with self.assertRaises(PropertyValueError):
            self.fail_testcase_Property_2.is_value_enough()
        self.assertTrue(self.fail_testcase_Person_2.is_old_enough())
        self.assertTrue(self.fail_testcase_Property_2.is_property_valid())
        self.assertEqual(self.fail_testcase_Person_2.hope_of_life(), 12)

    def test_fail_3(self):
        with self.assertRaises(PropertyValueError):
            self.fail_testcase_Property_2.is_value_enough()
        self.assertTrue(self.fail_testcase_Person_3.is_old_enough())
        self.assertTrue(self.fail_testcase_Property_3.required_stratum())
        self.assertTrue(self.fail_testcase_Property_3.is_property_valid())
        self.assertEqual(self.fail_testcase_Person_3.hope_of_life(), 7)
    

if __name__ == "__main__":
    unittest.main()


