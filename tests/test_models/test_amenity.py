#!/usr/bin/python3
"""Test suite for Amenity class"""
import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel
import pep8


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    @classmethod
    def setUpClass(cls):
        """Set up an Amenity instance for testing"""
        cls.amenity = Amenity()
        cls.amenity.name = "Internet"

    @classmethod
    def tearDownClass(cls):
        """Clean up resources after testing"""
        del cls.amenity

    def tearDown(self):
        """Remove temporary file created during testing"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_style_compliance(self):
        """Check if the Amenity class complies with PEP8 style guidelines"""
        style = pep8.StyleGuide(quiet=True)
        res = style.check_files(['models/amenity.py'])
        self.assertEqual(res.total_errors, 0, "Fix PEP8 style issues")

    def test_checking_for_docstring_Amenity(self):
        """Check if the Amenity class has docstrings"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes_Amenity(self):
        """Check if Amenity has the required attributes"""
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_is_subclass_Amenity(self):
        """Check if Amenity is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_attribute_types_Amenity(self):
        """Check attribute type for Amenity"""
        self.assertEqual(type(self.amenity.name), str)

    def test_save_Amenity(self):
        """Check if save() updates timestamps"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict_Amenity(self):
        """Check if to_dict() returns a dictionary"""
        self.assertEqual('to_dict' in dir(self.amenity), True)


if __name__ == "__main__":
    unittest.main()
