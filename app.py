from math import *
'''
this is also considered a comment
'''
#print statments(1)
print("Hello World")
#print statements cont'd (2)
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

#data and variable types(3)
character_name = "Tony"
character_age = "24"
is_male = False
print("There was once a man named " + character_name + ",")
print("He was " + character_age + " years old.")

character_name = "Damian"
print("He really liked the name " + character_name + ",")
print("but didn't like being " + character_age + ".")

#working with strings and functions(4)
#\n- new line or..
# \" - quick print of quotation mark
phrase = "Giraffe Academy"
print("Giraffe Academy\nis teaching me python")
print(phrase + " is cool") #concatenation -appending strings together
print(phrase.upper().isupper())
print(len(phrase))#obtain length of string
#intro to index and replace function with strings
print(phrase.index("A"))
print(phrase.replace("Giraffe", "Elephant"))

#Working with numbers(5)
my_num = 5
#str function converts number to string and aids with concatenation
print(str(my_num) + " my favorite number")
#math functions
print(pow(4,2))
print(abs(-10))
print(max(5,2))
print(min(5, 2))
print(round(3.6))
print(floor(3.22))

#Getting Input from Users(6)
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + " you are " + age + "!")
#prompts user for input then stores input into variable

