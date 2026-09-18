def show_expenses(expenses):
    print("\nYour expenses: ")

    for name, amount in expenses:
        print(f"{name}: {amount:.2f}")

expenses = []

with open("expenses.txt", "r") as file:
    for line in file:
        line = line.strip()

        if not line:
            continue

        name, amount = line.strip().split(",")
        amount = float(amount)
        expenses.append((name, amount))

while True:
    name = input("Expense name (or 'q' to quit): ")
    if name == "q":
        break

    amount = float(input("Amount: "))
    expenses.append((name, amount))

    with open("expenses.txt", "a") as file:
       file.write(f"{name}, {amount}\n")
show_expenses(expenses)

print(f"\nNumber of expenses: {len(expenses)}")
print("Thanks for using the expense tracker")
total = sum(amount for name, amount in expenses)

print(f"\nTotal spent: €{total:.2f}")

if expenses:
    average = sum(amount for _, amount in expenses)/len(expenses)
    print(f"Average expense: {average:.2f}")
