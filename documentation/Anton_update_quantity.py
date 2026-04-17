def update_quantity():
    """
    Asks a user for a name of an item and new quantity

    Parameters:
        None, The function is based on inputs

    Returns: 
        Does not return anything. Only prints messages to the terminal

    Raises: 
        There are no raised errors. FileNotFoundError is handled in try-except block
        and then the user returns to the main menu.

    Examples:
        If items.txt has "Coke,10":
        >>> update_quantity()
        Enter the name of the item to update: Coke
        Enter the new quantity: 15
        Quantity updated successfully!
    """
    try: # Checks if the file exists and is not empty
        with open("items.txt", "r") as f:
            if f.read().strip() == "":
                return # Returns back to the menu
    except FileNotFoundError:
        return 
    
    item_to_change = input("Enter the name of the item to update: ")
    new_quantity = input("Enter the new quantity: ")
    
    updated_items = []
    found = False
    
    with open("items.txt", "r") as f:
        for line in f:
            name, quantity = line.strip().split(",") # Takes the name and quantity of an item
            if name.lower() == item_to_change.lower():
                updated_items.append(f"{name},{new_quantity}\n") 
                found = True # If wished item to change exists then the quantity is changed
                             # and added to the list
            else:
                updated_items.append(line) # If item does not exist then adds the original
                                           # line to the list
                    
    if found:
        with open("items.txt", "w") as f:
            f.writelines(updated_items) # Writes the list in the file
        print("Quantity updated successfully!")
    else:
        print("Item not found.")