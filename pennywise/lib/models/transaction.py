import sqlite3

class Transaction:
    def __init__(self, amount, category, date, type, budget_id=None):
        self.amount = amount
        self.category = category
        self.date = date
        self.type = type
        self.budget_id = budget_id

    @staticmethod
    def create_table():
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            type TEXT NOT NULL CHECK(type IN ('income', 'expense')),
            budget_id INTEGER,
            FOREIGN KEY (budget_id) REFERENCES budgets(id)
        )
        """)
        conn.commit()
        conn.close()

    def save(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO transactions (amount, category, date, type, budget_id) VALUES (?, ?, ?, ?, ?)",
                       (self.amount, self.category, self.date, self.type, self.budget_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM transactions")
        transactions = cursor.fetchall()
        conn.close()
        return transactions