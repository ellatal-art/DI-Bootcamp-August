# Instructions:
# 1. Ask the user for two inputs:
# A number (integer).
# A length (integer).
# 2. Create a program that generates a list of multiples of the given number.
# 3. The list should stop when it reaches the length specified by the user.

number = int(input('Enter a number: '))
length = int(input('Enter the length: '))
multiples = []
for i in range(1, length + 1):
    multiples.append(number * i)
print(multiples)
    
    # Instructions:
# 1. Ask the user for a string.
# 2. Write a program that processes the string to remove 
# consecutive duplicate letters.
# The new string should only contain unique consecutive letters.
# For example, “ppoeemm” should become “poem” 
# (removes consecutive duplicates like ‘pp’, ‘ee’, and ‘mm’).
# 3. The program should print the modified string.

word = input("Enter the word")
result = ""
for letter in word:
    if not result or char != result[-1]:
        result +- char
print(result)


