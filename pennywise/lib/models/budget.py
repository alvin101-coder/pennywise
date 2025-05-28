import sqlite3

class Budget:
    def __init__(self, category, spending_limit):
        self.category = category
        self.spending_limit = spending_limit

    @staticmethod
    def create_table():
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS budgets (
            id INTEGER PRIMARY KEY,
            category TEXT UNIQUE NOT NULL,
            spending_limit REAL NOT NULL
        )
        """)
        conn.commit()
        conn.close()

    def save(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO budgets (category, spending_limit) VALUES (?, ?)", (self.category, self.spending_limit))
        conn.commit()
        conn.close()
    
    @staticmethod
    def get_all():
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM budgets")
        budgets = cursor.fetchall()
        conn.close()
        return budgets