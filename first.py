# Q1. Write a print statement to print below.
# Output:
# He said, "Let's have a cup of Tea"

print('He said, "Let\'s have a cup of Tea"')

# Q2. Write a Python Program to build an Ola/Uber Auto Meter.
# For first 100 km  -> Rs 10/km
# For next 100 km   -> Rs 9/km
# For next 500 km   -> Rs 6/km
# Waiting charge    -> Rs 5/min

distance = int(input("Enter distance (km): "))
waiting = int(input("Enter waiting time (minutes): "))

fare = 0

if distance <= 100:
    fare = distance * 10

elif distance <= 200:
    fare = (100 * 10) + ((distance - 100) * 9)

elif distance <= 700:
    fare = (100 * 10) + (100 * 9) + ((distance - 200) * 6)

else:
    fare = (100 * 10) + (100 * 9) + (500 * 6)

fare = fare + (waiting * 5)

print("Total Fare = Rs.", fare)

# Q3. Write a Python program to generate an Electricity Bill.
# If units < 100, then bill is Free
# For next 100 units, bill is Rs 5/unit
# For next 100 units, bill is Rs 7/unit
# Thereafter, Rs 10/unit

units = int(input("Enter electricity units: "))

bill = 0

if units < 100:
    bill = 0

elif units <= 200:
    bill = (units - 100) * 5

elif units <= 300:
    bill = (100 * 5) + (units - 200) * 7

else:
    bill = (100 * 5) + (100 * 7) + (units - 300) * 10

print("Electricity Bill = Rs.", bill)

# Q4. Calculate the below expression.
# (18 ** 3 + 2 ** 5) * (25 // 4) % 2 - ((144 / 12) ** 2)

result = (18 ** 3 + 2 ** 5) * (25 // 4) % 2 - ((144 / 12) ** 2)

print("Result =", result)


# Q5. Write a program to find a badge number.
# Badge number = Sum of ASCII values of agent_letter,
# code_number and security_level.

agent_letter = "B"
code_number = "5"
security_level = "2"

badge_number = ord(agent_letter) + ord(code_number) + ord(security_level)

print("Badge Number =", badge_number)




