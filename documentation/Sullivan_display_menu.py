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