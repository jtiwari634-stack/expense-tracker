import json
import os
from datetime import datetime


# Load existing expenses
if os.path.exists("expenses.json"):
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
else:
    expenses = []


def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense():
    expense_name = input("What did you spend on? ")

    try:
        amount = float(input("How much did you spend? "))

        if amount < 0:
            print("\nAmount cannot be negative!")
            return

        category = input("What category is this? ")

        expense_date = datetime.now().strftime("%d-%m-%Y")

        expenses.append([
            expense_name,
            amount,
            category,
            expense_date
        ])

        save_expenses()

        print("\nExpense added!")
        print("Item:", expense_name)
        print("Amount: ₹", amount)
        print("Category:", category)
        print("Date:", expense_date)

    except ValueError:
        print("\nPlease enter a valid number!")


def view_expenses():
    print("\n===== YOUR EXPENSES =====")

    if len(expenses) == 0:
        print("No expenses found.")
        return

    for i, expense in enumerate(expenses, start=1):

        if len(expense) >= 4:
            category = expense[2]
            expense_date = expense[3]

        elif len(expense) >= 3:
            category = expense[2]
            expense_date = "Unknown"

        else:
            category = "Other"
            expense_date = "Unknown"

        print(
            f"{i}. {expense[0]} - "
            f"₹{expense[1]:.2f} - "
            f"{category} - "
            f"{expense_date}"
        )


def total_spending():
    total = 0

    for expense in expenses:
        total = total + expense[1]

    print("\n===== TOTAL SPENDING =====")
    print(f"Total: ₹{total:.2f}")


def delete_expense():
    if len(expenses) == 0:
        print("\nNo expenses to delete.")
        return

    print("\n===== YOUR EXPENSES =====")

    for i, expense in enumerate(expenses, start=1):

        if len(expense) >= 4:
            category = expense[2]
            expense_date = expense[3]

        elif len(expense) >= 3:
            category = expense[2]
            expense_date = "Unknown"

        else:
            category = "Other"
            expense_date = "Unknown"

        print(
            f"{i}. {expense[0]} - "
            f"₹{expense[1]:.2f} - "
            f"{category} - "
            f"{expense_date}"
        )

    try:
        number = int(
            input("\nEnter expense number to delete: ")
        )

        if number >= 1 and number <= len(expenses):

            deleted_expense = expenses.pop(number - 1)

            save_expenses()

            print(
                f"\nDeleted: "
                f"{deleted_expense[0]} - "
                f"₹{deleted_expense[1]:.2f}"
            )

        else:
            print("\nInvalid expense number!")

    except ValueError:
        print("\nPlease enter a valid number!")


def spending_by_category():
    category_totals = {}

    for expense in expenses:

        if len(expense) >= 3:
            category = expense[2]
        else:
            category = "Other"

        amount = expense[1]

        if category in category_totals:
            category_totals[category] = (
                category_totals[category] + amount
            )
        else:
            category_totals[category] = amount

    print("\n===== SPENDING BY CATEGORY =====")

    if len(category_totals) == 0:
        print("No expenses found.")
        return

    for category, total in category_totals.items():
        print(f"{category}: ₹{total:.2f}")


def expenses_by_date():
    search_date = input("Enter date (DD-MM-YYYY): ")

    print("\n===== EXPENSES ON", search_date, "=====")

    found = False

    for i, expense in enumerate(expenses, start=1):

        if len(expense) >= 4:

            expense_date = expense[3]
            category = expense[2]

            if expense_date == search_date:

                print(
                    f"{i}. {expense[0]} - "
                    f"₹{expense[1]:.2f} - "
                    f"{category} - "
                    f"{expense_date}"
                )

                found = True

    if found == False:
        print("No expenses found for this date.")


def search_expense():
    search_name = input(
        "Enter expense name to search: "
    ).lower()

    found = False

    print("\n===== SEARCH RESULTS =====")

    for i, expense in enumerate(expenses, start=1):

        expense_name = expense[0].lower()

        if search_name in expense_name:

            if len(expense) >= 4:
                category = expense[2]
                expense_date = expense[3]

            elif len(expense) >= 3:
                category = expense[2]
                expense_date = "Unknown"

            else:
                category = "Other"
                expense_date = "Unknown"

            print(
                f"{i}. {expense[0]} - "
                f"₹{expense[1]:.2f} - "
                f"{category} - "
                f"{expense_date}"
            )

            found = True

    if found == False:
        print("No matching expenses found.")


# Main Menu
while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Exit")
    print("5. Delete Expense")
    print("6. Spending by Category")
    print("7. View Expenses by Date")
    print("8. Search Expense")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_spending()

    elif choice == "4":
        print("Goodbye!")
        break

    elif choice == "5":
        delete_expense()

    elif choice == "6":
        spending_by_category()

    elif choice == "7":
        expenses_by_date()

    elif choice == "8":
        search_expense()

    else:
        print("Invalid choice!")