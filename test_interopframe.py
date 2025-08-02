# test_interopframe.py
"""
Tests for InteropFrame module.
"""

import unittest
from interopframe import InteropFrame

class TestInteropFrame(unittest.TestCase):
    """Test cases for InteropFrame class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = InteropFrame()
        self.assertIsInstance(instance, InteropFrame)
        
    def test_run_method(self):
        """Test the run method."""
        instance = InteropFrame()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
