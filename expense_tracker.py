def show_expenses(expenses):
    print("\nYour expenses: ")

    for name, amount in expenses:
        print(f"{name}: {amount:.2f}")

expenses = []

while True:
    name = input("Expense name (or 'q' to quit): ")
    if name == "q":
        break

    amount = float(input("Amount: "))
    expenses.append((name, amount))

show_expenses(expenses)

total = sum(amount for name, amount in expenses)

print(f"\nTotal: €{total:.2f}")