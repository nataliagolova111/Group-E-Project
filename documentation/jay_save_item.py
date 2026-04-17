def save_item(item_name: str, item_quantity: int):
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
            file.write(f"{item_name},{item_quantity}\n")
        print(f"\nSaved: {item_name} | Quantity: {item_quantity}")
    except FileNotFoundError:
        print("Failed to save item. Error: items.txt/inventory does not exist")
