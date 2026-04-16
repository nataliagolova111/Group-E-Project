# Testing Plan

## Overview
**Functions tested:**  is_valid_name(name)
**Testing types:** Unit
**Date:**  16 April 2026

---

## Test Case Table

| Test ID | Description | Input(s) | Expected Output | Type | Pass/Fail | Notes |
|T1|Valid item name|"Pen"|True|Normal|Pass||
|T2|Blank string input|""|False|Error|Pass||

## Code Used for Testing

```python
def is_valid_name(name):
    if name.strip() != "" and isinstance(name,str):
        return True
    else:
        return False