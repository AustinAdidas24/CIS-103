# Question 1: Creating and Accessing Lists
# Create a list named `fruits` containing the following items: `apple`, `banana`, `cherry`. Then,
# perform the following tasks:
# - Print the entire list.
# - Access and print the first and last elements of the list.
# - Add `grape` to the list and print the updated list.
Fruits = ["apple", "banana", "cherry"]
print(Fruits)
print("\n This is the first fruit n the list: ", Fruits[0],"\n This is the second fruit in the list: ", Fruits[-1])
Fruits.append("grape")
print("\n", Fruits)

# Question 2: List Slicing and Indexing
# Given the list `numbers = [10, 20, 30, 40, 50]`, perform the following operations:
# - Print the first three elements using slicing.
# - Print the last two elements using negative indexing.
# - Replace the second element with `25` and print the updated list.

numbers = [10, 20, 30, 40, 50]
first_number = numbers[0] #calls index 0 and stores it in variable first_number
last_number = numbers[4] #calls index4 and stores it in variable last_number
last2 = numbers[-2:] #this prints out the last two numbers of the list with negative indexing
# The colon after the -2 indicates that we want to include all the elements from the second
# to last element up to the end of the list
numbers[1] = 25
print(f"This is the first number: {first_number}")
print(f"This is the last number: {last_number}")
print(f"These are the last two numbers: {last2}" )
print(numbers)

# Question 3: List Methods
# Given `colors = ['red', 'blue', 'green']`, use the appropriate list methods to:
# - Append `yellow` to the list.
# - Insert `black` at the beginning of the list.
# - Remove `blue` from the list.
# - Sort the list in alphabetical order and print it.

colors = ['red', 'blue', 'green']
colors.append("yellow") #appends "yellow" to the list
print(colors)
colors.insert(0, "black") #inserts the color black at the front of the list
print(colors)
colors.remove("blue")
print(colors)
colors.sort()
print(colors)

# Question 4: Searching a List
# Write a Python program that takes a list of names and checks if a specific name is
# present using the `in` operator. If the name exists, print its index; otherwise, print
# `Not Found`.

names = ["john", "smith"]
def lookup_name():
    lookup = input("Enter name to lookup: ")
    if lookup in names:
        index = names.index(lookup)
        print(f"The name, {lookup} is in index {index}")
    else:
        print("Not found")
lookup_name()

# Question 5: Finding the Median Using a List
# Write a Python program that takes a list of numbers and calculates the median.
# If the number of elements is odd, print the middle value; if even, print the
# average of the two middle values.
list_numbers = [1, 2, 3, 4, 5, 6]
def find_median():
    import statistics
    median = statistics.median(list_numbers)
    print(f"The median is {median}")
find_median()

# Question 6: Creating and Accessing a Dictionary
# Create a dictionary named `student` with the following key-value pairs:
# - `'name'`: `'Alice'`
# - `'age'`: `21`
# - `'major'`: `'Computer Science'`
# Then, perform the following operations:
# - Print the student's name.
# - Update the age to `22`.
# - Add a new key-value pair: `'GPA'`: `3.8`.
# - Remove the `'major'` key and print the updated dictionary.

student = {"name": "Alice", "age": "21", "major":"Computer Science"}
print(student["name"])
student["age"] = 22 # Updates the age to 22
student["GPA"] = 3.8 # This creates a new key value pair because it does not yet exist within the dictionary
del student["major"] #deletes the key-value pair
print(student)

# Question 7: Dictionary Methods
# Given the dictionary `grades = {'John': 85, 'Alice': 92, 'Bob': 78}`, perform the following
# operations:
# - Add a new student `'David'` with a grade of `88`.
# - Check if `'Alice'` exists in the dictionary.
# - Print all student names and their grades using a loop.

grades = {'John': 85, 'Alice': 92, 'Bob': 78}
grades["David"] = 88 # Creates a key-value pair that did not exist
print(grades)
print(f"Alice in the list: {'Alice' in grades}") # Finds if the name Alice is in the list
# Print all student names and their grades using a for loop
for student in grades: # Uses for loop that iterates through the dictionary and prints the key and value
    print(f"{student}: {grades[student]}")

for student in grades:
    print(student)
for grades in grades.values():
    print(grades)

# Question 8: Word Frequency Counter
# Write a Python program that takes a sentence as input and counts the occurrences of each word
# using a dictionary. Print the dictionary containing word counts.

def word_counter(sentence):
    words_in_sentence = sentence.split() # breaks the sentence into a list of words using spaces as separators
    # and labels the list words_in_sentence

    # Creates a empty dictionary named words in which the keys will be the words and the values will be the
    # the number of times each words appears
    words = {}

    # This creates a loop that goes through each word in the list named words_in_sentence
    for word in words_in_sentence:
        if word in words:
            words[word] += 1 # adds to the current count of the word if word already exists
        else:
            words[word] = 1 #starts the count at 1 if there is a new word.

    # returns the final dictionary of word counts.
    return words


sentence = "This is testing a Python test within a Python file in a Python IDE"

# Call the function and store the result
words = word_counter(sentence)

#print the amount of times the word is used.
print("# of times each word is used: ")
for word, count in words.items():
    print(f"{word}: {count}")

#import the Counter module from collections
from collections import Counter

def word_counter_(sentence): # create a function
    word_in_sentence = sentence.split() # breaks the sentence into a list of words and names it word_in_sentence
    return Counter(word_in_sentence) # returns the result from the function word_counter_

sentence = "This is testing a Python test within a Python file in a Python IDE"
word_counts = word_counter_(sentence)

print("# of times each word is used: ")
for word, count in word_counts.items():
    print(f"{word}: {count}")

#Question 9: Sorting a Dictionary
# Given `sales = {'John': 1500, 'Alice': 2200, 'Bob': 1800}`, write a program that sorts the dictionary
# by sales amount in descending order