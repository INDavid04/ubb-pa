# While Loops - Exercise
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box
#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)
# Three Loop Questions:
#1. What do I want to repeat?
#  -> input
#2. What do I want to change each time?
#  -> number
#3. How long should we repeat?
#  -> 3 times
guess_number = 10
i, trials = 0, 5
guessed = False
message = "Guess the number between 1 and 100! "
while i < trials:
    i += 1
    number = int(input(message))
    if number == guess_number:
        i, guessed = trials, True
        print("Hurray! You guessed the number!")
    elif guess_number < number:
        message = f"The number is less than {number}! Another number: "
    else:
        message = f"The number is greater than {number}! Another number: "
if not guessed:
    print(f"Sorry! The number was {guess_number}")

# # Conditionals - Exercise improve
# def num_days(month):
#     # optimize/shorten the code in the function
#     # try to reduce the number of conditionals 
#     if month == 'feb':
#         print('number of days in',month,'is',28)
#     elif month == 'apr' or month == 'jun' or month == 'sep' or month == 'nov':
#         print('number of days in',month,'is',30)
#     else:
#         print('number of days in',month,'is',31)
# num_days('oct')

# # If/Elif /Else - Exercise
# # Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# # Hint: use 3 separate inputs 
# # Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# # formula is: temp in C*9/5 + 32 = temp in f
# operation = str(input("Type: \n c for conversion from celsius to fahrenheit \n + for add \n - for substraction \n * for multiplication \n / for division \n Your input: "))
# if (operation == "c"):
#     temperature = float(input("Enter the temperature in celsius: "))
#     temperature = temperature * 9 / 5 + 32
#     print(f"Temperature in fahrenheit is {temperature}")
# elif (operation == "+"):
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#     print(f"The sum is {a + b}")
# elif (operation == "-"):
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#     print(f"The difference is {a - b}")
# elif (operation == "*"):
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#     print(f"The product is {a * b}")
# elif (operation == "/"):
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#     print(f"The division is {a / b}")
# else:
#     print("Sorry! I do not recognize any operation! Please try again with: c, +, -, * or /")

# # Functions - Exercise
# # 2. extend the function with another  input parameter 'color', that defaults to 'red'
# def greeting(name, age=28, color="red"):
#     #Greets user with 'name' from 'input box' and 'age', if available, default age is used
#     # 5. Capitalize first letter of the 'name', and rest are small caps 
#     print('Hello '  +  name.capitalize() + ', you are ' + str(age) +'!')
#     # 4. Change the 'You are xx!' text to say 'you will be xx+1 years old next birthday adding 1 to the age
#     print(f'Hello again {name}, you will be {age + 1} next birthday!')
#     # 1. Add new print statement - on a new line which says 'We hear you like the color xxx! xxx is a string with color
#     # 6. Favorite color should be in lowercase 
#     print (f'We hear you like the color {color.lower()}!')
# name = input('Enter your name: ')
# age = input('Enter your age: ')
# # 3. Capture the color via an input box as variable:color 
# color = input('Enter your color: ')
# greeting(name, int(age), color)

# # Sets - Exercise
# Eric_and_John = {'Eric','John'}
# friends = {'John','Michael','Terry','Eric','Graham'}
# my_friends = {'Reg','Loretta','Colin','John','Graham'}
# cars =['900','420','V70','911','996','V90','911','911','S','328','900']
# # 1. Check if ‘Eric’ and ‘John’ exist in friends
# print (friends.intersection(Eric_and_John))         # ME
# print('Eric' in friends and 'John' in friends)      # HIM
# # 2. Combine or add the two sets 
# print (friends.union(my_friends))                   # ME
# # print (friends.union | my_friends)                  # HIM
# # 3. Find names that are in both sets
# print (friends.intersection(my_friends))            # ME
# # print (friends.union & my_friends)                  # HIM
# # 4. Find names that are only in friends
# print (friends.difference(my_friends))              # ME
# # print (friends.union - my_friends)                  # HIM
# # 5. Show only the names who only appear in one of the lists
# all_friends = friends.union(my_friends)             # ME
# same_friends = friends.intersection(my_friends)     
# print (all_friends.difference(same_friends))        
# print(my_friends.symmetric_difference(friends))     # HIM
# print(my_friends ^ friends)
# # 6. Create a new cars-list without duplicates
# cars_set = set(cars)                                # ME
# cars_no_duplicates = cars_set
# cars_no_dupl =list(set(cars))                       # HIM
# print (cars_set)

# # Split and Join - Exercise
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise
# # My version
# csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
# friends_list = ['Exercise: fill me with names']
# friends_list.clear()
# csv = csv.replace(':', ',')
# csv = csv.replace(';', ',')
# friends_list = csv.split(',')
# print(friends_list)
# # His Version:
# friends_list = (','.join(','.join(csv.split(';')).split(':'))).split(',')
# print(friends_list)
# print('replace', csv.replace(';',',').replace(':',',').split(','))

