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



    