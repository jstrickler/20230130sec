person = "Bill", "Gates", "Microsoft", "1955-10-28"

print(f"person[0]: {person[0]}")

first_name = person[0]
last_name = person[1]
# etc etc

first_name, last_name, product, dob = person   # iterable unpacking


things = [
    (25, 'a', 'Chris', 'Don', 'Maria'),
    (32, 'm'),
    (8, 'x', 'Mike'),
]

for wombat in things:
    print(wombat[0], wombat[1])

print(f"things[0]: {things[0]}")
print(f"things[0][1]: {things[0][1]}")
print('-' * 60)
for room_size, carpet_code, *name in things:
    print(room_size, carpet_code, name)

print("\U0001F92F")


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

for first_name, last_name, product, dob in people:
    print(last_name, product)
print()

