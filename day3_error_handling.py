import csv

def load_expenses():
    try:
        with open("expenses.csv", "r") as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            expenses = [row for row in reader]
            return expenses
    except FileNotFoundError:
        print("No expenses file found. Starting fresh.")
        return []

expenses = load_expenses()
print(expenses)