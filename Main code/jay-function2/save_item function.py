def save_item(item_name:str, item_quantity:int):
    try:
        with open("items.txt", "a") as file:
            file.write(f"{item_name},{item_quantity}\n")
        print(f"Saved: {item_name} | Quantity: {item_quantity}")
    except FileNotFoundError:
        print("Failed to save item. Error: items.txt/inventory does not exist")