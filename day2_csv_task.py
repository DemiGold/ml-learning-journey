import csv

file_name = "expenses.csv"

# 1. Input Category and Amount
category = input("Enter Category: ")
amount = int(input("Enter Amount: "))

# 2. Try opening for reading to check if file exist
try:
    with open(file_name, "r") as f:
        pass
# Catch if file is missing then create it and write headers
except FileNotFoundError:
    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Category", "Amount"])

# 3. Append the new input data
with open(file_name, "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([category, amount])
print("Saved Successfully\n")

# 4. Read the file and print out the list
print("Expenses:")
with open(file_name, "r", newline="") as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    for row in reader:
        if row:
            print(f"{row[0]}, ₦{row[1]}")