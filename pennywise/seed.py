import lib.helpers as helpers

sample_budgets = [
    ("Food", 200),
    ("Rent", 1000),
    ("Transport", 150),
]

sample_transactions = [
    (50, "Food", "2025-05-28", "expense"),
    (1200, "Salary", "2025-05-25", "income"),
    (70, "Transport", "2025-05-26", "expense"),
]

def seed_data():
    print(" Seeding data...")

    for category, limit in sample_budgets:
        helpers.add_budget(category, limit)
        print(f" Budget added: {category} - ${limit}")

    for transaction in sample_transactions:
        helpers.add_transaction(*transaction)
        print(f" Transaction added: {transaction[2]} - ${transaction[0]} ({transaction[1]})")

    print(" Sample data successfully seeded!")

if __name__ == "__main__":
    seed_data()