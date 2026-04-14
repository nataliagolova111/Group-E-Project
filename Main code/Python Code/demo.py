from jay_save_item_function import save_item

def display_menu():
    print(f"{"=" * 10} Inventory Manager {"=" * 10}")
    print("1. Add an item to inventory")
    print("2. View all items in the inventory")
    print("3. Change the quantity of an item")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            pass
        elif choice == "2":
            save_item()
        elif choice == "3":
            pass
        else:
            print("Invalid choice. Try again.")

main()