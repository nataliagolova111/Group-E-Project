def save_item(item_name:str, item_quantity:int):
    try:
        with open("items.txt", "a") as file:
            file.write(f"{item_name},{item_quantity}\n")
        print(f"\nSaved: {item_name} | Quantity: {item_quantity}")
        return "SUCCESS" # For testing purposes only
    except FileNotFoundError:
        print("Failed to save item. Error: items.txt/inventory does not exist")