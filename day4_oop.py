import csv

class Expense:

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def __str__(self):
        return f"{self.category}: ₦{self.amount}"
        
    def to_row(self):
        return [self.category, self.amount]

def show_menu():
    print("-----Main Menu-----")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View total spent")
    print("4. Quit\n")

def  add_expense():
    try:
        with open("expense.csv", "r") as f:
            pass
    except FileNotFoundError:

        with open("expense.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(["Category","Amount"])
    while True:
        category = input("Enter Category: ").strip().capitalize()
        if category:
            break
        else:
            print("Input required...Category cannot be empty.")
    while True:
        try:
            amount = float(input("Enter expense amount: ₦"))
            break

        except ValueError:
            print("Invalid amount. Please enter a number.\n")
    new_expense = Expense(category,amount)
    with open("expense.csv", "a",newline="") as file:
        writer = csv.writer(file)

        writer.writerow(new_expense.to_row())

while True:
    show_menu()
    choice = input("Enter Choice: ")
    print()

    if choice == "1":
        add_expense()
        
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        break
    else:
        print("Enter a Valid Input 😡\n")

