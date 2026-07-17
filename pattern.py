
# Question 1:
# Print the following pattern. If n = 5
#
# *****
# ****
# ***
# **
# *

n = 5

for i in range(n, 0, -1):
    print("*" * i)


# Q.2) Take a string as input and change the case of it.
# Example:
# Input : Sandip Polytechnic
# Output: sANDIP pOLYTECHNIC

s = input("Enter a string: ")

print(s.swapcase())

