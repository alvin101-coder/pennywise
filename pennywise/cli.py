import lib.helpers as helpers

def main():
    while True:
        print("\n Pennywise - Personal Finance Tracker")
        print("1. Add a transaction")
        print("2. View all transactions")
        print("3. Set a budget")
        print("4. View budgets")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            date = input("Enter date (YYYY-MM-DD): ")
            type = input("Enter type (income/expense): ")
            budget_id = None
            helpers.add_transaction(amount, category, date, type, budget_id)
            print(" Transaction added successfully!")
        elif choice == "2":
            transactions = helpers.get_all_transactions()
            for t in transactions:
                print(f"ID: {t[0]}, {t[4].upper()} - {t[2]}: ${t[1]} on {t[3]}")
        elif choice == "3":
            category = input("Enter budget category: ")
            limit = float(input("Set spending limit: "))
            helpers.add_budget(category, limit)
            print(f" Budget set for {category}: ${limit}")
        elif choice == "4":
            budgets = helpers.get_all_budgets()
            for b in budgets:
                print(f" {b[1]} - Limit: ${b[2]}")
        elif choice == "5":
            print(" Exiting... See you next time!")
            break
        else:
            print(" Invalid choice, try again!")

if __name__ == "__main__":
    main()