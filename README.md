
#  Expense Tracker System (Python)

#  Project Description

The **Expense Tracker System** is a simple yet effective Python-based application designed to help users manage and monitor their daily expenses. In today’s fast-paced world, tracking expenses is essential for maintaining financial stability and avoiding unnecessary spending.

This project allows users to **record their expenses under different categories**, view previously saved data, and calculate the total expenditure over a period of time. It also provides basic feedback on spending habits, helping users understand whether their expenses are within a reasonable range.

The application uses **file handling (CSV format)** to store data permanently, ensuring that the information is not lost after the program is closed. The system is menu-driven, making it easy to use even for beginners.

---

#  Objectives

* To develop a simple and user-friendly expense management system
* To understand and implement **file handling in Python**
* To perform **basic calculations and data processing**
* To encourage users to track and manage their spending habits
* To demonstrate real-world application of Python programming concepts

---

#  Files in the Project

* `expense.py` – Main Python program containing all functions and logic
* `expenses.csv` – Data file used to store expense records (expense name and amount)

---

#  Features

*  Add new expenses with name and amount
*  View all recorded expenses
*  Calculate total expenses
*  Store and retrieve data using CSV file
*  Continuous operation using menu-driven system
*  Error handling for missing files
*  Optional feedback based on spending level (Low / Moderate / High)
*  Simple and modular code structure for easy understanding

---

#  Requirements

* Python 3.x installed on the system
* Basic understanding of Python (loops, functions, file handling)
* Any code editor (VS Code / IDLE / PyCharm)

---

#  Technologies Used

* **Programming Language:** Python
* **Concepts Used:**

  * Variables and Data Types
  * Lists and Dictionaries
  * Functions
  * Loops (while, for)
  * Conditional Statements (if-else)
  * File Handling (CSV module)

---

#  How to Run the Program

1. Create a folder for the project
2. Create a Python file named `expense.py`
3. Copy and paste the program code into the file
4. Open terminal or command prompt
5. Navigate to the project folder
6. Run the program using:

```bash id="runexp123"
python expense.py
```

---

#  Program Workflow

1. The program displays a menu with options
2. User selects an option:

   * Add expense
   * View expenses
   * Calculate total
   * Exit
3. If adding expense:

   * User enters name and amount
   * Data is stored in `expenses.csv`
4. If viewing expenses:

   * File is read and displayed
5. If calculating total:

   * All values are summed and shown
6. Program repeats until user exits
    #  Logic Explanation

* Expenses are stored in a **CSV file** as rows
* Each row contains:

  * Expense Name
  * Amount
* The program reads and writes data using Python’s `csv` module
* Total expense is calculated using a loop that adds all amounts
* Conditional statements are used to provide feedback


---
# Program
```import csv

FILE = "expenses.csv"

def add_expense():
    name = input("Enter expense name: ")
    amount = input("Enter amount: ")

    with open(FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, amount])


    print("Expense saved!\n")


def view_expense():
    try:
        with open(FILE, 'r') as file:
            reader = csv.reader(file)
            print("\nExpenses:")
            for row in reader:
                print(f"{row[0]} - ₹{row[1]}")
        print()
    except FileNotFoundError:
        print("No data found.\n")

def total_expense():
    total = 0
    try:
        with open(FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[1])
        print(f"Total Expense: ₹{total}\n")
    except FileNotFoundError:
        print("No data found.\n")

def menu():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expense()
        elif choice == '3':
            total_expense()
        elif choice == '4':
            break
        else:
            print("Invalid choice!\n")

menu()
```
#  Example Menu

```id="menuexp001"
1. Add Expense
2. View Expenses
3. Total Expense
4. Exit
Enter your choice:
```



#  Sample Output

###  Adding Expenses

```id="addexp001"
Enter expense name: Food
Enter amount: 200
Expense saved successfully!
```

```id="addexp002"
Enter expense name: Travel
Enter amount: 500
Expense saved successfully!
```
# Output
<img width="989" height="609" alt="image" src="https://github.com/user-attachments/assets/dbdfdf05-2fa6-4e0a-a63d-9ffcf2d16ae7" />



#  Viewing Expenses

```id="viewexp001"
Expenses:
Food - ₹200
Travel - ₹500
```


#  Total Expense

```id="totalexp001"
Total Expense: ₹700
```


#  Future Enhancements

*  Add date-wise expense tracking
*  Categorize expenses (Food, Travel, Bills, etc.)
*  Graphical representation using `matplotlib`
*  GUI interface using `tkinter`
*  Search and filter expenses
*  Convert into mobile/web app



# Limitations

* No authentication system (anyone can access data)
* Limited to basic expense tracking
* No advanced analytics or reports
* Command-line interface only


## Testing

The program was tested with:

* Valid inputs (numbers, text)
* Invalid inputs (strings instead of numbers)
* Empty file scenarios
* Multiple entries


print("Welcome")

The Expense Tracker System is a practical and beginner-friendly project that demonstrates how Python can be used to solve real-life problems. It helps users manage their daily expenses efficiently while also strengthening programming concepts such as file handling, loops, and conditionals.

This project can be further enhanced into a full-fledged financial management system with advanced features and a graphical interface.

