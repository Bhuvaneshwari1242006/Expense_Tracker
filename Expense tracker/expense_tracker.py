import csv
from datetime import datetime

def add_expense():
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    date = datetime.now().strftime("%Y-%m-%d")

    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("Expense added!")

def view_expenses():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            total = 0
            print("\nDate | Category | Amount")
            print("-" * 30)

            for row in reader:
                print(row[0], "|", row[1], "|", row[2])
                total += float(row[2])

            print("\nTotal:", total)

    except FileNotFoundError:
        print("No data found")

while True:
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        break
    else:
        print("Invalid choice")