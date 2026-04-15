from jay_save_item_function import save_item
from natalia_add_item import add_item
from sullivan_view_items import view_items

def display_menu():
    print(f"\n{"=" * 10} Inventory Manager {"=" * 10}")
    print("1. Add an item to inventory")
    print("2. View all items in the inventory")
    print("3. Change the quantity of an item")
    print("4. Exit")

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
        else:
            print("Invalid choice. Try again.")

main()