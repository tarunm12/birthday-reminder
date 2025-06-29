expenses = []

print("💰 Daily Expense Tracker")
print("Enter your expenses one by one.")
print("Type 'done' when finished.\n")

while True:
    entry = input("Enter expense amount: ₹")
    if entry.lower() == "done":
        break
    try:
        expenses.append(float(entry))
    except ValueError:
        print("❌ Please enter a number or 'done' to finish.")

total = sum(expenses)
print(f"\n✅ Total expenses today: ₹{total}")
