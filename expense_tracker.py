import csv

def add_expense():
    # keep asking until category isn't empty
    while True:
        category = input("Enter Category: ").strip()
        if category:
            break
        print("Input Required...Category cannot be empty.")

    # keep asking until a valid number is entered
    while True:
        try:
            amount = int(input("Enter Amount: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    # write header only if file doesn't exist yet
    try:
        with open("expenses.csv", "r", newline="") as file:
            pass
    except FileNotFoundError:
        with open("expenses.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Category", "Amount"])

    # append new expense
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([category, amount])

def show_menu():
    print("-----Main Menu-----")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View total spent")
    print("4. Quit")
    print()

while True:
    show_menu()
    choice = input("Enter Choice: ").strip()

    if choice == "1":
        add_expense()
        print("Saved Successfully ✅\n")

    elif choice == "2":
        try:
            with open("expenses.csv", "r", newline="") as file:
                reader = csv.reader(file)
                next(reader)  # skip header
                for row in reader:
                    print(f"Category: {row[0]}, Amount: {row[1]}")
        except FileNotFoundError:
            print("No expenses recorded yet.\n")
    elif choice == "3":
        pass

    elif choice == "4":
        break

    else:
        print("Enter a Valid Input 😡\n")