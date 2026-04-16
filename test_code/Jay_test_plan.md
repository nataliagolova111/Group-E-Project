# Testing Plan

## Overview
**Functions tested:**  save_item(item_name, item_quantity)
**Testing types:** Unit
**Date:**  04/16/2026

---

## Test Case Table

| Test ID | Description | Input(s) | Expected Output | Type | Pass/Fail | Notes |
|---------|-------------|----------|-----------------|------|-----------|-------|
|T1|Saving a normal valid item|item_name="Apple", item_quantity=10|"SUCCESS"|Normal|Pass|Basic successful save in items.txt|
|T2|Quantity given as string|item_name="Orange", item_quantity=Two|TypeError|Error|Fail|This currently crashes as code does not yet handle the error case|
---

## Code Used for Testing

```python
def save_item(item_name:str, item_quantity:int):
    try:
        with open("items.txt", "a") as file:
            file.write(f"{item_name},{item_quantity}\n")
        print(f"\nSaved: {item_name} | Quantity: {item_quantity}")
        return "SUCCESS" # For testing purposes only
    except FileNotFoundError:
        print("Failed to save item. Error: items.txt/inventory does not exist")