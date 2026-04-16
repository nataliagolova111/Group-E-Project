import unittest

### Functions ###

def save_item(item_name:str, item_quantity:int):
    try:
        with open("items.txt", "a") as file:
            file.write(f"{item_name},{item_quantity}\n")
        print(f"\nSaved: {item_name} | Quantity: {item_quantity}")
        return "SUCCESS" # For testing purposes only
    except FileNotFoundError:
        print("Failed to save item. Error: items.txt/inventory does not exist")
        return "FAILURE" # For testing purposes only
    
def is_valid_name(name):
    if name.strip() != "" and isinstance(name,str):
        return True
    else:
        return False
    
def view_items():
    try:
        with open("items.txt", "r") as f:
            line = f.readline()

            if line == "":
                print("There's no content in the txt.")
                return
            
            print("Inventory List:\n")

            count = 1
            while line != "":
                line = line.strip()

                if line != "":
                    parts = line.split(",")
                    name = parts[0]
                    quantity = parts[1]

                    print(count , "-" , "Name: " , name , "| Quantity: " , quantity)
                    count += 1

                line = f.readline()
    except:
        print("The txt doesn't exist.")


### Tests ###

class TestYourFunction(unittest.TestCase):

    def test_save_valid_item(self):
        # Test normal case
        result = save_item("Apple", 10)
        self.assertEqual(result, "SUCCESS")
    
    #No test needed for error case

    def test_is_valid_name(self):
        self.assertTrue(is_valid_name("Pen"))
    
    def test_is_valid_name_error(self):
        self.assertFalse(is_valid_name(""))

    def test_normal_file(self):
        # Normal: file exists and has valid data
        with open("items.txt", "w") as f:
            f.write("Apple,10")

        try:
            view_items()
            success = True
        except:
            success = False

        self.assertTrue(success)

if __name__ == '__main__':
    unittest.main()   

    

