import sqlite3

class Budget:
    def __init__(self, category, limit):
        self.category = category
        self.limit = limit

    @staticmethod
    def create_table():
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS budgets (
            id INTEGER PRIMARY KEY,
            category TEXT UNIQUE NOT NULL,
            limit REAL NOT NULL
        )
        """)
        conn.commit()
        conn.close()

    def save(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO budgets (category, limit) VALUES (?, ?)", (self.category, self.limit))
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
