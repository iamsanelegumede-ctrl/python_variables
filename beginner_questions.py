# Python Beginner Practice Workbook (Questions Only)
# Complete each task by writing your own code.

# -------------------------------
# 1. VARIABLES & DATA TYPES
# -------------------------------
# Create variables for:
# - Your name
# - Your age
# - Your height
#name = "Sanele"
#age = 23
#height = 1.5
# Print a sentence:
# My name is ___, I am ___ years old, and ___ meters tall.
#print(f"My name is {name}, I am {age} years old, and {height} meters tall.")
# Convert:
# - Age to float
# - Height to integer
#age_float = float(age)
#height_int = int(height)
#print(f"My age as a float is {age_float} and my height is {height_int} meters.")
# -------------------------------
# 2. USER INPUT
# -------------------------------
# Ask the user for:
# - Their name
# - Their age
#name = input("What is your name?")
#age = int(input("What is your age?"))
# Print:
# Hello [name], you will be [age + 5] in 5 years.
#print(f"Hello {name}, you will be {age + 5} in 5 years.")

# -------------------------------
# 3. CONDITIONAL STATEMENTS
# -------------------------------
# Ask the user for a number
#num = int(input("Please enter your number"))
# Check:
# - If positive → print "Positive number"
# - If negative → print "Negative number"
# - If zero → print "Zero"
#if num > 0:
 #   print("Positive number")
#elif num < 0:
 #   print("Negative number")
#else: print(0)        
# Bonus:
# Check if the number is even or odd
#if num % 2 == 0:
 #   print("even number")
#else: print("odd number")    

# -------------------------------
# 4. LOOPS
# -------------------------------
# For loop:
# - Print numbers from 1 to 10
for i in range(1,11):
    print(i)

# - Print only even numbers
for i in range(2,11,2):
    print(i)

# While loop:
# - Keep asking for a password until correct


# -------------------------------
# 5. LISTS
# -------------------------------
# Create a list of 5 favorite foods

# Print:
# - First item
# - Last item

# Add a new food
# Remove one item


# -------------------------------
# 6. DICTIONARIES
# -------------------------------
# Create a dictionary with:
# - name
# - age
# - city

# Print each value

# Add a new key:
# - job


# -------------------------------
# 7. FUNCTIONS
# -------------------------------
# Create a function that:
# - Greets a user
#def greet_user():
 #   print("Hello Sanele")
#greet_user()
# Create a function that:
# - Adds two numbers
# - Returns the result


# -------------------------------
# 8. STRINGS
# -------------------------------
# Given a string:
# - Count characters
# - Convert to uppercase
# - Convert to lowercase

# Check if a word exists in the string


# -------------------------------
# 9. FILE HANDLING
# -------------------------------
# Create a text file

# Write your name into it

# Read and print the contents


# -------------------------------
# 10. MINI PROJECT: STUDENT MANAGER
# -------------------------------
# Build a program that:
# - Asks user to enter student names
# - Stores them in a list
# - Prints all students
# - Saves them to a file
# - Allows searching for a student
