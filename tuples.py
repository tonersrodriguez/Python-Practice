#Tuples are a type of data structure
#A container that stores different values similiar to a list
#Key differences are: tuples are immutable (unchangeable)

coordinates = [(2, 5), (10, 13), (563, 567)]
#coordinates[1] = 10 - will cause an error since they are immutable
print(coordinates[0])

#Functions
def say_hi(name, age): #function will indent next line. Indentation matters!
    print("Hello " + name + ", you are " + age)
print("Top")
say_hi("Tony", "24")#calls the function
say_hi("Anthony", "25")
print("Bottom")
#Essentially when python executes the program
#it'll execute all code line by line unless called otherwise - flow


