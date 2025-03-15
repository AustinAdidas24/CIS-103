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
