import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"
FIELDS = ["date", "amount", "category", "note"]

def add_expense():
    amount = input("Amount: ₹")
    category = input("Category (e.g. Food, Travel, Rent): ")
    note = input("Note (optional): ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        if os.stat(FILENAME).st_size == 0:
            writer.writeheader()
        writer.writerow({
            "date": date,
            "amount": amount,
            "category": category,
            "note": note
        })

    print("✅ Expense added!")

def view_expenses():
    if not os.path.exists(FILENAME):
        print("No expenses found.")
        return

    with open(FILENAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['date']} | ₹{row['amount']} | {row['category']} | {row['note']}")

def total_by_category():
    if not os.path.exists(FILENAME):
        print("No expenses to calculate.")
        return

    totals = {}
    with open(FILENAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row['category']
            amount = float(row['amount'])
            totals[category] = totals.get(category, 0) + amount

    print("📊 Total Expenses by Category:")
    for cat, total in totals.items():
        print(f"{cat}: ₹{total:.2f}")

def main():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total by Category")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_by_category()
        elif choice == '4':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
