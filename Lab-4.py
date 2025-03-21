# Python Lab: Working with Dictionaries
# Part 1: Basic Dictionary Operations
# Problem 1: Creating a Dictionary
# Create a dictionary named `student` with the following key-value pairs:
# - `"name"`: `"John Doe"`
# - `"age"`: `20`
# - `"major"`: `"Computer Science"`
# - `"GPA"`: `3.8`
# Print the dictionary.

student = {
    "name": "John Doe",
    "age": 20,
    "major": "Computer Science",
    "GPA": 3.8
}

print(student)
# Problem 2: Accessing Values
# Using the `student` dictionary from Problem 1, print:
# - The student's name.
# - The student's major.

print("The students name is", student["name"])
print("Their major is", student["major"])

# Problem 3: Adding and Updating Values
# Add the following key-value pairs to the `student` dictionary:
# - `"email"`: `"johndoe@example.com"`
# - `"graduation_year"`: `2026`
# Then, update the `"GPA"` to `3.9`. Print the updated dictionary.
student["email"] = "johndoe@example.com"
student["graduation_year"] = "2026"
student["GPA"] = 3.9
print(student)
# Problem 4: Removing a Key-Value Pair
# Remove the `"age"` key from the dictionary and print the updated dictionary.

student.pop("age",)
print(student)

# Problem 5: Checking for a Key
# Check if the key `"email"` exists in the `student` dictionary. Print `True` if it exists, otherwise print
# `False`.

if "email" in student:
    print("True")
else:
    print("False")
#We can also print out the email if it is within the dictionary
if "email" in student:
    print(student["email"])
# THIS IS THE SHORTHAND METHOD
print("email" in student) #this will print true or false automatically
# Problem 6: Iterating Over Keys and Values
# Write a program that iterates over the `student` dictionary and prints each key-value pair in the
# format:
# ```
# key: value
# ```

# for (key, value) in student.items():
#     print(key)
# # or you can also do this
print(list(student.keys()))
print(list(student.values()))


# Problem 7: Counting Words in a Sentence
# Write a Python program that takes a sentence as input and counts the occurrences of each
# word, storing the result in a dictionary.
# **Example Input:**
# ```
# sentence = "hello world hello"
# ```
# **Expected Output:**
# ```
# {'hello': 2, 'world': 1}
# ```
# sentence = input("Enter a sentence: ")
# list_of_words1 = sentence.split
sentence = "This is an example sentence for lab 4"
words = sentence.split()
print(words)
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)
# Problem 8: Finding the Maximum Value
# Given a dictionary of test scores, find and print the student with the highest score.
# ```python
# scores = {'Alice': 85, 'Bob': 92, 'Charlie': 88, 'David': 75}
# ```
# **Expected Output:**
# ```
# Bob has the highest score of 92.
# ```

scores = {'Alice': 85, 'Bob': 92, 'Charlie': 88, 'David': 75}

max_student = max(scores, key=scores.get)
print(f"{max_student} has the highest score of {scores[max_student]}.")

# Problem 9: Merging Two Dictionaries
# You are given two dictionaries:
# ```python
# dict1 = {'a': 100, 'b': 200}
# dict2 = {'c': 300, 'd': 400}
# ```
# Merge them into a single dictionary.
# Problem 10: Inverting a Dictionary
# Given a dictionary where keys are names and values are ages:
# ```python
# ages = {'Alice': 25, 'Bob': 30, 'Charlie': 35}
# ```
# Create a new dictionary where the keys are ages and the values are names.
# **Expected Output:**
# ```
# {25: 'Alice', 30: 'Bob', 35: 'Charlie'}
# ```
# Problem 11: Removing Duplicates
# Given a dictionary with some duplicate values, create a new dictionary that keeps only unique
# values.
# ```python
# data = {'name1': 'apple', 'name2': 'banana', 'name3': 'apple', 'name4': 'orange'}
# ```
# **Expected Output:**
# ```
# {'name1': 'apple', 'name2': 'banana', 'name4': 'orange'}
# ```
# Problem 12: Sorting a Dictionary by Values
# Sort the following dictionary by its values in **descending order**.
# ```python
# sales = {'John': 1500, 'Alice': 2200, 'Bob': 1800}
# ```
# **Expected Output:**
# ```
# {'Alice': 2200, 'Bob': 1800, 'John': 1500}
# ```
# Problem 13: Nested Dictionary Access
# You are given a nested dictionary:
# ```python
# employee = {
# 'name': 'Alice',
# 'position': 'Software Engineer',
# 'salary': {
# 'base': 70000,
# 'bonus': 5000
# }
# }
# ```
# Print:
# 1. The employee’s name.
# 2. The employee’s base salary.
# 3. The total salary (base + bonus).
# Problem 14: Frequency of Characters in a String
# Write a program that takes a string and counts the frequency of each character using a
# dictionary.
# **Example Input:**
# ```python
# text = "hello"
# ```
# **Expected Output:**
# ```
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}
# ```
# Problem 15: Dictionary Comprehension
# Use dictionary comprehension to create a dictionary where keys are numbers from `1` to `5` and
# values are their squares.
# **Expected Output:**
# ```
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# ```