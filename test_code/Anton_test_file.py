#Automated testing

import unittest

def update_quantity(item_to_change:str, new_quantity:int):
    try:
        with open("Anton_test_items.txt", "r") as f:
            if f.read().strip() == "":
                return None # only for testing purposes, but there is actually None
                            # even without typing it in here
    except FileNotFoundError:
        return
    
    # Use these two inputs as parameters for testing only 
    # item_to_change = input("Enter the name of the item to update: ") 
    # new_quantity = input("Enter the new quantity: ")
    
    updated_items = []
    found = False
    
    with open("Anton_test_items.txt", "r") as f:
        for line in f:
            name, qty = line.strip().split(",")
            if name.lower() == item_to_change.lower():
                updated_items.append(f"{name},{new_quantity}\n")
                found = True
            else:
                updated_items.append(line)
                    
    if found:
        with open("Anton_test_items.txt", "w") as f:
            f.writelines(updated_items)
        print("Quantity updated successfully!")
    else:
        print("Item not found.")

class TestYourFunction(unittest.TestCase):

    # Before testing I created an empty file to check the try block
    # in the beginning of my function
    # Edge case: the file is empty and returns back to the main menu
    def test_item_not_found(self):
        result = update_quantity("Coke", "5")
        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()