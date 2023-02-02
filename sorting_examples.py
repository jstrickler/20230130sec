fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f1 = sorted(fruits)
print(f"f1: {f1}\n")

def ignore_case(s):
    compare_key = s.upper()
    print(f"comparing {s} as {compare_key}")
    return s.upper()

f2 = sorted(fruits, key=ignore_case)
print(f"f2: {f2}\n")

def wacky(m):
    return m[-1]

f3 = sorted(fruits, key=wacky)
print(f"f3: {f3}\n")

f4 = sorted(fruits, key=str.lower)
print(f"f4: {f4}\n")

f5 = sorted(fruits, key=len)
print(f"f5: {f5}\n")

def my_sort(item):
    return len(item), item.lower()

f6 = sorted(fruits, key=my_sort)
print(f"f6: {f6}\n")

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'LTN': 'London',  # (Luton)
    'LGW': 'London',  # (Gatwick)
    'LHR': 'London',  # (Heathrow)
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

print(f"airports.items(): {airports.items()}")
print()
for code, city in sorted(airports.items()):
    print(code, city)
print('-' * 60)

def by_value(item):
    return item[1], item[0]

for code, city in sorted(airports.items(), key=by_value):
    print(code, city)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

def by_dob(person):
    return person[-1]

for person in sorted(people, key=by_dob):
    print(person)

currencies = [
    "$1234GBP",
    "$47USD",
    "$57000JPY",
    "$123CHF",
]


def by_currency(m):
    return m[-3:]

c1 = sorted(currencies, key=by_currency)
print(f"c1: {c1}\n")

