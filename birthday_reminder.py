import datetime

birthdays = {
    "Tarun Sai": "06-29",
    "Anna": "12-05",
    "Tarun": "11-01"
}

today = datetime.datetime.now().strftime("%m-%d")

for name, bday in birthdays.items():
    if bday == today:
        print(f"🎉 Today is {name}'s birthday!")
