friends = ["Tony", "Ana", "Adam", "Alexandra"]
#for letter in "Giraffe Academy":
#print(letter)
for index in range(len(friends)):
    print(friends[index])
#another example
for index in range(1):
    if index == 0:
        print("First Iteration")
    else:
        print("Not the first iteration")

#intro to exponent functions
print(2**3) # == 2^3
def raise_to_power(base_num, pow_num):
    result = 1 #where the math result is stored
    for index in range(pow_num):#range from 0 to pow_num
        result = result * base_num
    return result
print(raise_to_power(3, 9))