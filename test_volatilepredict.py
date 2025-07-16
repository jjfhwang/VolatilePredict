# test_volatilepredict.py
"""
Tests for VolatilePredict module.
"""

import unittest
from volatilepredict import VolatilePredict

class TestVolatilePredict(unittest.TestCase):
    """Test cases for VolatilePredict class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VolatilePredict()
        self.assertIsInstance(instance, VolatilePredict)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VolatilePredict()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
