# Q1. Write a program to take any 2 numbers as input
# from user and find LCM of two numbers.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

greater = max(num1, num2)

while True:
    if greater % num1 == 0 and greater % num2 == 0:
        print("LCM =", greater)
        break
    greater += 1

# Q2. Write a program to take 2 numbers from user
# and find their HCF (Highest Common Factor).

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

hcf = 1

for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i

print("HCF =", hcf)

# Q3. Take an integer as input and convert it
# into binary form without using inbuilt functions.

num = int(input("Enter a number: "))

binary = ""

if num == 0:
    binary = "0"
else:
    while num > 0:
        rem = num % 2
        binary = str(rem) + binary
        num = num // 2

print("Binary =", binary)

# Q4. Write a program to take 2 integer inputs
# (start and end), then print every alternate number between them.

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

for i in range(start, end + 1, 2):
    print(i, end=" ")
  
# Q5. Take 2 integer inputs from user (start and end)
# Print every alternate number in a single line
# separated by "_"

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

for i in range(start, end + 1, 2):
    if i + 2 <= end:
        print(i, end="_")
    else:
        print(i)
