"""
Module: demo.py
Author: Group Project (Project Lead: Natalia, Core Developer: Anton, Testing & Quality Lead: Sullivan, Documentation Lead: Jay)
Description:
    1. A simple inventory management system for small businesses
    2. Supports add item, record a quantity, view inventory items and their quantities, update quantities, and save inventory data to a text file for next time use
    3. Provides a user-friendly menu for managing inventory
"""
def display_menu():
    """
    Display the main menu for the Inventory Manager.

    Parameters:
        None

    Returns:
        None

    Raises:
        None

    Example:
        >>> display_menu()

        ========== Inventory Manager ==========
        1. Add an item to inventory
        2. View all items in the inventory
        3. Change the quantity of an item
        4. Exit
        =======================================
    """
    print(f"\n{"=" * 10} Inventory Manager {"=" * 10}")   
    print("1. Add an item to inventory")
    print("2. View all items in the inventory")
    print("3. Change the quantity of an item")
    print("4. Exit")
    print("=" * 39)    # Print footer line to separate menu


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


def save_item(name, quantity):
    """
    Saves item to items.txt in append mode.

    Parameters:
        item_name (str) - name of item
        item_quantity (int) - quantity of item

    Returns: 
        None

    Raises: 
        FileNotFoundError: if items.txt/inventory does not exist

    Examples:
        >>> save_item("Apple", 10)
        Saved: Apple | Quantity: 10
    """
    try:
        with open("items.txt", "a") as file:  # Append mode preserves existing data instead of overwriting
            file.write(f"{name},{quantity}\n")
        print(f"\nSaved: {name} | Quantity: {quantity}")
    except FileNotFoundError:
        print("Failed to save item. Error: items.txt/inventory does not exist")


def view_items():
    """
    Display all items stored in items.txt.
    
    Parameters:
        None

    Returns:
        None

    Raises:
        FileNotFoundError: If the file cannot be opened or read.

    Example:
        >>> view_items()
        Inventory List:

        1 - Name: Apple | Quantity: 10
    """
    try:
        with open("items.txt", "r") as f:
            line = f.readline()

            if line == "":         # Check if file is empty
                print("There's no content in the txt.")
                return
            
            print("Inventory List:\n")

            count = 1
            while line != "":
                line = line.strip()    # Remove newline

                if line != "":    # check if the line is empty
                    parts = line.split(",")     # Split format into name and quantity as list
                    name = parts[0]
                    quantity = parts[1]

                    print(count , "-" , "Name: " , name , "| Quantity: " , quantity)
                    count += 1

                line = f.readline()
    except FileNotFoundError:
        print("The txt doesn't exist.")      # Handle when file does not exist or cannot be read


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

   
def main():  
    """
    A main loop which has a menu and controls the INventory Manager system.

    Parameters:
        None, The function is based on input
    Returns: 
        Does not return anything. Runs other methods with their information

    Raises: 
        There are no raised errors. 

    Examples:
        >>> main()
        ========== Inventory Manager ==========
        1. Add an item to inventory
        2. View all items in the inventory
        3. Change the quantity of an item
        4. Exit
        =======================================
        Choose an option: 4
        You have success exited inventory manager system!
    """
    while True:
        display_menu() # Shows the main menu
        choice = input("Choose an option: ")
        if choice == "1":
            name, quantity = add_item() # Create the item with the quantity
            save_item(name, quantity) # Saves the created item to the file
        elif choice == "2":
            view_items() # Displays all added items 
        elif choice == "3":
            view_items()
            update_quantity() # Changes the quantity of an item
        elif choice == "4":
            print("You have success exited inventory manager system!")
            break # Terminates the program
        else:
            print("Invalid choice. Try again.")

main()

main()