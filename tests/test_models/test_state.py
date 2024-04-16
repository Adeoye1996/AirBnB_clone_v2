#!/usr/bin/python3
"""Test cases for State class."""

from tests.test_models.test_base_model import test_basemodel
from models.state import State


class TestState(test_basemodel):
    """Represents the tests for the State class."""

    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name(self):
        """Test name attribute."""
        new = self.value()
        self.assertEqual(type(new.name), str)
