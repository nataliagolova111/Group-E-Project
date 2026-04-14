def view_items():
    try:
        with open("items.txt", "r") as f:
            lines = f.readlines()
    except:
        print("The txt doesn't exit.")
        return

    if len(lines) == 0:
        print("There's no content in the txt.")
        return

    print("Inventory List:\n")

    count = 1
    for line in lines:
        line = line.strip()

        if line != "":
            parts = line.split(",")
            name = parts[0]
            quantity = parts[1]

            print(count, "-","Name : " ,name, "| Quantity : ", quantity)
            count += 1