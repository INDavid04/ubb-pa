### Split and Join
msg ='Welcome to Python 101: Split and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(list(msg)) # transforma msg intr-o lista, afisand: ['W', 'e', 'l', 'c', 'o', 'm', 'e', ' ', 't', 'o', ...
print(msg.split()) # ['Welcome', 'to', 'Python', '101:', 'Split', 'and', 'Join']
print(msg.split(' ')) # la fel ca mai sus, insa, daca adaugam mai multe spatii, afiseaza si spatiile: '', '', ...
print(csv.split(',')) # ['Eric', 'John', 'Michael', 'Terry', 'Graham']
print(str(friends_list)) # ['Eric', 'John', 'Michael', 'Terry', 'Graham']
print('-'.join(friends_list)) # Eric-John-Michael-Terry-Graham
print('-'.join(friends_list + friends_list)) # Eric-John-Michael-Terry-Graham-Eric-John-Michael-Terry-Graham
print(''.join(msg.split())) # WelcometoPython101:SplitandJoin
print(msg.replace(' ', '')) # WelcometoPython101:SplitandJoin
print(msg.replace(' ', '<>')) # Welcome<>to<>Python<>101:<>Split<>and<>Join
###

### Lists Theory
friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
friends.sort() # sorteaza lista
friends.sort(reverse=True) # sorteaza lista descrescator
friends.reverse() # inverseaza lista
print(min(cars)) # 130
print(max(cars)) # 911
print(sum(cars)) # 2952
print(min(friends)) # Eric
print(max(friends)) # Terry
friends.append("TerryG") # adauga TerryG la finalul listei
friends.insert(0, "TerryH") # adauga TerryH pe prima pozitie
friends[2] = "TerryN" # modifica Terry cu TerryN
friends.extend(cars) # adauga lista cars la finalul listei friends
friends.remove('Terry') # scoate Terry din lista
friends.pop(-2) # scoate penultimul element din lista, -1 pentru ultimul, 0 pentru primul, nimic sau -1 pentru ultimul
friends.clear() # goleste lista, insa NU o sterge, afisam o lista goala
del friends # sterge lista, daca incercam sa o afisam, primim eroare
del friends[2] # sterge al treilea element din lista
new_friends = friends[:] # copiaza lista friends in new_friends
new_friends = friends.copy() # la fel ca linia de dinainte
new_friends = list(friends) # la fel ca primele doua linii de mai sus
###

### Lists - Exercise: Selling Lemonade
# You sale lemonade over two weeks, the lists show number of sold per week
# Profit for each lemonade sold is 1.5$
# Add another day to week 2 list by capturing a number as input
# Combine the two lists into the list caled 'sales'
# Calculate/print how much you have earned on
# Best day
# Worst day
# Separately and in total (Hint: 3 prints in total)
###
# sales_w1 = [7,3,42,19,15,35,9]
# sales_w2 = [12,4,26,10,7,28]
# sales = []
# new_day = int(input("How many lemonade have you sold last Sunday?"))
# sales_w2.append(new_day)
# sales.extend(sales_w1)
# sales.extend(sales_w2)
# print(f"You've earned {max(sales) * 1.5}$ in your best day!")
# print(f"You've earned {min(sales) * 1.5}$ in your worst day!")
# print(f"You've earned {max(sales) * 1.5 + min(sales) * 1.5}$ both in your best and worst day!")

### User Input - Exercise
# We want to convert kilometers to miles, knowing that a mile is 1.609 kilometers
# name = input("What is your name?")
# kilometers = input(f"Hi {name}! What is the distance?")
# 1 mile ... 1.609 km
# x mile ... 2 km 
###
# miles = float(kilometers) / 1.609
# print (f"The distance in miles is: {round(miles, 2)}")

### User Input
# name = input("My name is: ")
# print (f'Your name is {name}')

### Strings-2 Find/replace, string formatting
# msg = """Line1
#  Line2
#         Line3"""
# print (msg)

# msg = "Welcome to Python 101: Strings"
# print (msg.find('Python'))
# print (msg.replace('Python', 'Java'))
# print ('Python' in msg)
# print ('Java' in msg)

# # Challenge: Make the name (TERRY) capitilized!
# name='TERRY'
# color = 'RED'
# msg = '[' + name + '] loves the color ' + color.lower() + '!'
# msg1 = f'[{name.capitalize()}] loves the color {color.lower()}!'
# print(msg)
# print(msg1)

### Python 101: String Exercise 1 
# 1. From the string "Welcome to Python 101: Strings", extract text and create/print a new string that says:
#     a. "1 Welcome Ring to Tyler"
#     b. Every first letter in a word should be capitalized (title format)
# 2. Print the same string backwards... (Hint: Google is your friend)
###
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
# Create appropriate Variables for Item name, the price 
# and how many you have in stock
###
# name="John"
# price=14.99
# in_stock=5
# print(name + ' has ' + str(in_stock) + ' things of ' + str(price) + ' euro!')

### Here is my first line of Python
# print("Hello World! It is easier to run two commands in index.html instead of downloading python so yeah, power web console")