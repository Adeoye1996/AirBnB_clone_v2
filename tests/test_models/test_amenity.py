#!/usr/bin/python3
"""Test cases for Amenity class."""

import unittest
import pycodestyle
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime
from unittest.mock import patch
from time import sleep
from os import getenv


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class."""

    def setUp(self):
        """Set up for tests."""
        self.amenity = Amenity()

    def tearDown(self):
        """Tear down after tests."""
        del self.amenity

    def test_instance(self):
        """Test Amenity instance."""
        self.assertIsInstance(self.amenity, BaseModel)
        self.assertIsInstance(self.amenity, Amenity)

    def test_attributes(self):
        """Test Amenity attributes."""
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")

    def test_attributes_db(self):
        """Test Amenity attributes in DB mode."""
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.assertEqual(self.amenity.name, None)

    def test_to_dict(self):
        """Test to_dict method."""
        am = self.amenity
        self.assertIsInstance(am.to_dict(), dict)
        self.assertEqual(am.to_dict()["__class__"], "Amenity")
        self.assertEqual(type(am.to_dict()["created_at"]), str)
        self.assertEqual(type(am.to_dict()["updated_at"]), str)

    def test_str(self):
        """Test __str__ method."""
        amenity = self.amenity
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))

    def test_save(self):
        """Test save method."""
        instance = self.amenity
        created_at = instance.created_at
        sleep(2)
        instance.save()
        new_created_at = instance.created_at
        self.assertNotEqual(created_at, new_created_at)

    def test_str_method(self):
        """Test __str__ method."""
        inst = self.amenity
        string = "[Amenity] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))


class TestAmenityPEP8(unittest.TestCase):
    """Test for Amenity style."""

    def test_pep8_conformance(self):
        """Test that Amenity conforms to PEP8."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/amenity.py"])
        self.assertEqual(result.total_errors, 0)


if __name__ == "__main__":
    unittest.main()
