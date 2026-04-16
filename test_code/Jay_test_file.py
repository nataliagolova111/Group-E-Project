#Automated testing

import unittest

def save_item(item_name:str, item_quantity:int):
    try:
        with open("items.txt", "a") as file:
            file.write(f"{item_name},{item_quantity}\n")
        print(f"\nSaved: {item_name} | Quantity: {item_quantity}")
        return "SUCCESS" # For testing purposes only
    except FileNotFoundError:
        print("Failed to save item. Error: items.txt/inventory does not exist")
        return "FAILURE" # For testing purposes only

class TestYourFunction(unittest.TestCase):

    def test_save_valid_item(self):
        # Test normal case
        result = save_item("Apple", 10)
        self.assertEqual(result, "SUCCESS")
    
    #No test needed for error case

if __name__ == '__main__':
    unittest.main()