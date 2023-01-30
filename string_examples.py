s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"


print("Guido's the ex-BDFL of Python")
print('Guido is the ex-"BDFL" of Python')
print("""Guido's the ex-"BDFL" of Python""")

a = "foo"
b = "bar"
print(a + b)

x = a + b
print(x)
print('foo' in x)
print('ba' in x)
print('spam' in x)

print(x[4])
print(x.index('a'))
print(len(x))

actor = "Chris Hemsworth"

print(f"len(actor): {len(actor)}")
print(f"actor.index('em'): {actor.index('em')}")
print(f"actor.upper(): {actor.upper()}")
print(f"actor.lower(): {actor.lower()}")

print(f"actor.startswith('Chris'): {actor.startswith('Chris')}")
print(f"actor.startswith('Liam'): {actor.startswith('Liam')}")
print(f"actor: {actor}")
print(f"actor.count('h'): {actor.count('h')}")
print(f"actor.lower().count('h'): {actor.lower().count('h')}")


s = "          All my exes live in Texas         "
print("|"  + s + "|")
print("|"  + s.lstrip() + "|")
print("|"  + s.rstrip() + "|")
print("|"  + s.strip() + "|")
print()

n =        1234
print(f"n: {n}")

s2 = "xxxxxyyyyyxyxyxyxyxyxAll my exes live in Texasyyyyyyyyyyyyyyyyyyyyyyx"
print("|"  + s2 + "|")
print("|"  + s2.lstrip("xy") + "|")
print("|"  + s2.rstrip("xy") + "|")
print("|"  + s2.strip("xy") + "|")
print()

print(f"s2.replace('x', 'E'): {s2.replace('x', 'E')}")
s3 = s2.replace('x', 'EEE')
print(f"s3: {s3}")

salary = "$120000"

clean_salary = salary.lstrip('$')









