##########
# baza 2 #
##########

def baza2(nr):
    b2 = 0
    p = 1
    while nr != 0:
        b2 = b2 + (nr%2)*p
        nr = nr//2
        p = p*10
    return b2

nr = int(input("Numarul convertit in baza 2 este: "))
print(f"Numarul {nr} in baza 2 este: {baza2(nr)}")
print(f"Numarul {nr} in baza 2 este: {bin(nr)}")

##############
# submultimi #
##############

def subm1(n):
    for i in range(0, 1 << n): # 2**n
        for j in range(0, n):
            if (i >> j) & 1:
                print(f'{j+1} ', end='')
        print()

def subm2(n):
    for i in range(0, 1 << n): # 2**n
        for j in range(0, n):
            if i & (1 << j):
                print(f'{j+1} ', end='')
        print()

n = int(input("numarul de elemente: "))
print(f'submultimile cu {n} elemente: ')
subm2(n)

#############
# fibonacci #
#############

n = int(input())
a = 1
b = 1

while b <= n:
    a,b = b, a+b

print(f"{a} ")
n = n-a

while n !=0:
    if a <= n:
        n = n-a
        print(f"{a} ")
    a,b = b-a, a

##########
# minmax #
##########

n=int(input())
if n%2==0:
    x=int(input())
    y=int(input())
    start = 2
    if (x>y):
        maxim, minim = x, y
    else:
        maxim, minim = y, x
else:
    x=int(input())
    minim = maxim = x
    start = 1

for i in range (start, n, 2):
    x=int(input())
    y=int(input())
    if x>y:
        if x>maxim:
            maxim=x
        if y<minim:
            minim=y
    else:
        if y>maxim:
            maxim=y
        if x<minim:
            minim=x
print (f"Minimul este {minim}, maximul este {maxim}")

############
# periodic #
############

