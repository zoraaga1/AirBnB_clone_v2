#!/usr/bin/python3
"""Test suite for FileStorage class"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.review import Review
import pep8
import json
import os


class TestFileStorage(unittest.TestCase):
    '''Test cases for the FileStorage class'''

    @classmethod
    def setUpClass(cls):
        """Set up for the test"""
        cls.user = User()
        cls.user.first_name = "Sara"
        cls.user.last_name = "Jhonas"
        cls.user.email = "sara.jhonas@gmail.com"
        cls.storage = FileStorage()

    @classmethod
    def tearDownClass(cls):
        """Clean up resources after testing"""
        del cls.user

    def tearDown(self):
        """Teardown after each test"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_style_compliance(self):
        """Check if the FileStorage class complies with PEP8 style guidelines"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8 style issues")

    def test_all_method(self):
        """Test if the all method returns the __objects attribute"""
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, self.storage._FileStorage__objects)

    def test_new_method(self):
        """Test if the new method adds an object to __objects"""
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.id = 123455
        user.name = "Kevin"
        self.storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])

    def test_reload_method(self):
        """Test if the reload method loads objects from a file correctly"""
        self.storage.save()
        root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(root, "file.json")
        with open(path, 'r') as f:
            lines = f.readlines()
        try:
            os.remove(path)
        except Exception:
            pass
        self.storage.save()
        with open(path, 'r') as f:
            lines2 = f.readlines()
        self.assertEqual(lines, lines2)
        try:
            os.remove(path)
        except Exception:
            pass
        with open(path, "w") as f:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)


if __name__ == "__main__":
    unittest.main()
