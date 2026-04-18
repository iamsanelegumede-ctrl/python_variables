# Python Variables Practice: 30 Tasks
# Instructions: Complete each task by writing the code below the comment.

# --- Level 1: The Basics (Naming & Assignment) ---
# 1. Create a variable named 'city' and assign it the name of your hometown.
city="Johannesburg"
print("Question 1:", city)
# 2. Create a variable 'age' and set it to your age.
age= 23
print("Question 2:", age)
# 3. Assign the value 100 to a variable called 'score'.
score= 100
print("Question 3:", score)
# 4. Create a variable 'is_sunny' and set it to True.
is_sunny= True
print("Question 4 is sunny", is_sunny)
# 5. Reassign the 'score' variable from task 3 to a new value: 150.
score=150
print("Question 5 updated score:", score)
# 6. Create two variables, 'x' and 'y', and assign them both the value 5 on a single line.
x=y=5
print("Question 6 the value of x:", x)
print("Question 6 the value of y:", y)
#print("Question 6-X:{x},Y:{y}")
# 7. Rename the illegal variable '2_cool' to something valid.
cool_2="too cool"
print("Question 7:" ,cool_2)
# 8. Create a variable using snake_case (e.g., user_favorite_color).
user_favourite_colour= "black"
print("Question 8:", user_favourite_colour)
# 9. Swap the values of two variables, a = 10 and b = 20, so a is 20 and b is 10.
a=10
b=20
swap= a,b=b,a
print("Question 9:", swap)
# 10. Create a variable 'pi' and assign it the value 3.14159.
pi= 3.14159
print("Question 10:", pi)
# --- Level 2: Data Types & Conversion ---

# 11. Use the type() function to check the data type of 'age'.
print("Question 11:", type(age))
# 12. Create a string 'price_str = "19.99"' and convert it to a float.
price_str= "19.99"
price_float= float(price_str)
print("Question 12:", price_float)
# 13. Convert the float 9.99 into an integer. 
int_value= int(9.99)
print("Question 13:", int_value)
# 14. Create a variable 'greeting' that combines a string and your 'city' variable.
greeting= (city)
print("Question 14: Hello I am from", greeting)
# 15. Use an f-string to print: "I am [age] years old and live in [city]."
print(f"I am {age} years old and live in {city}.")
# 16. Create a variable with a long string and use len() to find its length.
long_string= "I am using this statement to use the length function."
print("Question 16:", len(long_string))
# 17. Use input() to store a name in a variable called 'user_name'.
user_name= input("Please enter your name:")
print("Question 17:", user_name)
# 18. Ask a user for their birth year, convert to int, and calculate their current age.
birth_year= int(input("What is your birth year:"))
current_age= 2026-birth_year
print("Question 18:", current_age)
# 19. Create a boolean variable that checks if 10 is greater than 5.
is_greater= 10>5
print("Question 19:", is_greater)
# 20. Create a variable 'nothing' and assign it the value None.
nothing= None
print("Question 20:", nothing)
# --- Level 3: Basic Math with Variables ---

# 21. Create 'length = 10' and 'width = 5'. Calculate 'area' in a new variable.
length= 10
width= 5
area= length*width
print("Question 21:", area)
# 22. Create 'count = 0'. Increment it by 1 using the += operator.
count= 0
count += 1
print("Question 22:", count)
# 23. Calculate the remainder of 10 / 3 using the modulo operator (%).
remainder= 10%3
print("Question 23:", remainder)
# 24. Create 'base = 2' and 'exponent = 3'. Calculate 2 to the power of 3.
base= 2
exponent= 3
power= base**exponent
print("Question 24:", power)
# 25. Find the average of three variables: test1, test2, and test3.
test1= 10
test2= 20
test3= 30
average= (test1 + test2 + test3)/3
print("Question 25:", average)
# 26. Create 'price = 50'. Calculate a 10% discount and store the final price.
price= 50
discount= price*0.10
final_price= price-discount
print("Question 26:", final_price)
# 27. Convert a 'fahrenheit' variable to 'celsius' using: (F - 32) * 5/9.
fahrenheit=100
celsius=(fahrenheit-32)*5/9
print("Question 27:" ,celsius)
# 28. Create 'seconds = 3660'. Convert this into minutes and remaining seconds.
seconds= 3660
minutes= seconds//60
remaining_seconds= seconds % 60
print("Question 28:" ,minutes)
print("Question 28:" ,remaining_seconds)
# 29. Use a variable to store the result of 10 // 3 (floor division).
x= 10//3
print("Question 29:" ,x)
# 30. Create a 'wallet' variable with 100. Subtract three 'purchase' variables from it.
wallet= 100
purchase1= 10
purchase2= 20
purchase3= 30
wallet= wallet - purchase1 - purchase2 - purchase3
print("Question 30:" ,wallet)