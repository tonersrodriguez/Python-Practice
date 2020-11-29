#return-statements
def cube(num):
    return num*num*num
    #return any value back to the caller
    #return is also last call so nothing after will be read


#prints value called by function
#print(cube(16))

result = cube(4)
print(result)

#intro to if-statements
is_male = False #boolean variable
is_tall = True
if is_male and is_tall:
#or checks for multiple conditions to match
#and checks for all condiions to match
    print("You are a male or you're just tall or both, who knows.")
#if variable is set to false then nothing would print since it checks if boolean is true
#else-if
elif is_male and not is_tall:
    print("You're a male just not tall shortie, sorry.")
elif not(is_male) and is_tall:
    print("You're not a male but you are tall")
else:
    print("You are not a male and you might not be tall, sorry bub.")