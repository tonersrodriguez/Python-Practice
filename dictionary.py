monthConversions = {
    #converting 3 char month names to full names
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
}

print(monthConversions.get("Jun", "Not a valid key"))

#intro to while-loops
#initial value of variable
i = 1
#while this condition is true function will loop
#loop condition
while i <=10:
    print(i)
    # or i = i+1 (both increment i)
    i += 1
print("Done with loop")