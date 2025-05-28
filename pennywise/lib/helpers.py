import sqlite3

DB_NAME = "database.db"

def connect_db():
    return sqlite3.connect(DB_NAME)

def add_transaction(amount, category, date, type, budget_id=None):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (amount, category, date, type, budget_id) VALUES (?, ?, ?, ?, ?)",
                   (amount, category, date, type, budget_id))
    conn.commit()
    conn.close()

def get_all_transactions():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()
    conn.close()
    return transactions

def add_budget(category, limit):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO budgets (category, limit) VALUES (?, ?)", (category, limit))
    conn.commit()
    conn.close()

def get_all_budgets():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM budgets")
    budgets = cursor.fetchall()
    conn.close()
    return budgets