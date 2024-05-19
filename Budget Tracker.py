"""
Created By Anthony -- 5/18/2024 
https://github.com/Wazupbutrcup

This application will allow you to:

Add income and expenses.
Categorize expenses.
Generate reports of your financial status.
"""

"""
BudgetTracker class: Manages transactions including incomes and expenses, and generates financial reports.

add_income: Adds an income transaction.
add_expense: Adds an expense transaction with a category.
generate_report: Summarizes total income, total expenses, and balance, and breaks down expenses by category.
show_transactions: Displays all transactions.
main function: Provides a simple menu-driven interface for the user to interact with the budget tracker.
"""

import datetime

class BudgetTracker:
    def __init__(self):
        self.transactions = []

    def add_income(self, amount, description=""):
        self.transactions.append({
            "type": "income",
            "amount": amount,
            "description": description,
            "date": datetime.datetime.now()
        })

    def add_expense(self, amount, category, description=""):
        self.transactions.append({
            "type": "expense",
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.datetime.now()
        })

    def generate_report(self):
        total_income = sum(t["amount"] for t in self.transactions if t["type"] == "income")
        total_expense = sum(t["amount"] for t in self.transactions if t["type"] == "expense")
        balance = total_income - total_expense

        report = f"Report as of {datetime.datetime.now()}\n"
        report += f"Total Income: ${total_income:.2f}\n"
        report += f"Total Expense: ${total_expense:.2f}\n"
        report += f"Balance: ${balance:.2f}\n\n"
        report += "Expenses by Category:\n"

        categories = {}
        for t in self.transactions:
            if t["type"] == "expense":
                if t["category"] not in categories:
                    categories[t["category"]] = 0
                categories[t["category"]] += t["amount"]

        for category, amount in categories.items():
            report += f"  {category}: ${amount:.2f}\n"

        return report

    def show_transactions(self):
        for t in self.transactions:
            date_str = t["date"].strftime("%Y-%m-%d %H:%M:%S")
            if t["type"] == "income":
                print(f"{date_str} - Income: ${t['amount']:.2f} - {t['description']}")
            else:
                print(f"{date_str} - Expense: ${t['amount']:.2f} - {t['category']} - {t['description']}")

def main():
    tracker = BudgetTracker()
    
    while True:
        print("\nPersonal Budget Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Generate Report")
        print("4. Show Transactions")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter income amount: "))
            description = input("Enter income description: ")
            tracker.add_income(amount, description)
            print("Income added.")
        elif choice == "2":
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            description = input("Enter expense description: ")
            tracker.add_expense(amount, category, description)
            print("Expense added.")
        elif choice == "3":
            print(tracker.generate_report())
        elif choice == "4":
            tracker.show_transactions()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
