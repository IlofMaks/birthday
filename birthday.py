from datetime import datetime, timedelta, date

users = [    {'name': 'Alex', 'birthday': datetime(1994, 4, 25)},
             {'name': 'Anastasia', 'birthday': datetime(1995, 4, 26)},
             {'name': 'Elysey', 'birthday': datetime(2023, 4, 24)},
             {'name': 'Oleg', 'birthday': datetime(2018, 4, 27)},
]

def get_birthday_per_week(users):
    today = date.today()
    this_monday = today - timedelta(days=today.weekday())
    if today.weekday() >= 5:
        next_monday = this_monday + timedelta(days=7)
    else:
        next_monday = this_monday + timedelta(days=1)
    birthday_per_week = {day: [] for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']}
    for user in users:
        birthday = user['birthday'].replace(year=today.year).date()
        birthday_weekday = birthday.weekday()
        if this_monday <= birthday < next_monday:
            day_of_week = birthday.strftime('%A')
            birthday_per_week[day_of_week].append(user['name'])
        elif birthday >= next_monday:
            if birthday_weekday == 5:
                day_of_week = 'Monday'
            elif birthday_weekday == 6:
                day_of_week = 'Monday'
            else:
                day_of_week = birthday.strftime('%A')
            birthday_per_week[day_of_week].append(user['name'])
    print("Birthday list by day of the week:")
    for day, names in birthday_per_week.items():
        if names:
            print(f"{day}: {', '.join(names)}")

get_birthday_per_week(users)
