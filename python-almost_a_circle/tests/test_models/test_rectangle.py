#!/usr/bin/python3
"""Rectangle class tests."""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    """Test for the rectangle class methods."""

    def test_instance(self):
        r = Rectangle(1, 2)
        self.assertEqual(isinstance(r, Rectangle), True)


if __name__ == "__main__":
    unittest.main()
