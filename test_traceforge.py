# test_traceforge.py
"""
Tests for TraceForge module.
"""

import unittest
from traceforge import TraceForge

class TestTraceForge(unittest.TestCase):
    """Test cases for TraceForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TraceForge()
        self.assertIsInstance(instance, TraceForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TraceForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
