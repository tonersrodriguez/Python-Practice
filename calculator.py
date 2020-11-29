#issue with this block of code??
#num1 = input("Enter a number: ")
#num2 = input("Enter another number: ")
#result = num1 + num2
#print(result)
#num variables are taken as strings instead of numbers

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)
print(result)