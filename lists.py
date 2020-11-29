#practice with lists
friends = ["Anthony" , "Juan", "Marcelo", "Justin", "Miguel", "Staphany"]
#lists can hold a variety of variables and will run fine

print(friends)
print(friends.index("Staphany"))
print(friends[0]) #accesses the position in the list
print(friends[-2])#backdoor indexing/begins at -1
friends[1] = "Juana"#modification of list
print(friends[1])

#using functions for lists
lucky_numbers = [2, 5, 15, 23, 25, 41, 100]
#extend function - appends lists together
friends.extend(lucky_numbers)
print(friends)

#add individual elements instead of entire list
friends.append("Edgar") #adds to end of list
friends.insert(2, "Andrea") #locates index position and adds new name to list
print(friends)
friends.remove("Marcelo")
print(friends)
friends.pop()#gets ride of last element in this list
print(friends)
friends.clear()#clears entire list
print(friends)

#sort
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)

#copy
friends2 = friends.copy()
print(friends2)

