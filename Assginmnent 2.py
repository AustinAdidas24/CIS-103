# this code asks the user for their first name and last name and greets them
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
print("Hello, " + first_name + " " + last_name + "!") #concatenate the greeting "Hello and users input

# this piece of code asks the user to input 2 numbers and performs the following operations: addition,
# subtraction, multiplication, integer division, and floating-point division.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the first number: "))

print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")

if num2 != 0:
    print(f"Integer Division: {num1 // num2}")
    print(f"Floating-Point Division: {num1 / num2}")
else:
    print("Cannot divide by zero.")

# this code find the square root of the number input by the user and handles errors
import math
number = float(input("Enter a number: "))
if number >= 0:
    print(math.sqrt(number))
else:
    print("Cannot calculate square root of negative number. ")

# asks the user to input a base and exponent and performs the function
base = float(input("Enter the base: "))
exponent = float(input("Enter the exponent"))

print(f"This is the result: {base ** exponent}")

# rounds pi to 5 decimal places
pi_rounded = round(math.pi, 5)
print(pi_rounded)

# Variable reassignment and type conversion
#assigns an integer to a variable x
x = 134
print(x)
#reassigns the same variable with a different floating point number
x = 23
print(x)

#converts a string into an integer
example = "235"
print(example)
print(float(example) + 2345)