# # Split and Join
# msg ='Welcome to Python 101: Split and Join'
# csv = 'Eric,John,Michael,Terry,Graham'
# friends_list = ['Eric','John','Michael','Terry','Graham']
# print(list(msg)) # transforma msg intr-o lista, afisand: ['W', 'e', 'l', 'c', 'o', 'm', 'e', ' ', 't', 'o', ...
# print(msg.split()) # ['Welcome', 'to', 'Python', '101:', 'Split', 'and', 'Join']
# print(msg.split(' ')) # la fel ca mai sus, insa, daca adaugam mai multe spatii, afiseaza si spatiile: '', '', ...
# print(csv.split(',')) # ['Eric', 'John', 'Michael', 'Terry', 'Graham']
# print(str(friends_list)) # ['Eric', 'John', 'Michael', 'Terry', 'Graham']
# print('-'.join(friends_list)) # Eric-John-Michael-Terry-Graham
# print('-'.join(friends_list + friends_list)) # Eric-John-Michael-Terry-Graham-Eric-John-Michael-Terry-Graham
# print(''.join(msg.split())) # WelcometoPython101:SplitandJoin
# print(msg.replace(' ', '')) # WelcometoPython101:SplitandJoin
# print(msg.replace(' ', '<>')) # Welcome<>to<>Python<>101:<>Split<>and<>Join

# # Lists Theory
# friends = ['John','Michael','Terry','Eric','Graham']
# cars = [911,130,328,535,740,308]
# friends.sort() # sorteaza lista
# friends.sort(reverse=True) # sorteaza lista descrescator
# friends.reverse() # inverseaza lista
# print(min(cars)) # 130
# print(max(cars)) # 911
# print(sum(cars)) # 2952
# print(min(friends)) # Eric
# print(max(friends)) # Terry
# friends.append("TerryG") # adauga TerryG la finalul listei
# friends.insert(0, "TerryH") # adauga TerryH pe prima pozitie
# friends[2] = "TerryN" # modifica Terry cu TerryN
# friends.extend(cars) # adauga lista cars la finalul listei friends
# friends.remove('Terry') # scoate Terry din lista
# friends.pop(-2) # scoate penultimul element din lista, -1 pentru ultimul, 0 pentru primul, nimic sau -1 pentru ultimul
# friends.clear() # goleste lista, insa NU o sterge, afisam o lista goala
# del friends # sterge lista, daca incercam sa o afisam, primim eroare
# del friends[2] # sterge al treilea element din lista
# new_friends = friends[:] # copiaza lista friends in new_friends
# new_friends = friends.copy() # la fel ca linia de dinainte
# new_friends = list(friends) # la fel ca primele doua linii de mai sus

# # Lists - Exercise: Selling Lemonade
# You sale lemonade over two weeks, the lists show number of sold per week
# Profit for each lemonade sold is 1.5$
# Add another day to week 2 list by capturing a number as input
# Combine the two lists into the list caled 'sales'
# Calculate/print how much you have earned on
# Best day
# Worst day
# Separately and in total (Hint: 3 prints in total)
# #
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

# # User Input - Exercise
# We want to convert kilometers to miles, knowing that a mile is 1.609 kilometers
# name = input("What is your name?")
# kilometers = input(f"Hi {name}! What is the distance?")
# 1 mile ... 1.609 km
# x mile ... 2 km 
# #
# miles = float(kilometers) / 1.609
# print (f"The distance in miles is: {round(miles, 2)}")
# # User Input
# name = input("My name is: ")
# print (f'Your name is {name}')

# # Strings-2 Find/replace, string formatting
# msg = """Line1
#  Line2
#         Line3"""
# print (msg)
# #
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

# # Python 101: String Exercise 1 
# 1. From the string "Welcome to Python 101: Strings", extract text and create/print a new string that says:
#     a. "1 Welcome Ring to Tyler"
#     b. Every first letter in a word should be capitalized (title format)
# 2. Print the same string backwards... (Hint: Google is your friend)
# #
# initial_string = "Welcome to Python 101: Strings"
# new_string = initial_string[18] + initial_string[0:7] + " Ring " + initial_string[8:10] + " Tyler"
# print (new_string)
# new_titled_string = new_string.title()
# print(new_titled_string)

# # Strings - Basics / Slicing
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

# # Arithmetic operations
# a, b = 8, 2
# print ("For " + str(a) + " and " + str(b))
# print ("Addition: ", a + b)
# print ("Substraction: ", a -b)
# print ("Multiplication: ", a * b)
# print ("Division (float): ", a / b)
# print ("Division (floor): ", a // b)
# print ("Modulus: ", a % b)
# print ("Exponent: ", a ** b)

# # Variables and datatypes
# print('Variables & Datatypes - Exercise')
# Create appropriate Variables for Item name, the price 
# and how many you have in stock
# #
# name="John"
# price=14.99
# in_stock=5
# print(name + ' has ' + str(in_stock) + ' things of ' + str(price) + ' euro!')

# # Here is my first line of Python
# print("Hello World! It is easier to run two commands in index.html instead of downloading python so yeah, power web console")