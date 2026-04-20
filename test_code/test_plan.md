# Testing Plan

## Overview
**Functions tested:**  view_items() , save_item(item_name, item_quantity) , is_valid_name(name) , update_quantity(item_to_change:str, new_quantity:int)
**Testing types:** Unit
**Date:**  04/16/2026

---

## Test Case Table

| Test ID | Description | Input(s) | Expected Output | Type | Pass/Fail | Notes |
|---------|-------------|----------|-----------------|------|-----------|-------|
|T1|Saving a normal valid item|item_name="Apple", item_quantity=10|"SUCCESS"|Normal|Pass|Basic successful save in items.txt|
|T2|Quantity given as string|item_name="Orange", item_quantity=Two|TypeError|Error|Fail|This currently crashes as code does not yet handle the error case|
|T3|Valid item name|"Pen"|True|Normal|Pass||
|T4|Blank string input|""|False|Error|Pass||
|T5|Viewing item from a normal file|"Apple,10"|True|Normal|Uses assertTrue to confirm|
|T6|Test if a file is empty|("Coke", "5")|None|Edge|Pass|The test passes because when the file is empty, the try block returns None and goes back to the main menu|

---

## Code Used for Testing

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

def update_quantity(item_to_change:str, new_quantity:int):
    try:
        with open("Anton_test_items.txt", "r") as f:
            if f.read().strip() == "":
                return None # only for testing purposes, but there is actually None
                            # even without typing it
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