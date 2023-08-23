from datetime import datetime, timedelta

def get_birthdays_per_week(users: list) -> None:
    current_date = datetime.now()
    days = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday" ]
    birth_days_list = []

    for i in range(0, 7):
        date = current_date + timedelta(days= i)
        if date.weekday() == 5:
            date = current_date + timedelta(days= i + 2)
        if date.weekday() == 6:
            date = current_date + timedelta(days= i + 1)
        
        day = date.day
        if not next((item for item in birth_days_list if item["day"] == date.day), None):        
            birth_days_list.append({ "day": date.day, "month": date.month, "weekday": days[date.weekday()], "list": [] })

    for user in users:
        birth_day = datetime(year=current_date.year, month=user["birthday"].month, day=user["birthday"].day)
        delta = birth_day - current_date
        if -2 <= delta.days <= 7:
            wd = birth_day.weekday()
            age = current_date.year - user["birthday"].year
            string = f"{user['name']} ({age} years)"
            index = None
            if wd in [0, 5, 6] or ((wd == -1 or wd == -2) and current_date.weekday == 0):
                index = 0
            elif wd not in [ -1, -2 ]: 
                index = wd
            if index != None:
                birth_days_list[index]["list"].append(string)

    for item in birth_days_list:
        if len(item["list"]):
            print(f"{item['day']}.{item['month']} {item['weekday']}: {', '.join(item['list'])}")