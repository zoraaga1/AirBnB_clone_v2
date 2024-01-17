#!/usr/bin/python3
"""Test suite for DBStorage class"""
import unittest
import pep8
import json
import os
from os import getenv
import MySQLdb
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage


@unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
class TestDBStorage(unittest.TestCase):
    '''Test cases for the DBStorage class'''

    @classmethod
    def setUpClass(cls):
        """Set up for the test"""
        cls.User = getenv("HBNB_MYSQL_USER")
        cls.Passwd = getenv("HBNB_MYSQL_PWD")
        cls.Db = getenv("HBNB_MYSQL_DB")
        cls.Host = getenv("HBNB_MYSQL_HOST")
        cls.db = MySQLdb.connect(host=cls.Host, user=cls.User, passwd=cls.Passwd, db=cls.Db, charset="utf8")  # noqa
        cls.query = cls.db.cursor()
        cls.storage = DBStorage()
        cls.storage.reload()

    @classmethod
    def tearDownClass(cls):
        """Clean up resources after testing"""
        cls.query.close()
        cls.db.close()

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_pep8_style_compliance(self):
        """Check if the DBStorage class complies with PEP8 style guidelines"""
        style = pep8.StyleGuide(quiet=True)
        res = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(res.total_errors, 0, "Fix PEP8 style issues")

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_read_tables(self):
        """Check if the expected tables exist in the database"""
        self.query.execute("SHOW TABLES")
        res = self.query.fetchall()
        self.assertEqual(len(res), 7)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_no_element_user(self):
        """Check if there are no elements in the users table"""
        self.query.execute("SELECT * FROM users")
        res = self.query.fetchall()
        self.assertEqual(len(res), 0)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_no_element_cities(self):
        """Check if there are no elements in the cities table"""
        self.query.execute("SELECT * FROM cities")
        res = self.query.fetchall()
        self.assertEqual(len(res), 0)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_add(self):
        """Check if adding an element ress in the correct table size"""
        self.query.execute("SELECT * FROM states")
        res = self.query.fetchall()
        self.assertEqual(len(res), 0)
        state = State(name="LUISILLO")
        state.save()
        self.db.autocommit(True)
        self.query.execute("SELECT * FROM states")
        res = self.query.fetchall()
        self.assertEqual(len(res), 1)


if __name__ == "__main__":
    unittest.main()
