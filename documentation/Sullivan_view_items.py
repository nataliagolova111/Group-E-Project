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