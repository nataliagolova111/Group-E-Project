# Testing Plan

## Overview
**Functions tested:**  def update_quantity(item_to_change:str, new_quantity:int)
**Testing types:** Unit 
**Date:**  4/16/2026

---

## Test Case Table

| Test ID | Description | Input(s) | Expected Output | Type | Pass/Fail | Notes |
|---------|-------------|----------|-----------------|------|-----------|-------|
|T1|Test if a file is empty|("Coke", "5")|None|Edge|Pass|The test passes because when the file is empty, the try block returns None and goes back to the main menu|
---

## Code Used for Testing

```python
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