""" Mini task — put it all together
Write a program that:

1. Asks the user to input a category and amount
2. Saves it to expenses.csv
3. Reads the file back and prints all expenses """

import csv

# Step 1 - get input
category = input("Enter category: ")
amount = input("Enter amount: ")

# Step 2 - append to CSV
with open("expenses.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([category, amount])

print("Saved!")

# Step 3 - read and display all
with open("expenses.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    print("\nAll expenses:")
    for row in reader:
        print(f"  {row[0]}: ₦{row[1]}")