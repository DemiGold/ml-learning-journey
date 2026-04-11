# Create a file and write to it
with open("expenses.txt", "w") as file:
    file.write("Food, 2500\n")
    file.write("Transport, 1000\n")
    file.write("Data, 1000\n")

print("File written successfully!\n")


# Read the entire file block
with open("expenses.txt", "r") as file:
    print(file.read())


# Add a new expense without deleting old ones
with open("expenses.txt", "a") as file:
    file.write("Rent, 15000\n")

print("Expenses added!\n")


# Read one line at a time to cleanly process the data
with open("expenses.txt", "r") as file:
    for line in file:
        print(line.strip())