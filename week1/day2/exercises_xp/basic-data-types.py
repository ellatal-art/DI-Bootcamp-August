    #Exercise 1: Favorite Numbers   
# Key Python Topics:
# Sets
# Adding/removing items in a set
# Set concatenation (using union)
#     Instructions:
# Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
# Note: Sets are unordered collections, so ensure no duplicate numbers are added.

my_fav_numbers = {2, 5, 6, 10}
my_fav_numbers.update([4, 8])
print(my_fav_numbers)
my_fav_numbers.remove(8)

friend_fav_numbers = {11, 12}

my_fav_numbers.update(friend_fav_numbers)
print(my_fav_numbers)
    #Firstly I confused append() with add(), whuch caused an AttributeError
    #To concatenate 2 sets I was choosing between 2 options: unuon() update()
    #I chose update() because it was simpler and faster
    
    
    #Exercise 2: Tuple
# Key Python Topics:
# Tuples (immutability)
# Instructions:
# Given a tuple of integers, try to add more integers to the tuple.
# Hint: Tuples are immutable, meaning they cannot be changed after creation. 
# Think about why you can’t add more integers to a tuple

my_tuple = (1, 2, 3)
print(my_tuple)
    #Tuples are immutabler, so I convert it into a list to modify it
    
temp_list = list(my_tuple)
    #Make the necessary changes, and then convert it back into a tuple
    
temp_list.append(4)
temp_list.append(5)
my_tuple = tuple(temp_list)
print(my_tuple)

    #Exercise 3: List Manipulation
# Key Python Topics:
# Lists
# List methods: append, remove, insert, count, clear
    # Instructions:
# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list.
# Remove "Blueberries" from the list.
# Add "Kiwi" to the end of the list.
# Add "Apples" to the beginning of the list.
# Count how many times "Apples" appear in the list.
# Empty the list.
# Print the final state of the list.

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove('Blueberries')
basket.append("Kiwi")
basket.sort()
print(basket)
basket.count("Apples")
print(basket.count('Apples'))
basket.clear()
print(basket)
    # Everything here is pretty logical: the methods do exactly what their names say

    #Exercise 4: Floats
# Recap: What is a float? What’s the difference between a float and an integer?
# Create a list containing the following sequence of mixed floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?

# A float is a number with decimals, unlike an integer which is a whole number.

current_number = 1.5
numbers = []

while current_number <= 5:
    numbers.append(current_number)
    current_number += 0.5
print(numbers)

#at first, because my output was im a column. Then I realized I had to use a list and .append() 
#each number inside the loop.
#I also learned about IndentationError 

    # Exercise 5: For Loop
# Key Python Topics:
# Loops (for)
# Range and indexing
# Instructions:
# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.

numbers = range(1, 21)
for number in numbers:
    print(number)
    
for num in range(1, 21):
    print:(num)
 
index = 0
for num in range(1, 21):
    if index % 2 == 0:
        print(num)
    index += 1
    
    #I checked if the index is even using "if" and printed only even indexes 
    
    #Exercise 6: While Loop
# Key Python Topics:
# Loops (while)
# Conditionals
# Instructions:
# Write a while loop that keeps asking the user to enter their name.
# Stop the loop if the user’s input is your name.

name = ""
while name != "Ella":
    name = input("Enter your name: ")
print("Hello, " , name)
    #it stops automatically
    
# Exercise 7: Favorite Fruits
# Key Python Topics:
# Input/output
# Strings and lists
# Conditionals
# Instructions:
# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new fruit. I hope you enjoy it!"



fruits = input("Enter your favorite fruits(separetad by spaces):")
favorite_list = fruits.split()
print("Your favorite fruits are:", favorite_list)
new_fruit = input("Enter the name of any fruit: ")
if new_fruit in favorite_list:
    print("You chose one of your favorite fruits! Enjoy")
else:
    print("You chose a new fruit. I hope you enjoy it!")

    #Exercise 8: Pizza Toppings
# Key Python Topics:
# Loops
# Lists
# String formatting
# Instructions:
# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.


toppings = []

while True:
    topping = input("Enter pizza topping (or type 'quit' to finish): ")
    if topping == 'quit': 
        break
    
    toppings.append(topping)
    print("Adding", topping, "to your pizza.")

print("\nYour pizza toppings are:", toppings)

total = 10+2.5 * len(toppings)
print("Total cost: $", total)
    #it was difficult, included many steps: like creting loop, using break, 
    # storing toppings in a list and calculating
    
    #Exercise 9: Cinemax Tickets
# Key Python Topics
# Conditionals
# Lists
# Loops
# Instructions:
# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.

total_cost = 0
members = int(input("How many family members?"))

for member in range(members):
    age = int(input("How old are each member?"))
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15
    total_cost += price 
print("Total cost for all tickets:", total_cost)

    #Bonus:
# Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
# Write a program to:
# Ask for each person’s age.
# Remove anyone who isn’t allowed to watch.
# Print the final list of attendees.

allowed = []
teenagers = int(input("How many people does a group of teenagers include?"))

for i in range(teenagers):
    age = int(input("How old are each member?"))
    if 16 <= age <=21:
        allowed.append(age)
    else:
        print("Sorry, you are not allowed.")
        
print("People allowed to watch:", allowed)

# Exercise 10: Sandwich Orders
# Key Python Topics:
# Lists
# Loops (while)
# Instructions:
# Using the list:
# sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]
# The deli has run out of “Pastrami”, so use a loop to remove all instances of “Pastrami” from the list.
# Prepare each sandwich, one by one, and move them to a list called finished_sandwiches.
# Print a message for each sandwich made, such as: "I made your Tuna sandwich."
# Print the final list of all finished sandwiches.

sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]
finished_sandwiches = []
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove("Pastrami")
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)
print("All finished sandwiches:", finished_sandwiches)







        
    
    
    





    