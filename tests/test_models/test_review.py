#!/usr/bin/python3
"""Test suite for Review class"""
import unittest
import os
from os import getenv
from models.review import Review
from models.base_model import BaseModel
import pep8


class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    @classmethod
    def setUpClass(cls):
        """Set up a Review instance for testing"""
        cls.rev = Review()
        cls.rev.place_id = "9876-abcd"
        cls.rev.user_id = "169-cba"
        cls.rev.text = "A fantastic experience!"

    @classmethod
    def tearDownClass(cls):
        """Clean up resources after testing"""
        del cls.rev

    def tearDown(self):
        """Remove temporary file created during testing"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_style_compliance(self):
        """Check if the Review class complies with PEP8 style guidelines"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8 style issues")

    def test_checking_for_docstring_Review(self):
        """Check if the Review class has a docstring"""
        self.assertIsNotNone(Review.__doc__)

    def test_attributes_existence_Review(self):
        """Check if Review instance has the expected attributes"""
        self.assertTrue('id' in self.rev.__dict__)
        self.assertTrue('created_at' in self.rev.__dict__)
        self.assertTrue('updated_at' in self.rev.__dict__)
        self.assertTrue('place_id' in self.rev.__dict__)
        self.assertTrue('text' in self.rev.__dict__)
        self.assertTrue('user_id' in self.rev.__dict__)

    def test_is_subclass_of_base_model_Review(self):
        """Check if Review is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.rev.__class__, BaseModel), True)

    def test_attribute_types_Review(self):
        """Check if attribute types are correct for Review"""
        self.assertEqual(type(self.rev.text), str)
        self.assertEqual(type(self.rev.place_id), str)
        self.assertEqual(type(self.rev.user_id), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save_Review(self):
        """Check if save() updates timestamps"""
        self.rev.save()
        self.assertNotEqual(self.rev.created_at, self.rev.updated_at)

    def test_to_dict_Review(self):
        """Check if to_dict() returns a dictionary"""
        review_dict = self.rev.to_dict()
        self.assertIsInstance(review_dict, dict)


if __name__ == "__main__":
    unittest.main()
