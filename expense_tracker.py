import datetime

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
today = datetime.datetime.now().strftime("%Y-%m-%d")

# Save to file
with open("expenses.txt", "a") as file:
    file.write(f"\n🗓️ {today}\n")
    for amount in expenses:
        file.write(f"₹{amount}\n")
    file.write(f"➡️ Total: ₹{total}\n")

print(f"\n✅ Total expenses today: ₹{total}")
print("💾 Saved to expenses.txt")
