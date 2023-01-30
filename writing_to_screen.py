value = 37.3439
person = "Fred Flintstone"
city = "Bedrock"

print(value, person, city)
print("Barney is Fred's friend")
print(value, person, city, sep=',')
print(value, person, city, sep=' X ')
print(value, person, city, sep='')
print("Python", end=' ')
print("is", end=' ')
print("the", end=' ')
print("best")


print(city, person, sep=',')

s = f"{city},{person}"
print(s)
s = "{},{}".format(city, person)
print(s)

print(f"Value is {value}")
print(f"Value is {value:.3f}")

