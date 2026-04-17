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