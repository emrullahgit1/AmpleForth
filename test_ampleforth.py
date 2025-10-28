# test_ampleforth.py
"""
Tests for AmpleForth module.
"""

import unittest
from ampleforth import AmpleForth

class TestAmpleForth(unittest.TestCase):
    """Test cases for AmpleForth class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AmpleForth()
        self.assertIsInstance(instance, AmpleForth)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AmpleForth()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
