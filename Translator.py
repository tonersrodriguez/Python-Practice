number_grid= [
    [1,2,3],#row 0
    [4,5,6],#row 1
    [7,8,9],#row 2
    [0]
#essentially creating 3x4 grid using 2D lists
]
print(number_grid[0][2])
#should print 3
#nested for loop (for-loop in a for-loop)
for row in number_grid:
    for col in row:
        print(col)

#basic translator
#translates any vowel in the phrase inputted with a 'g'
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + 'g'
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))
