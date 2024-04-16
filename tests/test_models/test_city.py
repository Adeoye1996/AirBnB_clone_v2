#!/usr/bin/python3
"""Test cases for City class."""

import unittest
import os
import pycodestyle
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Represents the tests for the City class."""

    @classmethod
    def setUpClass(cls):
        """Set up for the test."""
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    @classmethod
    def tearDownClass(cls):
        """At the end of the test this will tear it down."""
        del cls.city

    def tearDown(self):
        """Teardown."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8_City(self):
        """Tests pep8 style."""
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_City(self):
        """Checking for docstrings."""
        self.assertIsNotNone(City.__doc__)

    def test_attributes_City(self):
        """Check if City has attributes."""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_is_subclass_City(self):
        """Test if City is subclass of BaseModel."""
        self.assertTrue(issubclass(self.city.__class__, BaseModel))

    def test_attribute_types_City(self):
        """Test attribute type for City."""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_save_City(self):
        """Test if the save works."""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_City(self):
        """Test if dictionary works."""
        self.assertTrue(hasattr(self.city, 'to_dict'))


class TestPEP8(unittest.TestCase):
    """Test PEP8 style for City class."""

    def test_pep8_city(self):
        """Test PEP8 style."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == "__main__":
    unittest.main()
