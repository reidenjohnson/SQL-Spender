# Overview

SQL Spender is a straightforward expense tracker that records, edits, and summarizes personal spending.  
The software demonstrates how a Python program can interact with a SQL relational database using the built-in `sqlite3` library.  
Users can add, view, update, and delete expense entries, and view a spending summary by category that uses aggregate SQL functions. All of which is then saved locally to the database file it created.  

The purpose of writing this software was to gain hands-on experience with building and managing a relational database through code rather than manual SQL tools. This project helped solidify concepts of data persistence, CRUD operations, and query aggregation.

[Software Demo Video](https://youtu.be/Os9SgJy4nCw)

# Relational Database

The program automatically generates the database and table if they do not already exist. 
It uses SQLite to connect Python with SQL commands, storing and updating data directly within the table and database.

| Column | Type | Description |
|---------|------|-------------|
| id | INTEGER (Primary Key) | Unique identifier for each record |
| date | TEXT | Date of the expense in YYYY-MM-DD format |
| category | TEXT | Expense category such as Food, Fuel, or Rent |
| amount | REAL | Numeric cost of the expense |
| description | TEXT | Optional notes about the purchase |
 
It demonstrates the ability to:
- **Insert** new records  
- **Retrieve** all records  
- **Modify** existing records  
- **Delete** records  
- Perform a **GROUP BY** query using `COUNT()` and `SUM()` to summarize expenses by category

# Development Environment

- **IDE / Editor:** Visual Studio Code  
- **Programming Language:** Python 3.13.7
- **Database Engine:** SQLite (via the `sqlite3` standard library)  

# Useful Websites

- [W3Schools – SQL Tutorial](https://www.w3schools.com/sql/)  
- [Python sqlite3 Documentation](https://docs.python.org/3/library/sqlite3.html)  
- [SQLite Tutorial](https://www.sqlitetutorial.net/)  
- [GeeksforGeeks – CRUD Operations in SQLite with Python](https://www.geeksforgeeks.org/python-sqlite/)

# Future Work

- Create a simple GUI interface for easier use
- Add date-range filtering for expense queries  
- Export data to CSV or Excel format  

