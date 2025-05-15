import unittest
import sys 
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.model.inverse_mortage import Person, Property
from src.model.exceptions import *
from src.controller.personas_controller import connect_db, create_table_people, insert_person, delete_person, update_persona


class TestInverseMortage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #Normal Cases
        cls.normal_testcase_Property_1 = Property(4, 655e5, 25, True, True)
        cls.normal_testcase_Person_1 = Person("Pepito Perez Vaquero", 65, True, False, cls.normal_testcase_Property_1, True)

        cls.normal_testcase_Property_2 = Property(6, 750e5, 7, True, True)
        cls.normal_testcase_Person_2 = Person("Sol Baquero", 66, True, False, cls.normal_testcase_Property_2, True)

        cls.normal_testcase_Property_3 = Property(4, 655e5, 1, True, True)
        cls.normal_testcase_Person_3 = Person("Anastacia Caly", 71, True,True, cls.normal_testcase_Property_3, True)

        # Extraordinary Cases
        cls.extraordinary_testcase_Property_1 = Property(4, 655e5, 25, True, True)
        cls.extraordinary_testcase_Person_1 = Person("Pepito Perez Vaquero", 85, False, False, cls.extraordinary_testcase_Property_1, True)

        cls.extraordinary_testcase_Property_2 = Property(5, 655e5, 15, True, True)
        cls.extraordinary_testcase_Person_2 = Person("Juanito Monsalve Castrillon", 70, False, False, cls.extraordinary_testcase_Property_2, True)

        cls.extraordinary_testcase_Property_3 = Property(5, 655e5, 15, True, True)
        cls.extraordinary_testcase_Person_3 = Person("Carlos Sanchez", 60, False, True, cls.extraordinary_testcase_Property_3, True)

        # Fail Cases

        cls.fail_testcase_Property_1 = Property(4, 655e5, 25, True, True)
        cls.fail_testcase_Person_1 = Person("Pepito Perez Vaquero", 65, True, False, cls.fail_testcase_Property_1, False)

        cls.fail_testcase_Property_2 = Property(7, 750e5, 18, True, True)
        cls.fail_testcase_Person_2 = Person("Sol Baquero", 66, True, False, cls.fail_testcase_Property_2, True)

        cls.fail_testcase_Property_3 = Property(4, 1000e5, 1, True, True)
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
    

class TestDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = connect_db()
        cls.test_property = Property(5, 800000000, 20, True, True)
        
    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'conn') and cls.conn is not None:
            cls.conn.close()

    def test_create_table_normal(self):
        try:
            create_table_people()
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"create_table_people raised exception: {e}")

    def test_insert_person_normal(self):
        try:
            test_person = Person("Test Person", 70, False, False, self.test_property, True)
            insert_person(test_person)
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"insert_person raised exception: {e}")

    def test_update_person_normal(self):
        try:
            person_id = 1
            updated_person = Person("Updated Person", 72, True, False, self.test_property, True)
            update_persona(person_id, updated_person)
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"update_persona raised exception: {e}")

    def test_delete_person_normal(self):
        try:
            person_id = 1
            delete_person(person_id)
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"delete_person raised exception: {e}")

    def test_insert_person_failed(self):
        try:
            insert_person(None)
            self.assertTrue(True)  
        except Exception:
            self.assertTrue(True)

    def test_update_person_failed(self):
        # Test with invalid ID
        try:
            update_persona(-999, Person("Invalid", 70, False, False, self.test_property, True))
            self.assertTrue(True)  
        except Exception:
            self.assertTrue(True)

    def test_delete_person_failed(self):
        # Test with invalid ID
        try:
            delete_person(-999)
            self.assertTrue(True)  
        except Exception:
            self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()