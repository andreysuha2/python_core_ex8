from datetime import datetime
import pprint
import random

NAMES = [ "Ben", "Bill", "John", "Ann" ]

USERS = [   {'birthday': datetime(1975, 5, 3, 0, 0), 'name': 'Ben 0'},
    {'birthday': datetime(1991, 9, 9, 0, 0), 'name': 'Bill 0'},
    {'birthday': datetime(1995, 6, 3, 0, 0), 'name': 'John 0'},
    {'birthday': datetime(1952, 2, 3, 0, 0), 'name': 'Ann 0'},
    {'birthday': datetime(1968, 12, 23, 0, 0), 'name': 'Ben 1'},
    {'birthday': datetime(1956, 1, 3, 0, 0), 'name': 'Bill 1'},
    {'birthday': datetime(2000, 5, 17, 0, 0), 'name': 'John 1'},
    {'birthday': datetime(1973, 10, 3, 0, 0), 'name': 'Ann 1'},
    {'birthday': datetime(1962, 12, 12, 0, 0), 'name': 'Ben 2'},
    {'birthday': datetime(1991, 3, 28, 0, 0), 'name': 'Bill 2'},
    {'birthday': datetime(1967, 3, 15, 0, 0), 'name': 'John 2'},
    {'birthday': datetime(1955, 10, 11, 0, 0), 'name': 'Ann 2'},
    {'birthday': datetime(1990, 11, 3, 0, 0), 'name': 'Ben 3'},
    {'birthday': datetime(1955, 5, 2, 0, 0), 'name': 'Bill 3'},
    {'birthday': datetime(1979, 4, 12, 0, 0), 'name': 'John 3'},
    {'birthday': datetime(1978, 10, 14, 0, 0), 'name': 'Ann 3'},
    {'birthday': datetime(1963, 12, 18, 0, 0), 'name': 'Ben 4'},
    {'birthday': datetime(1976, 4, 28, 0, 0), 'name': 'Bill 4'},
    {'birthday': datetime(1987, 3, 4, 0, 0), 'name': 'John 4'},
    {'birthday': datetime(1990, 2, 5, 0, 0), 'name': 'Ann 4'},
    {'birthday': datetime(1957, 1, 3, 0, 0), 'name': 'Ben 5'},
    {'birthday': datetime(1970, 5, 27, 0, 0), 'name': 'Bill 5'},
    {'birthday': datetime(1994, 4, 26, 0, 0), 'name': 'John 5'},
    {'birthday': datetime(1989, 7, 12, 0, 0), 'name': 'Ann 5'},
    {'birthday': datetime(1972, 6, 12, 0, 0), 'name': 'Ben 6'},
    {'birthday': datetime(1989, 6, 15, 0, 0), 'name': 'Bill 6'},
    {'birthday': datetime(1962, 2, 21, 0, 0), 'name': 'John 6'},
    {'birthday': datetime(1956, 6, 26, 0, 0), 'name': 'Ann 6'},
    {'birthday': datetime(1992, 3, 14, 0, 0), 'name': 'Ben 7'},
    {'birthday': datetime(1988, 4, 2, 0, 0), 'name': 'Bill 7'},
    {'birthday': datetime(1954, 11, 29, 0, 0), 'name': 'John 7'},
    {'birthday': datetime(1987, 11, 8, 0, 0), 'name': 'Ann 7'},
    {'birthday': datetime(1973, 5, 20, 0, 0), 'name': 'Ben 8'},
    {'birthday': datetime(1957, 3, 5, 0, 0), 'name': 'Bill 8'},
    {'birthday': datetime(1950, 12, 10, 0, 0), 'name': 'John 8'},
    {'birthday': datetime(1962, 4, 1, 0, 0), 'name': 'Ann 8'},
    {'birthday': datetime(1977, 9, 13, 0, 0), 'name': 'Ben 9'},
    {'birthday': datetime(1988, 5, 6, 0, 0), 'name': 'Bill 9'},
    {'birthday': datetime(1961, 2, 20, 0, 0), 'name': 'John 9'},
    {'birthday': datetime(1979, 9, 25, 0, 0), 'name': 'Ann 9'}]

def generate_users_sample(names: list = NAMES, cycles: int = 10, print_result: bool = False) -> list:
    users = []
    for i in range(0, cycles):
        for name in names:
            month = random.randint(1, 12)
            max_day = None
            if month == 2:
                max_day = 28
            elif month <= 7:
                max_day = 31 if month % 2 else 30
            else:
                max_day = 30 if month % 2 else 31
            day=random.randint(1, max_day)
            users.append({
                "name": f"{name} {i}",
                "birthday": datetime(year=random.randint(1950, 2000), month=month, day=day)
            })
    if print_result:
        pprint.pprint(users, indent=4)
    return users