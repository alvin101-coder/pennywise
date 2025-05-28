import lib.helpers as helpers

def debug():
    print(" Debugging Pennywise...")

    print("\n Existing Budgets:")
    budgets = helpers.get_all_budgets()
    for b in budgets:
        print(f"Category: {b[1]}, Limit: ${b[2]}")

    print("\n Existing Transactions:")
    transactions = helpers.get_all_transactions()
    for t in transactions:
        print(f"ID: {t[0]}, {t[4].upper()} - {t[2]}: ${t[1]} on {t[3]}")

if __name__ == "__main__":
    debug()