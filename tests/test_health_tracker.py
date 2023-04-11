import unittest
from unittest.mock import patch
from io import StringIO
import sys
import health_tracker

class TestHealthTracker(unittest.TestCase):
    sys.stdout
    sys.stdin

    @patch('sys.stdin', StringIO('Shado\nFemale\n23\n50\n130'))
    def test_main(self):
        pass


if __name__ == '__main__':
    unittest.main()