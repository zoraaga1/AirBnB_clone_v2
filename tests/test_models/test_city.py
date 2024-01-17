#!/usr/bin/python3
"""Test suite for City class"""
import unittest
import os
from models.city import City
from models.base_model import BaseModel
import pep8
from os import getenv


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    @classmethod
    def setUpClass(cls):
        """Set up a City instance for testing"""
        cls.city = City()
        cls.city.name = "San Francisco"
        cls.city.state_id = "CA"

    @classmethod
    def tearDownClass(cls):
        """Clean up resources after testing"""
        del cls.city

    def tearDown(self):
        """Remove temporary file created during testing"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_style_compliance(self):
        """Check if the City class complies with PEP8 style guidelines"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8 style issues")

    def test_checking_for_docstring_City(self):
        """Check if the City class has a docstring"""
        self.assertIsNotNone(City.__doc__)

    def test_attributes_existence_City(self):
        """Check if City instance has the expected attributes"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_is_subclass_of_base_model_City(self):
        """Check if City is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attribute_types_City(self):
        """Check if attribute types are correct for City"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save_City(self):
        """Check if save() updates timestamps"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_City(self):
        """Check if to_dict() returns a dictionary"""
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
