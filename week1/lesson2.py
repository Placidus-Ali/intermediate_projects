"""
Q1: Create a function, that repeats the first 2 letters of a word which will be followed by 3 dots and a 
space after. The string should be ended with a question mark.
"""

name = 'Placidus'
while name:
    print(((name[0:2]+'...'' ')*2),name +'?')
    break
"""
Q2: Perform a for loop that searches through a string and prints only distinct vowel letters
"""

my_name = "My name is Placidus Chukwuebuka Ali"
vowel_letters = "aeiouAEIOU" 
for letters in my_name:
    if letters in vowel_letters:
        print(letters)

"""
Q3: Perform a while loop that requests for a name, if that name is entered, it will be printed else,
if user types “end” (this command should be case insensitive), the while loop is terminated
"""
school_name = "stutern"
while True:
    choice = input('Enter your choice: ') 
    if choice == school_name:
        print(school_name)
    if choice == 'end' or 'End' or 'ENd' or 'enD' or 'EnD':
        break
# pls remember that I used an input statement here. So it will require you to make a 'choice' before it could be executed. 
# If your choice is school_name which is 'stutern', it will print 'stutern', but if your choice is any of the spelling of 'end' provided, it 
# will break.
