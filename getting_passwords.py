# method 1
import os

password = os.getenv("MYPASSWORD", "NOT FOUND")
print("password:", password)

# method 2
with open("my_secret_secure_password_file.txt") as pw_in:
    password = pw_in.read().rstrip()
print("password:", password)

# method 3
from getpass import getpass
password = getpass("Please enter your password: ")
print("password:", password)
