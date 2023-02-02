
anne_countries = ['Egypt', 'Morocco', 'Mexico', 'Honduras', 'Malaysia',
        'Spain', 'Canada', 'Belgium', 'Laos']

felix_countries = ['Morocco', 'United Kingdom', 'Laos', 'Morocco',
         'Canada', 'Vietnam', 'Uzbekistan', 'Australia']

anne = set(anne_countries)
felix = set(felix_countries)
anne.add("Burkina Faso")
anne.add('Egypt')

print("BOTH:", anne & felix)  # intersection
print("JUST ONE:", anne ^ felix)  # xor
print("ALL:", anne | felix)  # union
print("JUST anne:", anne - felix)
print("JUST felix:", felix - anne)


