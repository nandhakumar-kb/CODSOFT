#Task 3 : Password Generator
print("Task 3 : Password Generator")
import random
import string
try:
    length = int(input("Enter the password length: "))
except ValueError:
    print("Invalid input ,Enter a number.")
all_characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(all_characters) for _ in range(length))
print("Your generated password is:", password)