# test_branchblaze.py
"""
Tests for BranchBlaze module.
"""

import unittest
from branchblaze import BranchBlaze

class TestBranchBlaze(unittest.TestCase):
    """Test cases for BranchBlaze class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BranchBlaze()
        self.assertIsInstance(instance, BranchBlaze)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BranchBlaze()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
