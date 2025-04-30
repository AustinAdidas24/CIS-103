# 6. Write a function summation(lower, upper) that returns the sum
# of all integers from lower to upper, inclusive.
def summation(lower, upper):
    result = 0
    for i in range(lower, upper + 1): # the +1 here ensures that the upper value is included
        result += i
    return result
print(summation(1,5))
# This would print out 15 because our code says that we want to add
# all the numbers that are in between 1 and 5 including 1 and 5


# 7. Modify the repToInt function so that the base argument is optional
# and defaults to 2.
def repToInt(repString, base=2):
    decimal = 0
    exponent = len(repString) - 1
    for digit in repString:
        decimal = decimal + int(digit) * base ** exponent
        exponent -= 1
    return decimal
string_1 = "011001"
print(repToInt(string_1))

# 8.	Given the structure chart for the text analysis program,
# explain how the design supports division of labor and hides complexity.
# Well the chart shows how the program is divided into different modules/functions which include:
# countSentences, countWords, countSyllables, fleschIndex, gradeLevel.
# These are all functions that make up the main program. Each functions hides the complexity within that module/function
# so we don't see exactly what is going on we only know what it does.

# 9.	The doctor program uses a reply function to simulate a conversation
# . What programming principle is demonstrated by separating this logic
# into its own function?
# So here the program is broken down into smaller independent functions.
# This isolates the code responsible for understanding input and generating responses and
# is within a single function, making it easier to find, understand and alter down the line.
# Top down design
# 10.	Brainstorm and describe a simple program idea (not from the
# PowerPoint)that could benefit from top-down design. List at least 3
# functions it would use and what each would do.
# I am thinking of a program that would allow you to utilize your phone
#completely hands free using voice commands.
# This program would lsiten for voice commands and perform whichever action
# is associated to that voice command. We would have to write a function that listens for
# voice commands by capturing audio input from the user utilizing the onboard mic and
# identifies the command and returns it as a string.
# The second function would have to take the string as input and execute the action/s associated
# with the command.

