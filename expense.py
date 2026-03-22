#!/usr/bin/env python
# coding: utf-8

# In[5]:


from google.colab import files
uploaded = files.upload()


# In[ ]:


import csv

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

