def is_valid_name(name):
    if name.strip() != "" and isinstance(name,str):
        return True
    else:
        return False

def is_valid_quantity(quantity):
    if not quantity.isdigit():
        return False,"Quantity must be a whole number."
    elif int(quantity) <= 0:
        return False,"Quantity must be a number greater than 0."
    else:
        return True

def add_item():
    while True:
        name = input("Enter item name: ")
        if is_valid_name(name):
            break
        else:
            print("Invalid name. Please enter a non-empty name.")
    
    while True:
        quantity = input("Enter quantity of that item: ")
        if is_valid_quantity(quantity):
            quantity = int(quantity)
            break
        else:
            print("Invalid quantity. Please enter a positive whole number.")

    return name,quantity

add_item()