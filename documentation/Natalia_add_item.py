def is_valid_name(name):
    """
    Checks if the given item name is valid.

    Parameters:
        name (str): The name of the inventory item entered by the user.

    Returns:
        bool: True if the name is not empty or just spaces, False otherwise.

    Raises:
        AttributeError: If name is not a string and does not support the strip() method.

    Example:
        >>> is_valid_name("Pen")
        True
        >>> is_valid_name("   ")
        False
    """
    if name.strip() != "" and isinstance(name,str):     #ensures the name is meaningful and not just white spaces
        return True
    else:
        return False

def is_valid_quantity(quantity):
    """
    Checks if the given quantity is valid.

    Parameters:
        quantity (str): The quantity entered by the user.

    Returns:
        tuple and/or bool: 
            - (False, message) if invalid
            - True if valid

    Raises:
        AttributeError: If quantity is not a string and does not support the isdigit() method.

    Example:
        >>> is_valid_quantity("5")
        True
        >>> is_valid_quantity("abc")
        (False, "Quantity must be a whole number.")
    """
    if not quantity.isdigit():      #prevents non-numeric input from being converted to integer and raising an error
        return False,"Quantity must be a whole number."
    elif int(quantity) <= 0:
        return False,"Quantity must be a number greater than 0."
    else:
        return True

def add_item():
    """
    Prompts the user to enter an item name and quantity, validating both inputs.

    Parameters:
        None, The function is based on user input.

    Returns:
        tuple: The valid item name (str) and quantity (int).

    Raises:
        No possible raised errors. Invalid inputs are handled through repeating while-loop prompts.

    Example:
        >>> add_item()
        Enter item name: Pen
        Enter quantity of that item: 10
        ("Pen", 10)
    """
    while True:     #repeats until a valid, non-empty name is entered
        name = input("Enter item name: ")
        if is_valid_name(name):
            break
        else:
            print("Invalid name. Please enter a non-empty name.")
    
    while True:
        quantity = input("Enter quantity of that item: ")
        if is_valid_quantity(quantity):
            quantity = int(quantity)    #converts only after validation to avoid errors
            break
        else:
            print("Invalid quantity. Please enter a positive whole number.")

    return name,quantity