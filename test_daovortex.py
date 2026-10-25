# test_daovortex.py
"""
Tests for DaoVortex module.
"""

import unittest
from daovortex import DaoVortex

class TestDaoVortex(unittest.TestCase):
    """Test cases for DaoVortex class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = DaoVortex()
        self.assertIsInstance(instance, DaoVortex)

    def test_run_method(self):
        """Test the run method."""
        instance = DaoVortex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
