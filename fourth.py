# Q1. Take a string as input and change its case.

string = input("Enter a string: ")

print(string.swapcase())

# Q1. Take a string as input and change its case.
# without using swapcase().

string = input("Enter a string: ")

result = ""

for ch in string:
    if ch.islower():
        result += ch.upper()
    elif ch.isupper():
        result += ch.lower()
    else:
        result += ch

print(result)

# Q2. Print the following pattern.
# If n = 5
# *****
# ****
# ***
# **
# *

n = int(input("Enter n: "))

for i in range(n, 0, -1):
    print("*" * i)

# Pattern 2: Inverted Left Triangle

n = int(input("Enter n: "))

for i in range(n, 0, -1):
    print("*" * i)


# Pattern 5: Pyramid

n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Pattern 6: Diamond

n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
