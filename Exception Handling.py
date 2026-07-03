try:
    filename = input("Enter the file name: ") + ".txt"

    with open(filename, "r") as file:
        lines = file.readlines()

    items = 0
    free_items = 0
    amount = 0
    discount = 0

    for line in lines:
        line = line.strip()

        if line == "":
            continue

        parts = line.split()

        if parts[0].lower() == "discount":
            discount = int(parts[1])
        else:
            items += 1
            if parts[1].lower() == "free":
                free_items += 1
            else:
                amount += int(parts[1])

    print("No of items purchased:", items)
    print("No of free items:", free_items)
    print("Amount to pay:", amount)
    print("Discount given:", discount)
    print("Final amount paid:", amount - discount)

except FileNotFoundError:
    print("File not found")

except Exception as e:
    print("Error:", e)


#SampleOutput:
Enter the file name: Purchase-1
No of items purchased: 3
No of free items: 0
Amount to pay: 135
Discount given: 5
Final amount paid: 130

#SampleOutput:
Enter the file name: Purchase-1
No of items purchased: 5
No of free items: 2
Amount to pay: 485
Discount given: 80
Final amount paid: 405