#################
# Laboratorul 2 #
#################

# Instructiunea conditionala
x = 10
if x % 2 == 0:
    if x > 8:
        print(x, "este numar par mai mare decat 8")
    print(x)
elif x % 3 == 0:
    print(x, "multiplu de 3")
else:
    print("nu stiu nimic despre x")

# structura repetitiva
# cu numar de pasi <-> pentru / for
# RECAP: range(<OPT>start, stop, <OPT>step) <OPT> means optional parameter
for i in range(1, 10, 3):
    print(i)
    
# nu exista structura repetitiva cu test final do ... while!!!
# cu test initial
# daca <conditie> ramane True atunci while-ul continua sa execute operatiile din interiorul sau
print("while")
n = 5
while n > 0:
    n -= 1 # n = n - 1, n op= valoare <=> n = n op valoare
    print(n)
    break
    
for i in range(1, 11):
    if i % 2 != 0 or i <= 5:
        continue
    print(i)
    break

# Problema 1
n, reversedN = 101, 0
copyN = n
while copyN > 0:
    lastDigit = copyN % 10
    reversedN = reversedN * 10 + lastDigit
    copyN //= 10
if n == reversedN:
    print(True)
else:
    print(False)
print('palindrom' if n == reversedN else 'NU e palindrom')

# Problema 2
L1, L2 = 440, 280
copyL1, copyL2 = L1, L2

while copyL2 != 0:
    r = copyL1 % copyL2
    copyL1 = copyL2
    copyL2 = r
print(f'l = {copyL1}, nr. placi = {L1 * L2 // (copyL1 ** 2)}')

# Problema 4
a, b = 17, 37
for i in range(0, 100):
    if i >= a and i <= b or i % 5 != 0:
        continue
    print(i)
    
for i in range(99, -1, -1):
    if i >= a and i <= b or i % 5 != 0:
        continue
    print(i)

#################
# Laboratorul 3 #
#################

