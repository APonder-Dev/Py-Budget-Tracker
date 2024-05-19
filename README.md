# Personal Budget Tracker

A simple Python application to track your income and expenses, with features for categorizing expenses and generating reports. This application is available in both command-line and graphical user interface (GUI) versions.

## Features
- Add income transactions
- Add expense transactions with categories
- View all transactions
- Generate financial reports summarizing income, expenses, and balance
- Categorized expense summary in the report

## Requirements
- Python 3.x
- Tkinter (for the GUI version)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/personal-budget-tracker.git
    cd personal-budget-tracker
    ```

2. Install Tkinter if not already installed:
    ```bash
    # On Debian-based systems (e.g., Ubuntu)
    sudo apt-get install python3-tk

    # On macOS
    brew install python-tk

    # On Windows, Tkinter is usually included with Python installation
    ```

## Usage

### Command-line Version
1. Run the script:
    ```bash
    python budget_tracker_cli.py
    ```

2. Follow the prompts to add income, add expenses, view transactions, and generate reports.

### GUI Version
1. Run the script:
    ```bash
    python budget_tracker_gui.py
    ```

2. Use the graphical interface to interact with the application:
    - **Add Income**: Enter the amount and description, then click "Add Income".
    - **Add Expense**: Enter the amount, category, and description, then click "Add Expense".
    - **View Transactions**: Click "View Transactions" to display all recorded transactions.
    - **Generate Report**: Click "View Report" to display a detailed financial report.

## File Structure
```
personal-budget-tracker/
│
├── budget_tracker_cli.py     # Command-line version of the budget tracker
├── budget_tracker_gui.py     # GUI version of the budget tracker using Tkinter
└── README.md                 # This README file
```

## Examples

### Command-line Version
```yaml
Personal Budget Tracker
1. Add Income
2. Add Expense
3. Generate Report
4. Show Transactions
5. Exit
Choose an option: 1
Enter income amount: 5000
Enter income description: Salary
Income added.

Choose an option: 2
Enter expense amount: 150
Enter expense category: Groceries
Enter expense description: Weekly shopping
Expense added.

Choose an option: 3
Report as of 2024-05-18 10:30:00
Total Income: $5000.00
Total Expense: $150.00
Balance: $4850.00

Expenses by Category:
  Groceries: $150.00
```

### GUI Version
1. **Add Income Tab**:
    - Enter the amount and description, then click "Add Income".
    - A success message will appear confirming the addition.

2. **Add Expense Tab**:
    - Enter the amount, category, and description, then click "Add Expense".
    - A success message will appear confirming the addition.

3. **View Transactions & Report Tab**:
    - Click "View Transactions" to display all recorded transactions in the text area.
    - Click "View Report" to generate and display a detailed financial report in the text area.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or suggestions, please open an issue on the GitHub repository.

---

### Notes:
- Replace `your-username` in the clone URL with your actual GitHub username if you plan to host this on GitHub.
- Ensure that the file names (`Budget Tracker.py` and `Budget Tracker(GUI).py`) match the actual file names you have used in your project. If they are different, update the README accordingly.
- Include the `LICENSE` file in your repository if you choose to specify a license.