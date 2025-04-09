# Task 1: Using a For Loop for Definite Iteration
# Write a Python program that prints 'Python is fun!' five times using a for loop.
for number_of_times in range(1,20,2):
    print("Python is Fun!")
#this program prints the phrase: Python is Fun! 10 times using the range(start, stop, step)

# Task 2: Count-Controlled Loop - Factorial Calculation
# Write a Python program that calculates the factorial of a given number using a for loop.
num = int(input("Enter a positive integer: "))
if num < 0:
    print("Please enter a positive number")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num} is {factorial}")
#Task 3: Using While Loop - Sum Until User Exits
# Write a program that keeps asking the user for numbers until they enter a blank input, then
# prints the sum of all entered numbers.
total = 0.0 #creates a variable named: total that contains a floating point value 0.0
while True:
    data = input("Enter a number (or press Enter to quit): ") # takes user input and stored into variable
    if data == "": #Creates a conditional loop that ends when the user enters no input.
        break
    total += float(data)
print("The total sum is", total)

# Task 4: If-Else Selection Statements - Grading System
# Write a program that takes a numeric grade from the user and converts it to a letter grade.
score = int(input("Enter your numeric grade: "))
if score >= 90:
grade = 'A'
elif score >= 80:
grade = 'B'
elif score >= 70:
grade = 'C'
elif score >= 60:
grade = 'D'
else:
grade = 'F'
print(f"Your letter grade is {grade}")