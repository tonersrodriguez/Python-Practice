
#reading files - use open()
#r means that it only wants to read the file
employee_file = open("employees.txt", "r")#store open function in a variable
for employee in employee_file.readlines():
    print (employee)#using the for loop you are printing out the entire array
employee_file.close()#generally you want ot close the file after opening

#writing and appending files
#appending means to add text to files
# r - read, a - append, w - write
#writing to files can be useful by overwriting an existing file, writing a new file, or appending
employee_file = open("employees.txt", "a")
employee_file.write("\nEleo - Delivery Driver")
employee_file.close()

'''
employee_file = open("index.html", "w")
employee_file.write("<p>This is an html sample creating using 'w'</p>")
employee_file.close()
'''
#module is an external python file you import
#pip is used to install python modules / package manager / comes installed in python versions 3 and above
