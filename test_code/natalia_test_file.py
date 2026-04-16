#Automated testing

import unittest

def is_valid_name(name):
    if name.strip() != "" and isinstance(name,str):
        return True
    else:
        return False

class TestIsValidName(unittest.TestCase):

    def test_is_valid_name(self):
        self.assertTrue(is_valid_name("Pen"))
    
    def test_is_valid_name_error(self):
        self.assertFalse(is_valid_name(""))

if __name__ == '__main__':
    unittest.main()