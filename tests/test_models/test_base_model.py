#!/usr/bin/python3
"""Test suite for BaseModel class"""
import unittest
import os
from os import getenv
from models.base_model import BaseModel
import pep8


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """Set up a BaseModel instance for testing"""
        cls.base = BaseModel()
        cls.base.name = "Sara"
        cls.base.num = 20

    @classmethod
    def tearDownClass(cls):
        """Clean up resources after testing"""
        del cls.base

    def tearDown(self):
        """Remove temporary file created during testing"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_style_compliance(self):
        """Check if the BaseModel class complies with PEP8 style guidelines"""
        style = pep8.StyleGuide(quiet=True)
        res = style.check_files(['models/base_model.py'])
        self.assertEqual(res.total_errors, 0, "Fix PEP8 style issues")

    def test_checking_for_docstring_BaseModel(self):
        """Check if the BaseModel class has docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method_existence_BaseModel(self):
        """Check if BaseModel class has the required methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init_BaseModel(self):
        """Check if the base instance is of type BaseModel"""
        self.assertTrue(isinstance(self.base, BaseModel))

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save_BaseModel(self):
        """Check if save() updates timestamps"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict_BaseModel(self):
        """Check if to_dict() returns a dictionary"""
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
