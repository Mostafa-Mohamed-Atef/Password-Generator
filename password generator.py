from numpy import random
uppercase_alphabets = [chr(i) for i in range(65,91)]
lowercase_alphabets = [chr(i) for i in range(97,123)]
num = [str(i) for i in range(10)]
special_characters = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', 
    '{', '}', '[', ']', '|',':', ';', '"', '<', '>', ',', 
    '.', '?', '/', '~'
]

length = int(input('Enter password length: '))

print("Answer with 'y' and 'n' by this order : \n")

ifchar = input('Characters?').lower()
password = ''
if ifchar == 'n':
    for i in range(length):
        password = password + random.choice(num)
elif ifchar == 'y':
    prop = input("Uppercase? \n Special Characters? \n")
    if prop[0] == 'y':
        lowercase_alphabets.extend(uppercase_alphabets)
    if prop[1] == 'y':
        lowercase_alphabets.extend(special_characters)  
    lowercase_alphabets.extend(num)
    for i in range(length):
        password += random.choice(lowercase_alphabets)

print('Output:',password)