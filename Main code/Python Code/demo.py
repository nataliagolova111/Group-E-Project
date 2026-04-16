def display_menu():
    print(f"\n{"=" * 10} Inventory Manager {"=" * 10}")
    print("1. Add an item to inventory")
    print("2. View all items in the inventory")
    print("3. Change the quantity of an item")
    print("4. Exit")
    print("=" * 39)

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

def save_item(item_name:str, item_quantity:int):
    try:
        with open("items.txt", "a") as file:
            file.write(f"{item_name},{item_quantity}\n")
        print(f"\nSaved: {item_name} | Quantity: {item_quantity}")
        return "SUCCESS" # For testing purposes only
    except FileNotFoundError:
        print("Failed to save item. Error: items.txt/inventory does not exist")

def view_items():
    try:
        with open("items.txt", "r") as f:
            line = f.readline()

            if line == "":
                print("There's no content in the txt.")
                return
            
            print("\nInventory List:")

            count = 1
            while line != "":
                line = line.strip()

                if line != "":
                    parts = line.split(",")
                    name = parts[0]
                    quantity = parts[1]

                    print(count , "-" , "Name: " , name , "| Quantity: " , quantity)
                    count += 1

                line = f.readline()
    except:
        print("The txt doesn't exist.")

def update_quantity():
    try:
        with open("items.txt", "r") as f:
            if f.read().strip() == "":
                return # Go back to menu silently
    except FileNotFoundError:
        return
    
    item_to_change = input("Enter the name of the item to update: ")
    new_quantity = input("Enter the new quantity: ")
    
    updated_items = []
    found = False
    
    with open("items.txt", "r") as f:
        for line in f:
            name, qty = line.strip().split(",")
            if name.lower() == item_to_change.lower():
                updated_items.append(f"{name},{new_quantity}\n")
                found = True
            else:
                updated_items.append(line)
                    
    if found:
        with open("items.txt", "w") as f:
            f.writelines(updated_items)
        print("Quantity updated successfully!")
    else:
        print("Item not found.")
                 
def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            name, quantity = add_item()
            save_item(name, quantity)
        elif choice == "2":
            view_items()
        elif choice == "3":
            view_items()
            update_quantity()
        elif choice == "4":
            print("You have success exited inventory manager system!")
            break
        else:
            print("Invalid choice. Try again.")

main()