s = input()
t = ""
for i in range(len(s) // 2 + 1, 0, -1):
    if len(s) % i != 0:
        continue
    """
    if s.count(s[:i])==len(s)//i: # numara aparitiile care nu se suprapun
        print(f"Sirul {s} se obtine prin concatenarea lui {s[:i]} de {len(s) // i} ori")
        break
    """
    t = s[:i] * (len(s) // i)
    if t == s:
        print(f"Sirul {s} se obtine prin concatenarea lui {s[:i]} de {len(s) // i} ori")
        break

else:
    print(f"Nu este periodic sirul {s}")

#########
# prime #
#########

import re
w = input("cuv: ")
p = int(input("nr litere: "))
a = input("propozitie: ")

suf = w[-p:]
print(f"{p}-rimele ale cuvantului \'{a}\' sunt: ", end="")
a=a.replace(","," ")

"""#a = a.split( )
a=re.split("[, ;]",a) #[multimea separatorilor]
print(a)
a=re.split("[, ;]+",a)
print(a)
"""
for i in a:
    if suf == i[-p:]:
        print(i, end=" ")

#############
# seminar 2 #
#############

for i in range(10):
 print(i, end=" ")
 i=3
 print(i, end=" ")

########################
# 2 sum cu dict de poz #
########################

f = open("numere_comune.in", 'r')
nums = [ int(x) for x in f.readline().split()]
s = dict() #element:pozitie s[element]
target=10
for i in range(0, len(nums)):
    if target - nums[i] in s:
        print (s[target - nums[i]],i)
    s[nums[i]]=i

################
# 2 sum sortat #
################

f = open("numere_comune.in", 'r')
g = open("numere_comune.out", 'w')

ls = [ int(x) for x in f.readline().split()]
i = 0
j = len(ls) - 1
while i<j:
    if ls[i]+ls[j] == 0:
        print((ls[i], ls[j]), file=g)
        i += 1
        j -= 1
    elif ls[i] + ls[j] < 0:
        i += 1
    else:
        j -= 1

#################
# numere comune #
#################

"""
Fișierul text “numere_comune.in” conține numere naturale despărțite prin spații
și scrise pe mai multe linii. Să se afișeze pe ecran numerele care apar pe toate liniile din
fișier (folosind set + intersecție). Numerele vor fi afișate crescător.
"""
f = open('numere_comune.in', 'r')
mat = [[int(x) for x in line.split()] for line in f]
"""
mat = [line.split() for line in f]
for i in range(0, len(mat)):
    for j in range(0, len(mat[i])):
            mat[i][j] = int(mat[i][j])
"""

elm=[]
for i in mat[0]:

    nr = 0
    for j in range(1, len(mat)):
        if i in mat[j] and i not in elm:
            nr += 1

    if nr == len(mat) - 1:
        elm.append(i)

print(elm)

comune = set(mat[0])
for i in range(1, len(mat)):
    #comune = comune.intersection(mat[i])
    # comune = comune & set(mat[i])
    comune.intersection_update(mat[i])
print(*sorted(comune))
f.close()

f = open('numere_comune.in', 'r')
g=open("numere_comune.out","w")
comune={int(x) for x in f.readline().split()}
for linie in f:
    comune.intersection_update({int(x) for x in linie.split()})
print(*sorted(comune),file=g)
g.write("\n")
g.write(" ".join([str(x) for x in sorted(comune)]))
f.close()
g.close()

###################
# suvector suma k #
###################

v = [10, 1, 4, 7, 3, 2, 10, 1]
sum = 200
a = 0
b = 1
cur_sum = v[0]

while b < len(v):
    if cur_sum == sum:
        print(f"Secventa intre {a} si {b - 1} este {sum}")
        break
    if cur_sum < sum:
        cur_sum+= v[b]
        b+=1
    elif cur_sum > sum:
        cur_sum-= v[a]
        a+=1
else:
    print(f"Nu exista subsecventa care are suma {sum}")

####################
# Tema ksumarray_b #
####################

class Solution:
    def findSubarray(self, nums: list[int], k: int) -> bool:
        # Write your code here...

        pref_sum = 0 #suma subsecventei de la 0 la elementul de pe pozitia i
        set_prefix = set()  # multimea sumelor partiale de subsecvente deja obtinute
        for i in range(len(nums)):
            pref_sum += nums[i] #suma subsecventei creste la fiecare pas cu elementul curent

            if pref_sum == k: #daca am obtinut chiar suma k am gasit solutie
                return nums[:i + 1]
            if pref_sum - k in set_prefix: #caut daca exista o subsecventa de la 0 la o pozitie j mai mica decat i cu suma pref_sum - k in multime
                #daca exista - atunci am gasit o subsecv de suma k ( intre j+1 si i, dar nu putem afisa subsecventa deoarece in set am memorat doar sumele,
                #nu si pozitiile i asociate (vezi punctul c)
                return True
            set_prefix.add(pref_sum)
        return False
v=Solution()
print(v.findSubarray([10,1,7,4,3,5,12,10],14))

####################
# Tema ksumarray_c #
####################

class Solution:
    def findSubarray(self, nums: List[int], k: int) -> List[int]:
        # Write your code here...

        pref_sum = 0 #suma subsecventei de la 0 la elementul de pe pozitia i
        dict_prefix = {}  # dictionar de perechi de forma suma subsecv de la 0 la i : i
        for i in range(len(nums)):
            pref_sum += nums[i] #suma subsecventei creste la fiecare pas cu elementul curent

            if pref_sum == k: #daca am obtinut chiar suma k am gasit solutie
                return nums[:i + 1]
            if pref_sum - k in dict_prefix: #caut o subsecventa de la 0 la o pozitie j mai mica decat i cu suma pref_sum - k
                # caut suma in dictionar - cand o gasesc, valoarea asociata sumei este pozitia pe care se termina subsecventa (adica j)
                return nums[dict_prefix[pref_sum - k] + 1:i + 1] #subsecventa este de la j+1 la i
            dict_prefix[pref_sum] = i
        return []

#####################
# cuvinte personaje #
#####################

import re
def cheie(x): #x=(cuvant,multime personaje)
    return -len(x[1]),x[0]
d={}
f=open("teatru.in")
for linie in f:
    nume,replica=linie.split(": ")
    replica=replica.strip("\n")
    cuvinte=re.split("[ ,!?;]+",replica)
    print(nume,cuvinte)
    for cuv in cuvinte:
        cuv=cuv.lower()
        if len(cuv)>0:
            if cuv not in d:
                d[cuv]={nume}
            else:
                d[cuv].add(nume)
print(d)
ls=list(d.items())

ls.sort(key=cheie)
ls.sort(key=lambda x: (-len(x[1]),x[0]))

for cuv,personaje in ls:
    print(f"{cuv}: {' '.join(personaje)}")

for cheie in sorted(d,key = lambda x:(-len(d[x]),x)):
    print(f"{cheie}: {' '.join(d[cheie])}")
f.close()

#####################
# multimi distincte #
#####################

f=open("multimi.in","r")
s=set()
d={}
for linie in f:
    s1=frozenset(linie.split())
    if s1 not in d:
        d[s1]=1
    else:
        d[s1]+=1
    #{int(x) for x in linie.split()}
    s.add(s1)
print(s)
print(d)
print(len(s))
f.close()

###################################
# techie_LongestDistinctSubstring #
###################################

class Solution:
		def findLongestSubstring(self, s: str, k: int) -> str:
		
		startPosition = 0
		finPosition = 0
		totalLettersInCurSubstring = 0
		maxFinPos = 0
		maxStartPos = 0
		d = {}
		
		while finPosition < len(s):
			if s[finPosition] not in d:
				d[s[finPosition]] = 1
				totalLettersInCurSubstring += 1
			else:
				d[s[finPosition]] += 1
				
			while totalLettersInCurSubstring > k:
				d[s[startPosition]] -= 1
				startPosition += 1
				if d[s[startPosition-1]] == 0:
					totalLettersInCurSubstring -= 1
					del d[s[startPosition-1]]
					
			if totalLettersInCurSubstring == k:
				if maxFinPos - maxStartPos < finPosition - startPosition:
					maxFinPos = finPosition
					maxStartPos = startPosition
				
		
			finPosition += 1
			
		if totalLettersInCurSubstring <k:
			return s
		return	s[maxStartPos:maxFinPos+1]

##############################################
# techie_LongestDistinctSubstring_cu_pozitii #
##############################################

class Solution:
	def findLongestSubstring(self, s: str, k: int) -> str:
		# s = input()
		# k = int(input())
		d = {}
		n=len(s)
		kc=0
		start=0
		startl, lmax=0, 0
		for i in range(n):
		    if s[i] not in d and kc<k:
		        kc+=1
		    elif s[i] not in d and kc>=k:
		        if lmax<i-start:
		            lmax=i-start
		            startl=start
		        min_poz=min(d.values())
		        lit=[x for x in d if min_poz==d[x]]
		        del d[lit[0]]
		        start=min_poz+1
		    d[s[i]]=i
		    #print(d)
		#abdcbcdbdcbbc
		#print(start, n)
		if lmax<n-start:
		    lmax=n-start
		    startl=start
		if kc<k:
		    return s
		return s[startl:startl+lmax]

# Seminar 6 - 12 Decembrie 2024
# 1)

# a) 
def f (lista):
    if len(lista) <= 2:
        return sum(lista)
    k = len(lista) // 2
    aux = lista[:k] # -> O(nr de elem)
    return f(aux)
# Complexitate f(L) pt L lista cu n elem
# Vezi desenul din drive-ul lui Fabian!

# b)
def f (lista, p, u):
    if (u - p <= 2):
        return sum(lista[p:u+1])
    k = (u - p + 1) // 3
    aux_1 = sum(lista[p:p+k])
    aux_2 = f(lista, p + k + 1, p + 2 * k - 1)
    aux_3 = sum(lista[p + 2 * k + 1 : u + 1])
    return sum([aux_1, aux_2, aux_3])
# T(n) = 2T(n/2) + n
# interclasare, deci O(n * log n)
# Vezi desenul din drive-ul lui Fabian!
# La examen, arborele sau substitutie

# 2)
# Vector cu elem distincte
# Ni se da un vector sortat care a fost rotit nush cu cat, sa zicem cu 2 -> [3, 5, 7, 9, 12, 15] devine [7, 9, 12, 15, 3, 5]
# Trebuie sa sflam pe ce pozitie se afla un element