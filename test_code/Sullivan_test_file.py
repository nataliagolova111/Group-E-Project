import unittest

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


class TestViewItems(unittest.TestCase):

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