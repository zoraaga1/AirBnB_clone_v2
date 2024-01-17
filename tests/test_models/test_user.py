#!/usr/bin/python3
"""Test User module"""
import os
from models.base_model import BaseModel
from models.user import User
import unittest
import pep8

class TestUser(unittest.TestCase):
    """Unit tests for User class"""

    @classmethod
    def setUpClass(cls):
        """Set up the User instance for testing"""
        cls.user = User()
        cls.user.first_name = "Sara"
        cls.user.last_name = "Jhonas"
        cls.user.email = "sara.jhonas@gmail.com"
        cls.user.password = "sarapsswd"

    @classmethod
    def tearDownClass(cls):
        """Clean up resources after testing"""
        del cls.user

    def tearDown(self):
        """Remove temporary file created during testing"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_style_compl(self):
        """Check if the User class complies
        with PEP8 style guidelines"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix PEP8")

    def test_has_docstring(self):
        """Check if the User class has a docstring"""
        self.assertIsNotNone(User.__doc__)

    def test_attributes_User(self):
        """Check if User instance has the expected attributes"""
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def test_is_subclass(self):
        """Check if User is subclass of BaseModel"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_attribute_types(self):
        """Check if attribute types are correct for User"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.first_name), str)

    def test_save(self):
        """Check if calling save() updates the timestamps"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict(self):
        """Check if to_dict() returns a dictionary"""
        self.assertEqual('to_dict' in dir(self.user), True)


if __name__ == "__main__":
    unittest.main()