s = input()
print(s.center(10))
print(s[1:-1])
for i in range(len(s) // 2):
    print(s[i + 1:-i - 1].center(10))

s = input("s = ")
t = input("t = ")
pos = s.find(t)
if pos == -1:
    print(f'{t} nu a fost gasit in {s}.')
else:
    while pos != -1:
        print(pos, end=" ")
        pos = s.find(t, pos + len(t))

pos = s.index(t)
try:
    while True:
        print(pos, end=" ")
        pos = s.index(t, pos + len(t))
except:
    pass

prop = "Problemele cu siruri de caracteger nu sunt ggerle!"
s = "re"
t = "ger"
prop = prop.replace(t, s)
print(prop)

p = 1
if prop.count(t) > p:
    print(f"prea multe greseli detectate, au fost corectate primele {p}")
    prop = prop.replace(t, s, p)
print(prop)

prop = "Ana     are mere si    prune"
s = "mere"
t = "pere"
words = prop.split(" ")
for i in range(len(words)):
    if words[i] == s:
        words[i] = t
prop = " ".join(words)
print(prop)

prop = " " + prop + " "
s = " " + s + " "
t = " " + t + " "
prop = prop.replace(s, t)
print(prop[1:-1])

prop = "Ana,     are mere, si    prune."
s = "mere"
t = "pere"
words = prop.split()
print(words)

# Stefan Leustean:
# sir = input()
# s = input()
# t = input()
# pos = sir.find(s)
# while pos != -1:
#     ok1, ok2 = False, False
#     if pos == 0 or not sir[pos - 1].isalpha():
#         ok1 = True
#     if pos + len(s) == len(sir) or not sir[pos + len(s)].isalpha():
#         ok2 = True
#     if ok1 and ok2:
#         sir[pos:len(sir)].replace(s, t, count = 1)
#     pos = sir.find(s, pos + 1)

#################
# Laboratorul 4 #
#################

x = "Astazi este laboratorul     de liste la      PA"
resulted_words = []
words = x.split()
for word in words:
    if word[0].lower() in "aeiou":
        resulted_words.append(word)
print(*resulted_words, sep="\n")

resulted_words_comp = [word for word in words if word[0].lower() in "aeiou"]
print(*resulted_words_comp, sep="\n")

decrypted = "CIFRUL"
crypted = [chr(ord("A") + ((ord(c) - ord("A") + 1) % 26)) for c in decrypted]
print("".join(crypted))

x = "Ana are mere"
translation = [(c + "p" + c.lower()) if c.lower() in "aeiou" else c for c in x]
print(*translation, sep="")

x = "Astazi este laboratorul     de liste la      PA"
resulted_words = []
words = x.split()
for word in words:
    if word[0].lower() in "aeiou":
        resulted_words.append(word)
print(*resulted_words, sep="\n")

resulted_words_comp = [word for word in words if word[0].lower() in "aeiou"]
print(*resulted_words_comp, sep="\n")

decrypted = "CIFRUL"
crypted = [chr(ord("A") + ((ord(c) - ord("A") + 1) % 26)) for c in decrypted]
print("".join(crypted))

x = "Ana are mere"
translation = [(c + "p" + c.lower()) if c.lower() in "aeiou" else c for c in x]
print(*translation, sep="")

# Operatii cu liste
l1, l2 = [1, 2, 3, 4], [4, 5, 6, 7]
l1[1::2] = l2[1::2]
print(l1)

k = 1
l = [1, 2, 3, 4, 5, 6, 7]
# l = [l[i] for i in range(len(l)) if i >= k]
# l = l[k:]
print(l)

while k != 0:
    k -= 1
    l.pop(0) # <=> l.remove(l[0])
print(l)

l = [1, 2, 3, 0, 5, 6, 7, 8, 0, 10, 11, 12, 13, 14]
try:
    first_zero = l.index(0)
    second_zero = l.index(0, first_zero + 1)
    
    l[:second_zero + 1] = l[:first_zero]
    print(l)
except:
    print("Lista nu are 0-uri")

l = [1, 2, 3, 0, 5, 6, 7, 8, 0, 10, 11, 12, 13, 14]
try:
    while True:
        l.remove(0) # <=> zero_i = l.index(0) l.pop(zero_i)
except:
    print(l)

x = input().split() # Returneaza lista de STR!!!
x = [int(el) for el in x]
x_without_duplicates = [el for el in x if x.count(el) <= 1]
print(*x_without_duplicates)

l = [-2.345, 1, 3.4, -3, 50]
for i in range(len(l)):
    current_element = l[i]
    if current_element < 0:
        l.insert(i + 1, 0)
print(l)

#################
# Laboratorul 6 #
#################

import random
import string

v = [50, 30, 20, 10, 100]

def func(x):
    if x // 100 >= 1:
        return x ** 0.5
    return x

# v.sort(key=func, reverse=True) -> modificarile se fac in v, astfel pierdem v-ul original
v_prime = sorted(v, key=func, reverse=True) # sorted() nu face modificari in place, returneaza iterabilul(lista) sortat
print(v)

f = open("elevi.txt", "r")
person_database = {}
for person_information in f:
    split_person_information = person_information.split()
    print(split_person_information)
    person_id = split_person_information[0]
    person_database[person_id] = {
        "name": split_person_information[1],
        "surname": split_person_information[2],
        "grades": []
    }
    grades = [int(grade) for grade in split_person_information[3:]]
    # for grade in grades:
    #     person_database[person_id]["grades"].append(grade)
    person_database[person_id]["grades"] = grades
f.close()
print(person_database)

def increase_first_grade_by_cnp(cnp, person_database):
    if cnp not in person_database:
        return None

    grade = person_database[cnp]["grades"][0]
    return grade + 1 if grade != 10 else 10
print(increase_first_grade_by_cnp('2402900000041', person_database))
print(increase_first_grade_by_cnp('2402900020041', person_database))

def extend_list_grades_by_cnp(cnp, l_grades, person_database):
    if cnp not in person_database:
        return None

    grades = person_database[cnp]["grades"]
    grades.extend(l_grades)
    return grades
print(extend_list_grades_by_cnp('2402900000041', [10, 9, 8], person_database))
print(extend_list_grades_by_cnp('2402900200041', [10, 9, 8], person_database))

cnp_to_be_deleted = input()
def delete_by_cnp(cnp, person_database):
    if cnp not in person_database:
        return

    del person_database[cnp]
delete_by_cnp(cnp_to_be_deleted, person_database)
print(person_database)

# l = [2, 3]
# def list_add(li):
#     li.append(4)
# list_add(l)
# print(l)

g=open("elevi.out","w")
list_elevi = []

def sort_name(x):
    return x[0]
def sort_mean(x):
    return sum(x[2]) // len(x[2])

for cnp in person_database:
    l = []
    l.append(person_database[cnp]["name"])
    l.append(person_database[cnp]["surname"])
    l.append(person_database[cnp]["grades"])
    l.append(sum(person_database[cnp]["grades"]) // len(person_database[cnp]["grades"]))
    list_elevi.append(l)
print(list_elevi)
list_elevi.sort(key=sort_name, reverse=False)
print(list_elevi)
list_elevi.sort(key=sort_mean, reverse=True)
print(list_elevi)

print(string.ascii_letters)

def add_code_for_student(person_database):
    for cnp in person_database:
        person_database[cnp]['cod'] = random.choices(string.ascii_letters, k=3) + random.choices(string.digits, k=3)
        person_database[cnp]['cod'] = "".join(person_database[cnp]['cod'])
add_code_for_student(person_database)
print(person_database)

p = int(input())

filename = input()
f = open(filename, "r")

d = {}
for wordlist in f:
    wordlist_split = wordlist.split()
    for word in wordlist_split:
        suffix = word[len(word)-p:]
        if suffix in d:
            d[suffix].append(word)
        else:
            d[suffix] = [word]

def sort_dim(x):
    return len(x)
values_d = list(d.values())
values_d.sort(key = sort_dim, reverse = True)

def sort_dim_dict(x):
    return len(d[x])
sorted_d = sorted(d, key=sort_dim_dict, reverse=True)
new_d = {key: d[key] for key in sorted_d}
print(new_d)

for x in values_d:
    x.sort(reverse = True)
g = open("rime.txt", "w")
for x in values_d:
    g.write(" ".join(x) + "\n")
g.close()

# Stefan Teodor Minea
# def find_index_greater_than(s, x, i = 0, j = None):
#     if j is None:
#         j = len(s)
#     slice = s[i:j]
#     for k in range(len(slice)):
#         if x > slice[k]:
#             return k+i
#     return -1
# l = [1, 2, 3, 4, 5, 6, 7]
# ok = True
# for i in range(len(l) - 1):
#     index = find_index_greater_than(l, l[i], i, i+2)
#     if index == i+1:
#         continue
#     else:
#         ok = False
#         break
# if ok == True:
#     print("E desc")
# else:
#     print("Nu e desc")

#################
# Laboratorul 7 #
#################

l, n = [], None

def read_list():
    global l, n
    n = int(input("n="))
    for i in range(n):
        element = int(input())
        l.append(element)
        
read_list()
print(n, l)

def find_index_greater_than(s, x, i = 0, j = None):
    if j is None:
        j = len(s)
    
    slice = s[i:j]
    print(slice)
    for k in range(len(slice)):
        if x < slice[k]:
            return k + i
    return -1

print(find_index_greater_than([1, 2, 3, 4, 5, 6, 7], 4, j=3))

l = [7, 6, 5, 4, 3, 2, 1]
l2 = [1, 2, 3, 4, 5, 6, 7]
verify = True
for i in range(1, len(l)):
    if find_index_greater_than(l, l[i - 1], i, len(l)) != -1:
        verify = False
decision = "NU" if not verify else "DA"
print(decision)

"""
Despachetare dintr-o lista (numar variabil de parametrii)
"""
def stick_digits(*numbers):
    maximum_stick_number = ""
    for number in numbers:
        maximum_digit = max(str(number))
        maximum_stick_number += maximum_digit
    return int(maximum_stick_number)

stick_digits(4251, 73, 8, 133)
print(stick_digits(4251, 73, 8, 133))

def verify_stick_binary(a, b, c):
    result = stick_digits(a, b, c)
    return True if ord(max(str(result))) <= ord("1") else False

print(verify_stick_binary(1001, 0, 10))

# __init__.py > algoritmi_elementari
def numar_cifre(n):
    if n < 10:
        return 1
    return 1 + numar_cifre(n // 10)


def invers_numar(n, invers=0):
    if n == 0:
        return invers
    return invers_numar(n // 10, invers * 10 + n % 10)


def cmmdc(a, b):
    if b == 0:
        return a
    return cmmdc(b, a % b)
#
# Cinema 1 % Minionii 2 % 12:30 18:30
# Cinema 3 % Elfii cofetari % 10:30 12:30
# Cinema 2 % Minionii 2 % 15:00 18:30 20:30
# Cinema 1 % Elfii cofetari % 10:00 12:30
# Cinema 2 % Gasca Animalutelor % 15:00 18:30 20:00
# Cinema 4 % Minionii 2 % 16:00 18:30 20:30
# Cinema 1 % Buna dimineata % 09:30
#

def citire_program(fisier):
    program_cinematografie = {}

    f = open(fisier, 'r')
    for linie in f:
        nume_cinematograf, nume_film, ore_de_difuzare = map(str.strip, linie.split('%'))
        ore = ore_de_difuzare.split()

        if nume_cinematograf not in program_cinematografie:
            program_cinematografie[nume_cinematograf] = {}
        program_cinematografie[nume_cinematograf][nume_film] = ore

    f.close()
    return program_cinematografie

program = citire_program("cinema.in")
print(program)

def sterge_ore(program, cinema, film, ore):
    if cinema in program and film in program[cinema]:
        program[cinema][film] = [ora for ora in program[cinema][film] if ora not in ore]

        if not program[cinema][film]:
            del program[cinema][film]

        return list(program[cinema].keys())
    return []

f = input("nume film=")
c = input("nume cinema=")
o = input("ora programata pentru film (hh:mm)=")
print(sterge_ore(program, c, f, {o}))
#print("Cinema 1 % Nume film % 12:00 13:00".split(" % "))

#################
# Laboratorul 8 #
#################

import re
from collections import defaultdict

def count_user_actions(file_name):
    events = defaultdict(list)
    count_user_action = 0
    with open(file_name, 'r') as log_file:
        for line in log_file:
            re_match_email = re.search(r'[A-Za-z0-9_\-]+@[A-Za-z]+(\.[a-z]{2,3})+', line)
            if re_match_email is not None: # suntem in cazul in care avem un log al unui utilizator
                count_user_action += 1

                re_match_name = re.search(r'^([A-Za-z\s]+)\s\(', line)
                user_name = re_match_name.group(1)

                re_match_date_time = re.search(r'\[(\d{2}\.\d{2}\.\d{4}\,\s\d{2}\:\d{2}\s[AMP]+)\]', line)
                date_time = re_match_date_time.group(1)

                events[user_name].append(date_time)

    print(f'Total number of user actions: {count_user_action}')

    with open('output_logs.txt', 'w') as output_file:
        for user in events.keys():
            output_file.write(f'{user}: {"; ".join(events[user])}\n')

count_user_actions('log.txt')

def check_valid_ip_addresses(file_name):
    ipv4_regex = re.compile(r'^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])'
                            r'(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$')

    ipv6_regex = re.compile(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$')

    results = []
    with open(file_name, 'r') as ip_line:
        n = int(ip_line.readline())
        for _ in range(n):
            line = ip_line.readline()
            if ipv4_regex.match(line):
                results.append("IPv4")
            elif ipv6_regex.match(line):
                results.append("IPv6")
            else:
                results.append("Neither")

    with open("ip_out.txt", 'w') as output_file:
        output_file.write("\n".join(results))

check_valid_ip_addresses('ip.txt')

def extract_domains(file_name):
    domains = set()
    domain_regex = re.compile(r'https?:\/\/(ww[w2]\.)?([a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+)')
    with open(file_name, 'r') as f:
        n = int(f.readline())
        for _ in range(n):
            line = f.readline()
            matches = domain_regex.findall(line)
            for match in matches:
                domains.add(match[1])

    with open("output_domains.txt", 'w') as g:
        g.write(";".join(sorted(domains)))

extract_domains('domains.txt')

import datetime
def create_events(file_name):
    with open(file_name, 'r') as f:
        output_file = open('output_events.txt', 'w')
        for line in f:
            nume_eveniment, data_str = line.split(", ")

            data_eveniment = datetime.datetime.strptime(data_str.strip(), "%d-%m-%Y %H:%M")
            data_curenta = datetime.datetime.now()
            diferenta = (data_eveniment - data_curenta).days
            data_afisare = data_eveniment.strftime("%d/%m/%Y %H:%M")

            if diferenta < 0:
                mesaj = f"{nume_eveniment} - {data_afisare} - Eveniment trecut"
            else:
                mesaj = f"{nume_eveniment} - {data_afisare} - Zile pana la eveniment: {diferenta}"
            output_file.write(f"{mesaj}\n")
        output_file.close()

create_events('input_event.txt')

##################
# Laboratorul 11 #
##################

l = [("Andrew", 30), ("John", 30), ("Timmy", 10), ("George", 25)]

"""
Sa se ordoneze l crescator dupa varsta, iar in caz de egalitate sa se ordoneze numele
invers lexicografic

l = [("Timmy", 10), ("George", 25), ("John", 30), ("Andrew", 30)]
"""
def sortCriteria(x):
    name, age = x[0], x[1]
    return (-age, name)

l.sort(key=sortCriteria, reverse=True)
l = [("Andrew", 30), ("John", 30), ("Timmy", 10), ("George", 25)]
new_l = sorted(l, key=lambda x: (-x[0], x[1]), reverse=True)
print(l, new_l)

input_file = open("date.in", "r")

n = int(input_file.readline().strip())
# v = list(map(lambda x: int(x), input_file.readline().split()))
v = list(map(int, input_file.readline().split()))

input_file.close()

def get_maximum_point(v, f, l):
    if l - f < 2:
        return max(v[f], v[l])

    mid = (f + l) // 2
    if v[mid - 1] < v[mid] and v[mid] > v[mid + 1]:
        return v[mid]
    if v[mid - 1] < v[mid] < v[mid + 1]:
        return get_maximum_point(v, mid + 1, l)
    return get_maximum_point(v, f, mid - 1)

output_file = open("date.out", "w")
output_file.write(f'{get_maximum_point(v, 0, len(v) - 1)}')
output_file.close()

def fill(x, y, dim):
    global k, m
    if dim == 1:
        k += 1
        m[x][y] = k
    else:
        step = dim // 2
        fill(x, y + step, dim // 2)
        fill(x + step, y, dim // 2)
        fill(x, y, dim // 2)
        fill(x + step, y + step, dim // 2)

n = int(input("n = "))
power_2_n = 1 << n

k = 0
m = [[0 for _ in range(power_2_n)] for _ in range(power_2_n)]
fill(0, 0, power_2_n)
for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j], end=" ")
    print()

##################
# Laboratorul 12 #
##################

input_file = open("matrice.in", "r")
output_file = open("matrice.out", "w")

for content in input_file:
    current_line = list(map(int, content.split()))

    first_maximum, second_maximum = None, None
    for i, line_element in enumerate(current_line):
        if first_maximum is None:
            first_maximum = (line_element, i)
        elif first_maximum is not None and line_element >= first_maximum[0]:
            second_maximum = first_maximum
            first_maximum = (line_element, i)
        elif second_maximum is not None and line_element >= second_maximum[0]:
            second_maximum = (line_element, i)

    modified_current_line = []
    for i, line_element in enumerate(current_line):
        if i == first_maximum[1] or i == second_maximum[1]:
            continue
        modified_current_line.append(line_element)
    modified_current_line = list(map(str, modified_current_line))
    output_file.write(f'{" ".join(modified_current_line)}\n')

input_file.close()
output_file.close()


from collections import Counter, defaultdict

input_file_name = input('Introduceti numele fisierului de intrare: ')
input_file = open(input_file_name, "r")

count_words = Counter() # Counter() = defaultdict(int)
for content in input_file:
    list_words = content.strip().split()
    if len(list_words) == 0:
        continue

    for word in list_words:
        count_words[word.lower()] += 1
input_file.close()

frequency_dict = defaultdict(list)
for word, freq in count_words.items():
    frequency_dict[freq].append(word)
frequency_dict = dict(frequency_dict)
sorted_frequency_indices = sorted(frequency_dict, reverse=True)

frequency_dict[list(frequency_dict.keys())[0]].sort()
for key in sorted_frequency_indices:
    print(f"Frecventa {key}: {', '.join(frequency_dict[key])}")

d = {
    "ana": 3,
    "mere": 2,
    "pere": 3
}
# "ana: 3, pere: 3, mere: 2"

sorted_d_key_list = sorted(d, key=lambda x: d[x], reverse=True)
new_dict = {}
for element in sorted_d_key_list:
    new_dict[element] = d[element]
print(new_dict)

input_file = open("matrice.in", "r")
output_file = open("matrice.out", "w")

for content in input_file:
    current_line = list(map(int, content.split()))

    first_maximum, second_maximum = None, None
    for i, line_element in enumerate(current_line):
        if first_maximum is None:
            first_maximum = (line_element, i)
        elif first_maximum is not None and line_element >= first_maximum[0]:
            second_maximum = first_maximum
            first_maximum = (line_element, i)
        elif second_maximum is not None and line_element >= second_maximum[0]:
            second_maximum = (line_element, i)

    modified_current_line = []
    for i, line_element in enumerate(current_line):
        if i == first_maximum[1] or i == second_maximum[1]:
            continue
        modified_current_line.append(line_element)
    modified_current_line = list(map(str, modified_current_line))
    output_file.write(f'{" ".join(modified_current_line)}\n')

input_file.close()
output_file.close()


# from collections import Counter, defaultdict
#
# input_file_name = input('Introduceti numele fisierului de intrare: ')
# input_file = open(input_file_name, "r")
#
# count_words = Counter() # Counter() = defaultdict(int)
# for content in input_file:
#     list_words = content.strip().split()
#     if len(list_words) == 0:
#         continue
#
#     for word in list_words:
#         count_words[word.lower()] += 1
# input_file.close()
#
# frequency_dict = defaultdict(list)
# for word, freq in count_words.items():
#     frequency_dict[freq].append(word)
# frequency_dict = dict(frequency_dict)
# sorted_frequency_indices = sorted(frequency_dict, reverse=True)
#
# frequency_dict[list(frequency_dict.keys())[0]].sort()
# for key in sorted_frequency_indices:
#     print(f"Frecventa {key}: {', '.join(frequency_dict[key])}")

d = {
    "ana": 3,
    "mere": 2,
    "pere": 3
}
# "ana: 3, pere: 3, mere: 2"

sorted_d_key_list = sorted(d, key=lambda x: d[x], reverse=True)
new_dict = {}
for element in sorted_d_key_list:
    new_dict[element] = d[element]
print(new_dict)

input_file = open("date.in", "r")
output_file = open("date.out", "w")

v = list(map(int, input_file.readline().strip().split()))
input_file.close()

dp = [0] * len(v)

# Initializare
dp[0] = v[0]

# Recurenta
maximum_argument = (dp[0], 0)
for i in range(1, len(v)):
    dp[i] = max(dp[i - 1] + v[i], v[i])

    if maximum_argument[0] < dp[i]:
        maximum_argument = (dp[i], i)

sol = []
for i in range(maximum_argument[1], 0, -1):
    sol.append(v[i])
    if dp[i] == v[i]:
        break
sol.reverse()

sol = list(map(str, sol))
output_file.write(f'{" ".join(sol)}\n')
output_file.close()


input_file = open("date.in", "r")
output_file = open("date.out", "w")

M = []
m, n = map(int, input_file.readline().strip().split())
for content in input_file:
    line = list(map(int, content.strip().split()))
    M.append(line)

dp = [[0] * n for _ in range(m)] # genereaza o matrice m x n de 0-uri

# Initializarea
dp[0][0] = M[0][0]

for j in range(1, n):
    dp[0][j] = dp[0][j - 1] + M[0][j]

for i in range(1, m):
    dp[i][0] = dp[i - 1][0] + M[i][0]

# Recurenta
for i in range(1, m):
    for j in range(1, n):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + M[i][j]
print(dp)

path = []
i, j = m - 1, n - 1
while i > 0 or j > 0:
    path.append((i, j))
    if i > 0 and j > 0:
        if dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    elif i > 0:
        i -= 1
    else:
        j -= 1

path.append((0, 0))
path.reverse()
print(path)
