import unittest
from unittest.mock import patch
from io import StringIO
import sys
from bmi_calculator import *


class TestBMICalculator(unittest.TestCase):
    sys.stdout
    sys.stdin
    
    def test_get_namme(self):
        name = get_name()
        self.assertTrue(name)

    def test_get_gender(self):
        sex = get_gender()
        self.assertTrue(sex)

    def test_get_age(self):
        age = get_age()
        if isinstance(age,int):
            self.assertTrue(age)

    def test_get_weight(self):
        height = get_height()
        if isinstance(height,int):
            self.assertTrue(height)

    def test_get_height(self):
        weight = get_weight()
        if isinstance(weight,int):
            self.assertTrue(weight)

    @patch('sys.stdin', StringIO('50\n130\n'))
    def test_calculate_bmi(self):
        bmi = calculate_bmi()
        test_bmi = 50/(130/100)**2
        self.assertEqual(bmi,test_bmi)


if __name__ == '__main__':
    unittest.main()