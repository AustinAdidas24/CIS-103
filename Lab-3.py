#Python Lab Working with Lists
#Task 1: Creating and print lists
Fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(Fruits)

#Task 2: Accessing and Slicing Lists
# 1. Print the first and last element of `fruits`.
# 2. Use slicing to print the first three elements of `fruits`.
# 3. Print every other element of `fruits`.
print("\n", Fruits[0],Fruits[-1])
print("\n", Fruits[:3])
print("\n", Fruits[::2])

#Task 3: Modifying Lists
# 1. Replace "banana" with "blueberry".
# 2. Insert "fig" at index `2`.
# 3. Append "grape" to the end of the list.
# 4. Remove "date" from the list.
Fruits[1] = "blueberry"
print("\n", Fruits)

Fruits.insert(2, "fig")
print("\n", Fruits)

Fruits.append("grape")
print("\n", Fruits)

# Fruits.pop(3)
# print("\n", Fruits)

Fruits.remove("date")
print("\n", Fruits)

# Task 4: List Methods
# 1. Create a list `numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]`.
# 2. Find and print the length of the list.
# 3. Sort the list in ascending order.
# 4. Remove the last element using `pop()`.
# 5. Check if `4` is in the list using `in`.

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(len(numbers))

numbers.sort()
print(numbers)

numbers.pop()
print(numbers)

print("is 4 in list?: ", 4 in numbers)

# Task 5: Looping Through Lists
# 1. Print each item in `fruits` using a `for` loop.
# 2. Convert all fruit names to uppercase and print the new list

for i in Fruits:
    print(i.upper())

# Fruits_upper = Fruits.upper()


# Task 6: Finding the Maximum in a List
# 1. Create a list of random numbers.
# 2. Find and print the largest number.
import random
random_list = [random.randint(1,1000) for i in range(10)]
print(random_list)

print("Max: ", max(random_list))

# Task 7: Copying Lists and Avoiding Aliasing
# 1. Create a list `original = [10, 20, 30]`.
# 2. Create a copy `copy_list = original[:]`.
# 3. Modify `original` and print both lists to confirm they are separate.

original = [10, 20, 30]
bad_copy
copy_list = original[:]
original[1] = 90
print("Original: ", original)
print("Copy: ", copy_list)
print("Bad copy: ", bad_copy)