### Strings-2 Find/replace, string formatting
msg = """Line1
 Line2
        Line3"""
print (msg)

msg = "Welcome to Python 101: Strings"
print (msg.find('Python'))
print (msg.replace('Python', 'Java'))
print ('Python' in msg)
print ('Java' in msg)

# Challenge: Make the name (TERRY) capitilized!
name='TERRY'
color = 'RED'
msg = '[' + name + '] loves the color ' + color.lower() + '!'
msg1 = f'[{name.capitalize()}] loves the color {color.lower()}!'
print(msg)
print(msg1)

### Python 101: String Exercise 1
# """ 
# 1. From the string "Welcome to Python 101: Strings", extract text and create/print a new string that says:
#     a. "1 Welcome Ring to Tyler"
#     b. Every first letter in a word should be capitalized (title format)
# 2. Print the same string backwards... (Hint: Google is your friend)
# """
# initial_string = "Welcome to Python 101: Strings"
# new_string = initial_string[18] + initial_string[0:7] + " Ring " + initial_string[8:10] + " Tyler"
# print (new_string)
# new_titled_string = new_string.title()
# print(new_titled_string)


### Strings - Basics / Slicing
# msg='welcome to it\'s Python 101: Strings' # \ is the escaping character which means the nex character should't be interpreted as a special character, so the ' character should't close the string
# print ("### Strings Basics")
# print (msg) # normal print
# print (msg+msg) # print the message for two times with no space
# print (msg*3) # print the message for three times with no space
# print (msg,msg) # print the message for two times with space 
# print (msg.upper()) # every letter capitalized
# print (msg.lower()) # every letter is lower
# print (msg.capitalize()) # only the first letter is capitalized
# print (msg.title()) # only the first letter of a new word is capitalized
# print (len(msg)) # counts the lengts of the msg variable where \' is one character and we do not add one more character for \0
# print (msg.count('python')) # will return 0 because is case sensitive
# print (msg.count('Python')) # will retunr 1 because we have one "Python"
# print (msg.count('o')) # will return 3 because we have three '0'
# print ("### String Slicing")
# """
# w e l c o m e   t o    i  t  \' s     P  y  t  h  o  n     1  0  1  :     S  t  r  i  n  g  s
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34
# """
# print (msg[0]) # the first letter, w
# print (msg[5]) # the letter m
# print (msg[-1]) # the last letter, s
# print (msg[-4]) # the last four letter, i
# print (msg[11:13]) # msg[11] and msg[12], so it, inclusive 11, exclsive 13 (11-12)
# print (msg[16:]) # from position 16 to the end, Python 101: Strings (16-34)
# print (msg[:7]) # from the beggining to the 7th position exclusive, welcome (0-6) 
# print (msg[-7:]) # from the last 7th position to the end, Strings (28-34)
# print (msg[-7:-4]) # from the last 7th inclusive position to the last 4th exclusive postion, Str (28-30)

### Arithmetic operations
# a, b = 8, 2
# print ("For " + str(a) + " and " + str(b))
# print ("Addition: ", a + b)
# print ("Substraction: ", a -b)
# print ("Multiplication: ", a * b)
# print ("Division (float): ", a / b)
# print ("Division (floor): ", a // b)
# print ("Modulus: ", a % b)
# print ("Exponent: ", a ** b)

### Variables and datatypes
# print('Variables & Datatypes - Exercise')
# #Create appropriate Variables for Item name, the price 
# #and how many you have in stock
# name="John"
# price=14.99
# in_stock=5
# print(name + ' has ' + str(in_stock) + ' things of ' + str(price) + ' euro!')

### Here is my first line of Python
# print("Hello World! It is easier to run two commands in index.html instead of downloading python so yeah, power web console")