from pprint import pprint

d1 = dict()
d2 = {'NC': 'Raleigh', 'VA': 'Richmond', 'MD': 'Annapolis'}
d3 = {}  # empty dict

print(f"d2['NC']: {d2['NC']}")
print(f"d2: {d2}")

d2['MD'] = 'Baltimore'
print(f"d2: {d2}")

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

airports['ORD'] = "Chicago"

print(f"airports: {airports}")
print()
pprint(airports)
print()

print(f"airports['IAD']: {airports['IAD']}")
# print(f"airports['L']: {airports['L']}")
print(f"airports.get('XYX'): {airports.get('XYX')}")

print(f"airports.get('XYX', 'NOT FOUND'): {airports.get('XYX', 'NOT FOUND')}")

print(f"airports.get('RDU'): {airports.get('RDU')}")
print('-' * 60)

for code, city in airports.items():
    print(code, city)
print()
print('-' * 60)

for code, city in sorted(airports.items()):
    print(code, city)



