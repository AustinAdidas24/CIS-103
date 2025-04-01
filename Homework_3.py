#Homework - 3
#    String Manipulation: Write a Python program that takes a user’s first name and last name as input and prints a greeting message
#    that includes their full name. Done
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print("Welcome to python", first_name, last_name)

#    Arithmetic Operations: Write a Python script that asks the user to enter two numbers and then displays:
#     Their sum
#     Their difference
#     Their product
#     The result of dividing the first number by the second (show both integer and float division)
num1 = input("Enter first number")
num2 = input("Enter second number")

print("The sum is:", int(num1) + int(num2))
print("The difference is:", int(num1) - int(num2))
print("The product is:", int(num1) * int(num2))
print("The result of the division of num1 by num2 is:", int(num1) / int(num2))
print("The result of the division of num1 by num2 is:", float(num1) / float(num2))

# Using Functions and Modules:
# Write a Python program that imports the math module and calculates the area of a circle.
# The program should ask the user to enter the radius of the circle, compute the area using the formula: Area = π * r², and print the result with an appropriate message.

import math
radius = float(input("Enter the radius of the circle: "))

print("The are of the circle is: ", math.pi * (radius ** 2))