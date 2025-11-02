# Project: SQL Spender (Expense Tracker)
# Author:  Reiden Johnson


# Import the built-in SQLite3 library
import sqlite3


# ======================================================
#                  DATABASE SETUP
# ======================================================

# Connect to the SQLite database file
# If the file doesn't exist, it will automatically be created
conn = sqlite3.connect("expenses.db")

# Create a cursor object that allows you to send SQL commands to the database
cursor = conn.cursor()

# Each expense record will include an ID, date, category, amount, and description
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    category TEXT NOT NULL,
    amount REAL NOT NULL,
    description TEXT
);
""")
conn.commit()  # Save changes to the database


# ======================================================
#                 ADD NEW EXPENSE
# ======================================================

def add_expense():
    # Demonstrates the SQL INSERT command.
   

    # Collect input values from the user
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g. Food, Fuel, Rent): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    # Insert the data into the table using a SQL query
    # The '?' placeholders help prevent SQL injection vulnerabilities
    cursor.execute(
        "INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
        (date, category, amount, description)
    )

    conn.commit()  # Save the new record
    print("Expense added successfully!\n")


# ======================================================
#                 VIEW ALL EXPENSES
# ======================================================

def view_expenses():
    
    # Run a SELECT query to fetch all rows
    cursor.execute("SELECT * FROM expenses")
    records = cursor.fetchall()

    # If there are no results, tell the user
    if not records:
        print("No expenses recorded yet.\n")
        return

    # Print the table 
    print("\nID | Date       | Category  | Amount  | Description")
    print("-" * 55)

    # row[0] = id, row[1] = date, row[2] = category, row[3] = amount, row[4] = description
    for row in records:
        print(f"{row[0]:<2} | {row[1]:<10} | {row[2]:<9} | ${row[3]:<7.2f} | {row[4]}")
    print()


# ======================================================
#               UPDATE EXISTING EXPENSE
# ======================================================

def update_expense():

    # Demonstrates the SQL UPDATE command.

    # Show all current records so the user can pick one to modify
    view_expenses()
    expense_id = input("Enter the ID of the expense to update: ")

    # Check if the selected expense exists
    cursor.execute("SELECT * FROM expenses WHERE id = ?", (expense_id,))
    record = cursor.fetchone()
    if not record:
        print("Expense not found.\n")
        return

    # Let the user update one or more fields
    # Leaving a field blank keeps its previous value
    print("Leave field blank to keep current value.")
    new_date = input(f"New date [{record[1]}]: ") or record[1]
    new_category = input(f"New category [{record[2]}]: ") or record[2]
    new_amount = input(f"New amount [{record[3]}]: ") or record[3]
    new_description = input(f"New description [{record[4]}]: ") or record[4]

    # Run the SQL UPDATE command
    cursor.execute("""
        UPDATE expenses
        SET date = ?, category = ?, amount = ?, description = ?
        WHERE id = ?
    """, (new_date, new_category, float(new_amount), new_description, expense_id))

    conn.commit()  # Save changes
    print("Expense updated successfully!\n")


# ======================================================
#                 DELETE AN EXPENSE
# ======================================================

def delete_expense():

    # Demonstrates the SQL DELETE command.

    # Show current data for reference
    view_expenses()
    expense_id = input("Enter the ID of the expense to delete: ")

    # Run the SQL DELETE command
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()

    # Check whether the row existed and was deleted
    if cursor.rowcount == 0:
        print("Expense not found.\n")
    else:
        print("Expense deleted successfully!\n")


# ======================================================
#              VIEW SUMMARY (Aggregates)
# ======================================================

def view_summary():
  
    # Demonstrates the SQL GROUP BY clause and
    # uses two aggregate functions: COUNT() and SUM().

    cursor.execute("""
        SELECT category, COUNT(*) AS count, SUM(amount) AS total
        FROM expenses
        GROUP BY category
    """)
    records = cursor.fetchall()

    if not records:
        print("No data available for summary.\n")
        return

    print("\nCategory Summary")
    print("-----------------------------")
    print("Category | Count | Total ($)")
    print("-----------------------------")

    # Each row now contains the category name, number of expenses, and total sum
    for row in records:
        print(f"{row[0]:<9} | {row[1]:<5} | ${row[2]:<8.2f}")
    print()


# ======================================================
#                   MAIN MENU LOOP
# ======================================================

def main():
    
    # Displays a menu, receives input, and calls the appropriate function.


    print("=======================================")
    print("     Welcome to SQLSpender Tracker     ")
    print("=======================================")

    while True:
        # Show the main menu options
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. View Summary (by Category)")
        print("6. Exit")

        # Collect the user’s choice
        choice = input("Select an option (1-6): ")
        print()

        # Match the user’s input to the right function
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            update_expense()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            view_summary()
        elif choice == "6":
            # Exit the loop and close the program
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid selection. Try again.\n")

    # Once the user exits, close the database connection
    conn.close()


# ======================================================
#                  PROGRAM ENTRY POINT
# ======================================================

# This makes sure the program only runs when executed directly,
# and not when imported into a different script

if __name__ == "__main__":
    main()
