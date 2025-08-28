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



    