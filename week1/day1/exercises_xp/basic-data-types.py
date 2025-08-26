    #Exercise 1 : Hello World
# Instructions
# Print the following output in one line of code:
# Hello world
# Hello world
# Hello world
# Hello world

print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
#Dublicating the line(shift + option + down arrow)

print('Hello World\nHello World\nHello World\nHello World')
#Using \n - newline

    # Exercise 2 : Some Math
# Instructions
# Write code that calculates the result of:
# (99^3)*8 (meaning 99 to the power of 3, times 8).

result = (99**3)* 8
print(result)
#at first I used (:) and it gave me - "NameError: name 'result' is not defined"
#then I replased ":" and "="

    # Exercise 3 : What Is The Output ?
# Predict the output of the following code snippets:
# >>> 5 < 3     False - 5 is not less than 3
# >>> 3 == 3    True - both sides are equal
# >>> 3 == "3"  False - different types
# >>> "3" > 3   we can not compare str and int
# >>> "Hello" == "hello"    False - case-sensitive

print(5 < 3)
print(3 == 3)
print(3 == "3")
#print("3" > 3)         TypeError cannot compare string and integer
print("Hello" == "hello")

    #Exercise 4 : Your Computer Brand
# Instructions
# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable, print a sentence that states the following:
# "I have a <computer_brand> computer."

Computer_brand = "MacBook"
print("I have a " + Computer_brand + " computer.")

# #Exercise 5 : Your Information
# Instructions
# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. 
# The sentence must contain all the variables created in parts 1, 2, and 3.
# Have your code print the info message.
# Run your code.

full_name = 'Ella Tal'
age = 35
shoe_size = 38
info = full_name + ' will soon grow up ' + str(age) + ' to the size of her feet ' + str(shoe_size)
print(info)
    #At first I forgot to convert numbers to strings
    #Then I fixed it and also added the missing spaces
    
    #Exercise 6 : A & B
# Instructions
# Create two variables, a and b.
# Each variable’s value should be a number.
# If a is bigger than b, have your code print "Hello World".

a = 2
b = 1
if a>b:
    print("Hello World")
    #Firstly I skipped ":", because I forgot that "if" is a condition
    
    #Exercise 7 : Odd Or Even
# Instructions
# Write code that asks the user for a number and determines whether this number is odd or even.

number = int(input('Enter a number: '))
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
    #I had to check if a number is odd or even. 
#I can check it by dividing the number by 2 (using the modulo operator %)
#Then I used conditinals "if; else" 

    #Exercise 8 : What’s Your Name ?
# Instructions
# Write code that asks the user for their name and determines 
# whether or not you have the same name. Print out a funny message based on the outcome.

name = input('What is your name?')
if name == 'Ella':
    print("We are namesake monkeys")
else:
    print('The only monkey here is you')
    
        #Exercise 9 : Tall Enough To Ride A Roller Coaster
# Instructions
# Write code that will ask the user for their height in centimeters.
# If they are over 145 cm, print a message that states they are tall enough to ride.
# If they are not tall enough, print a message that says they need to grow some more to ride.

height = int(input("What is your height?"))
if height >= 145:
    print('You are allowed to rude!')
else:
    print('You are not allowed to ride')
    #it's important to convert input - integer
    










