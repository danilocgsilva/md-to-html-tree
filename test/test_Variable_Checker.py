import sys
import os
sys.path.append("..")
from src.Variable_Checker import Variable_Checker
import unittest

class Test_Variable_Checker(unittest.TestCase):

    def test_can_correctly_assert_false_non_existent_variable(self):
        variable_checker = Variable_Checker()
        variable_name = 'NON_EXISTENT_VARIABLE'
        self.assertFalse(variable_checker.exists(variable_name))

    def test_confirm_variable_existence(self):
        variable_checker = Variable_Checker()
        existing_variable = "EXISTING_VARIABLE"
        os.environ[existing_variable] = "any_content"
        self.assertTrue(variable_checker.exists(existing_variable))


if __name__ == '__main__':
    unittest.main()

