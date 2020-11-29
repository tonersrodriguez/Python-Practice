#method of protecting program so it doesnt crash giving it exception conditions

try:
    number = int(input("Enter a number: "))
    print(number)
#except cases can be used to handle errors that occur
#except cases are used to catch SPECIFIC errors
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")

