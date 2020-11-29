#if-else statment set with multiple conditions to judge three inputs from user
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >=num3:
        return num2
    else:
        return num3
print(max_num(350, 40, 5))

#NOW WE WILL ATTEMPT A BETTER CALCULATOR
#CREATE THREE VARIABLES 2 FOR NUMBERS AND 1 FOR OPERATOR
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid Operator")