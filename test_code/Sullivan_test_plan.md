# Testing Plan

## Overview
**Functions tested:**  view_items()
**Testing types:** Unit
**Date:**  04/16/2026

---

## Test Case Table

| Test ID | Description | Input | Expected Output | Type | Pass/Fail | Notes |
| T1 | Viewing item from a normal file | items.txt contains "Apple,10" | True |Normal | Uses assertTrue to confirm |

---

## Code Used for Testing

```python
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