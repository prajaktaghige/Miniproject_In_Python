import json

def load_expenses():
    try:
        with open('expenses.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open('expenses.json', 'w') as f:
        json.dump(expenses, f)

def main():
    expenses = load_expenses()
    
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Quit")

        choice = input("Choose an option: ")

        if choice == '1':
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            expenses.append({'category': category, 'amount': amount})
            save_expenses(expenses)
        elif choice == '2':
            print("\nExpenses:")
            for expense in expenses:
                print(f"Category: {expense['category']}, Amount: ${expense['amount']}")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
