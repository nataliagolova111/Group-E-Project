def view_items():
    """
    Display all items stored in items.txt.
    
    Parameters:
        None

    Returns:
        None

    Raises:
        Exception: If the file cannot be opened or read.

    Example:
        >>> view_items()
        Inventory List:

        1 - Name: Apple | Quantity: 10
    """

    try:
        with open("items.txt", "r") as f:
            line = f.readline()

            if line == "":
                print("There's no content in the txt.")
                return
            
            print("Inventory List:\n")

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