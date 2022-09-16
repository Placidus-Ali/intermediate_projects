"""
Q1: Create a function, that repeats the first 2 letters of a word which will be followed by 3 dots and a 
space after. The string should be ended with a question mark.
"""

name = 'Placidus'
while name:
    print((' Pla' + '...' '' )*2, '' 'Placidus' + '?')
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
Q3: 
"""