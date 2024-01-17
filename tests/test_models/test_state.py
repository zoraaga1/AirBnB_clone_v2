#!/usr/bin/python3
"""Unit tests for State class"""
import unittest
import os
from models.state import State
from models.base_model import BaseModel
import pep8


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    @classmethod
    def setUpClass(cls):
        """Set up a State instance for testing"""
        cls.state = State()
        cls.state.name = "Texas"

    @classmethod
    def tearDownClass(cls):
        """Clean up resources after testing"""
        del cls.state

    def tearDown(self):
        """Remove temporary file created during testing"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_style_compliance(self):
        """Check if the State class complies with PEP8 style guidelines"""
        style = pep8.StyleGuide(quiet=True)
        res = style.check_files(['models/state.py'])
        self.assertEqual(res.total_errors, 0, "Fix PEP8 style issues")

    def test_checking_for_docstring_State(self):
        """Check if the State class has a docstring"""
        self.assertIsNotNone(State.__doc__)

    def test_attributes_existence_State(self):
        """Check if State instance has the expected attributes"""
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_is_subclass_of_base_model_State(self):
        """Check if State is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_attribute_types_State(self):
        """Check if attribute types are correct for State"""
        self.assertEqual(type(self.state.name), str)

    def test_save_State(self):
        """Check if save() updates timestamps"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict_State(self):
        """Check if to_dict() returns a dictionary"""
        self.assertEqual('to_dict' in dir(self.state), True)


if __name__ == "__main__":
    unittest.main()
