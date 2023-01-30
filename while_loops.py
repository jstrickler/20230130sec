
i = 0
while i < 3:
    print(i)
    i += 1
print()

while True:
    response = input("Is class over yet? ")
    if response == "n":
        print("Aw, man....")
        continue
    elif response == "y":
        print("Yippee!!")
        break
    else:
        print("Please enter 'y' or 'n'")

print("BYE-BYE")
