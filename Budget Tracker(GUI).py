"""
Personal Budget Tracker with GUI
The Personal Budget Tracker application provides a user-friendly graphical interface to manage your financial transactions, categorize expenses, and generate detailed reports. 
Built using Python and the Tkinter library, this application offers a simple yet effective way to keep track of your income and expenses.

Features:
    Add Income: Easily record your income with the amount and a brief description.
    Add Expense: Track your expenses by specifying the amount, category, and description.
    View Transactions: Display a list of all your income and expense transactions.
    Generate Report: Get a detailed financial report that summarizes your total income, total expenses, balance, and a breakdown of expenses by category.
User Interface:
    Main Window: The main window consists of three tabs managed by a ttk.Notebook widget.
        Add Income Tab: Allows the user to input the amount and description of an income transaction.
        Add Expense Tab: Enables the user to input the amount, category, and description of an expense transaction.
        View Transactions & Report Tab: Provides buttons to view all transactions and to generate a financial report, with the output displayed in a text widget.

How to Use:
    Launching the Application: Run the script to open the main window of the budget tracker.
    Adding Income:
        Navigate to the "Add Income" tab.
        Enter the income amount and a brief description.
        Click the "Add Income" button to save the income transaction.
    Adding Expense:
        Navigate to the "Add Expense" tab.
        Enter the expense amount, category, and a brief description.
        Click the "Add Expense" button to save the expense transaction.
    Viewing Transactions:
        Navigate to the "View Transactions & Report" tab.
        Click the "View Transactions" button to display all recorded transactions in the text area.
    Generating Report:
        Navigate to the "View Transactions & Report" tab.
        Click the "View Report" button to generate and display a detailed financial report in the text area.
Code Structure:
    BudgetTracker Class: Manages the financial transactions, including adding income and expenses, and generating reports.
        Methods:
            add_income(amount, description): Adds an income transaction.
            add_expense(amount, category, description): Adds an expense transaction with a category.
            generate_report(): Generates a financial summary report.
            show_transactions(): Returns a list of all transactions.
    BudgetTrackerApp Class: Manages the Tkinter GUI, including creating the main window and handling user interactions.
        Methods:
            create_widgets(): Sets up the main interface with tabs and widgets.
            create_tab1_widgets(), create_tab2_widgets(), create_tab3_widgets(): Set up the widgets for each tab.
            add_income(), add_expense(), view_transactions(), view_report(): Handle button clicks and update the application state.
"""

import datetime
import tkinter as tk
from tkinter import ttk, messagebox

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
        transaction_list = []
        for t in self.transactions:
            date_str = t["date"].strftime("%Y-%m-%d %H:%M:%S")
            if t["type"] == "income":
                transaction_list.append(f"{date_str} - Income: ${t['amount']:.2f} - {t['description']}")
            else:
                transaction_list.append(f"{date_str} - Expense: ${t['amount']:.2f} - {t['category']} - {t['description']}")
        return transaction_list

class BudgetTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Budget Tracker")
        self.tracker = BudgetTracker()

        self.create_widgets()

    def create_widgets(self):
        # Create a notebook
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        # Add tabs
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)

        self.notebook.add(self.tab1, text="Add Income")
        self.notebook.add(self.tab2, text="Add Expense")
        self.notebook.add(self.tab3, text="View Transactions & Report")

        self.create_tab1_widgets()
        self.create_tab2_widgets()
        self.create_tab3_widgets()

    def create_tab1_widgets(self):
        # Tab 1: Add Income
        self.income_amount_label = ttk.Label(self.tab1, text="Amount:")
        self.income_amount_label.pack(pady=5)
        self.income_amount_entry = ttk.Entry(self.tab1)
        self.income_amount_entry.pack(pady=5)

        self.income_description_label = ttk.Label(self.tab1, text="Description:")
        self.income_description_label.pack(pady=5)
        self.income_description_entry = ttk.Entry(self.tab1)
        self.income_description_entry.pack(pady=5)

        self.add_income_button = ttk.Button(self.tab1, text="Add Income", command=self.add_income)
        self.add_income_button.pack(pady=10)

    def create_tab2_widgets(self):
        # Tab 2: Add Expense
        self.expense_amount_label = ttk.Label(self.tab2, text="Amount:")
        self.expense_amount_label.pack(pady=5)
        self.expense_amount_entry = ttk.Entry(self.tab2)
        self.expense_amount_entry.pack(pady=5)

        self.expense_category_label = ttk.Label(self.tab2, text="Category:")
        self.expense_category_label.pack(pady=5)
        self.expense_category_entry = ttk.Entry(self.tab2)
        self.expense_category_entry.pack(pady=5)

        self.expense_description_label = ttk.Label(self.tab2, text="Description:")
        self.expense_description_label.pack(pady=5)
        self.expense_description_entry = ttk.Entry(self.tab2)
        self.expense_description_entry.pack(pady=5)

        self.add_expense_button = ttk.Button(self.tab2, text="Add Expense", command=self.add_expense)
        self.add_expense_button.pack(pady=10)

    def create_tab3_widgets(self):
        # Tab 3: View Transactions & Report
        self.view_transactions_button = ttk.Button(self.tab3, text="View Transactions", command=self.view_transactions)
        self.view_transactions_button.pack(pady=5)

        self.view_report_button = ttk.Button(self.tab3, text="View Report", command=self.view_report)
        self.view_report_button.pack(pady=5)

        self.output_text = tk.Text(self.tab3, height=15, width=50)
        self.output_text.pack(pady=5)

    def add_income(self):
        try:
            amount = float(self.income_amount_entry.get())
            description = self.income_description_entry.get()
            self.tracker.add_income(amount, description)
            messagebox.showinfo("Success", "Income added successfully!")
            self.income_amount_entry.delete(0, tk.END)
            self.income_description_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    def add_expense(self):
        try:
            amount = float(self.expense_amount_entry.get())
            category = self.expense_category_entry.get()
            description = self.expense_description_entry.get()
            self.tracker.add_expense(amount, category, description)
            messagebox.showinfo("Success", "Expense added successfully!")
            self.expense_amount_entry.delete(0, tk.END)
            self.expense_category_entry.delete(0, tk.END)
            self.expense_description_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    def view_transactions(self):
        transactions = self.tracker.show_transactions()
        self.output_text.delete(1.0, tk.END)
        for transaction in transactions:
            self.output_text.insert(tk.END, transaction + "\n")

    def view_report(self):
        report = self.tracker.generate_report()
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, report)

def main():
    root = tk.Tk()
    app = BudgetTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
