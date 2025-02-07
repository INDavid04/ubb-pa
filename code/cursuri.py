###############
# C1 Partea 1 #
###############

x=1
print(x, type(x))
x="abd"
print(x, type(x))
if x=="abc":
    print("nu")#plint("nu")
else:
    print("da",end=" ") #end - ce sir foloseste ca final, implicit-endline
    print("pauza")
print(x,"un sir", sep="=") #sep implicit spatiu
print(x,"un sir", sep=" este ") #sep implicit spatiu
x=input("dati x ") #str -pana la finalul liniei
x=int(x)
y=input("dati y ")
y=int(y)
print(x+y)

###############
# C1 Partea 2 #
###############

x=7
print(x,id(x))
x=x+1
print(x,id(x))

x=100
z=0
y=z+100
print(id(x),id(y))
x=1000
z=0
y=z+1000
print(id(x),id(y))
x=1234567891234566923
print(x,type(x))

"""
x=0.1
print(x*x)
print(x*x==0.01) #False - precizie
print(abs(x*x-0.01)<1e-8) #True
"""

#############################
# C2 Instructiuni atribuire #
#############################

x = y = 2
print(id(x), id(y))
x, y = 1, 2
print(x, y)
x, y = y, x  # de tupluri dreapta => tuplu, nu este echivalent cu x=y , y=x
print(x, y)

# if .. elif... else
# ultima cifra a lui 3**k
k = 8
if k % 4 == 0:
    print(1)
elif k % 4 == 1:
    print(3)
elif k % 4 == 2:
    print(9)
else:
    print(7)
# while
# for
# for var in secventa
s = "abc"
for litera in s:
    print(litera)
# range:
"""
range(n) -> 0,1,..n-1
range(a,b) -> a,a+1,...,b-1
range(a,b, pas)
"""
print(list(range(10, 1, -1)))
# break, continue
# else - si pentru structuri repetitive (se executa daca nu s-a iesit cu break)
"""
Sa se afiseze primul divizor propriu al lui n
"""
n = 25
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        print(i)
        break
else:
    print("nu are divizori proprii")

# pass
i = 0
for i in range(0, 4):
    print(i)
    # i=i+1
print(i)

################################
# C2 Secvente siruri. Cautarea #
################################

s="programarea"
print("a" in s)
print(s.count("a"))
print(s.count("a",6)) #numara incepand de la pozitia 5
print(s.count("a",6,10)) #numara incepand de la pozitia 5 pana la pozitia 10 exclusiv adica de ca s[5] pana la s[9]

#pozitii
p=s.index("a")
print(f"prima pozitie {p}")
p=s.index("a",p+1)
print(f"a doua pozitie {p}")

try:
    p=s.index("b") #eroare daca elementul nu este gasit
    print(f"prima pozitie {p}")
except ValueError:
    pass
print("ok")

#exc: sa se afiseze toate pozitiile pe care apare "a" in s
p=s.index("a")
try:
    while True:
        print(p)
        p=s.index("a",p+1)
except:
    pass

#doar pt siruri -find - returneaza -1 daca elementul nu este gasit
p=s.find("a")
while p!=-1:
    print(p)
    p=s.find("a",p+1)

#rfind, rindex - cauta de la dr la stg (ultima aparite) - doar pt siruri
p=s.rfind("a")
print(f"ultima pozitie {p}")

#concatenari => obiect nou
s=s[:3]+" "+s[5:]
print(s)
n=7
s="a"*n
print(s)
v=[0]*n
print(v)

#sorted -> returneaza lista
v=[9,4,6,7]
v_sortat=sorted(v)
print(v_sortat,v)
s="mare"
s_sortat=sorted(s)
print(s_sortat)
#---- siruri caractere - unificari/separari
#separator.join(secventa de cuvinte)
ls=["programarea", "algoritmilor", "seria", "14"]
s=" ".join(ls)
print(ls)
print(s)
s="_".join(ls)
print(s)
cuv="".join(s_sortat)
print(cuv)

#sir.split(separator) -> lista de cuvinte
#daca nu se specifica separator - caractere albe
s="programrea algoritmilor    seria 14"
ls=s.split()
print(" ".join(ls))
print(ls)
ls=s.split(" ")
print(ls)
print(" ".join(ls))

############
# C3 Array # @ TODO: contiune from here;
############

"""
clasa list- vector (array)
elminarea primului elelemnt -> O(n)

"""
ls=[1,"abc",[3,4]] #imbricate, pot fi neomogene
m=[[2,3],[5,6]]
#lista vida
ls=[]
ls=list()
#list(iterabil)->lista (cu fiecare element din iterabil)
ls=list(range(6))
print(ls)
ls=list("un cuvant") #sir elemnt=o litera
print(ls) #lista de litere

#Se pot initializa cu comprehensiune (list comprehension)
#Exc - o lista cu primele n patrate perfecte
n=5
ls=[]
for i in range(1,n+1):
    ls.append(i*i) #append - adauga un element la finalul listei
print(ls)

#ls=[expresie for element in iterabil]
ls1=[i*i for i in range(1,n+1)]
print(ls1)

##sa se creeze un vector cu n elemente egale cu 0
v=[0]*n
v[0]=1
print(v)
v=[]
for i in range(n):
    v.append(0)
v=[0 for i in range(n)]
v[0]=3
print(v)
#se se citeasca un vector de numere intregi cu elementele date pe o linie
#9 0 23 4 7
v=input().split()
print(v)
"""
for x in v:
    x=int(x) #nu se modifica v
print(v)
"""
for i in range(len(v)):
    v[i]=int(v[i])
print(v)

v=[int(x) for x in input().split() ]
print(v)

#citim 2 numere pe aceeasi linie
m,n=[int(x) for x in input("dati doua numere ").split() ]
print(m+n)

#Comprehensiune conditionata:
#[expresie for elem in iterabil if conditie]
#Exp: sa se creeze o lista cu elementele pozitive ale unei liste date
ls=[4,5,-1,7,3,-8,9]
ls_pozitiv=[]
for x in ls:
    if x>0:
        ls_pozitiv.append(x)
print(ls_pozitiv)
ls_pozitiv=[x for x in ls if x>0]
print(ls_pozitiv)

#exc: se dau doua liste reprezentand multimi
#sa se creeze o noua lista cu intersectia celor doua multimi
a=[3,1,5,7]
b=[1,7,2,9,11]
c=[x for x in a if x in b]
print(c)

##se da un cuvant, sa se stearga vocalele din cuvant => un nou cuvant
s="programarea"
ls=[lit for lit in s if lit.lower() not in "aeiou"]
print(ls)
s_consoane="".join(ls)
print(s_consoane)
"""
    for x in "aeiou"
        s=s.replace(x,"")
"""

#in comprehensiune expresie poate contine si operatorul if... else (?:)
#exp: Data o lista, sa se creeze o noua lista in care elementele negative
#din lista initiala sunt inlocuite cu 0
ls=[8,1,-5,7,-2,-3]
ls2=[x if x>0 else 0 for x in ls]
print(ls2)

#for in for
ls_perechi=[(x,y) for x in range(1,7) for y in range(1,7) if x%2==0 and y%2==0]
print(ls_perechi)

#EXp - cifrul lui Cezar pt k=1 si litere mici
s="abz" #=>bca
s_cezar="".join([chr(ord(lit)+1) if lit<'z' else 'a' for lit in s])
print(s_cezar)
"""
lit="c"
if lit<'z':
    lit=chr(ord(lit)+1)
else:
    lit='a'
"""

# In continuare, curs3_liste_modificare
"""
append(element) -> adaugarea elementului la final
extend(iterabil) -> adauga elementele din iterabil unul cate unul
    la finalul listei
"""
ls=[3,4]
ls.append(5)
print(ls)
ls.extend([7,8,9])
print(ls)
ls.append("abc")
print(ls)
ls.extend("abc")
print(ls)

#Modifcarea listei - cu felieri
"""
ls[i]=x
ls[i:j]=iterabil (care nu are neaparat aceeasi lungime cu secv ls[i:j]
ls[i:j:k]=iterabil (de aceeasi lungime)
"""
ls=[1,2,3,4]
ls[1:3]=[5]
print(ls)
ls=[1,2,3,4,5,6]
ls2=[11,12,13,14,15,16]
ls[::2]=ls2[::2]
print(ls)
#adaugarea unui element x in lista pe pozitia i
#insert(i,element)
ls=[6,8,9]
ls.insert(1,7)
print(ls)
ls[1:2]=[17] #inlocuirea ui ls[1]
print(ls)
ls[1:1]=[18] #inserare pe pozitia 1
print(ls)
#del ls[i:j]
#del ls[i]
#metode: pop(pozitie), insert(poz,element)
#liste - remove(x) - elimina doar prima aparitie a lui x din lista
ls=[1,2,3,4]
ls[2]=[]
print(ls)
ls[2:3]=[]
print(ls)
del ls[2]
print(ls)

ls=ls+[4] #NU
#copiere
l=[7,8]
l1=l #nume pentru aceeasi lista
l1[0]=9
print(l1,l)
l1=l.copy()
l1[0]=11
print(l1,l)
m=[[1,2],[4,5]]
m1=m.copy() #copiere superficiala -doar de referinta
m1[0][0]=13
print(m1)
print(m)

# In continuare, curs3_siruri_completare

#SIRURI - continuare
#split - are si parametrul maxsplit = cate imparitire sa faca maxim
p="acesta este un exemplu"
lp=p.split(" ")
print(lp)
lp=p.split(" ",maxsplit=1)
print(lp)
#rsplit

#exemplu - pe o line de forma nume varsta. Sa se afiseze varsta e o linie, numele pe alta
p="Marinescu Ghemeci Ruxandra  36"
lp=p.rsplit(maxsplit=1)
print(lp)
print(int(lp[1]))
print(lp[0])

#exemplu coordonatele carteziebne si eticheta
p="3 7 acesta este un punct in plan"
ls=p.split(maxsplit=2)
x=int(ls[0])
y=int(ls[1])
eticheta=ls[2]
print(f"({x},{y}) are \"eticheta {eticheta}\"")
print(f'({x},{y}) are "eticheta {eticheta}" ')

#ord, chr
#caractere UNICODE
#Modificari -> obiect nou

#s=s.replace(sect,sect_noua,cate_aparitii) - v. laborator
s="un exemplu"
s1=s.replace("u","")
print(s1)
s2=s.replace("u","",1)
print(s2)
x="am mancat"
y="am "+"mancat"
print(x,y,id(x),id(y))
z=input()
w="am "+z
print(x,w,id(x),id(w))
x=w
print(x,w,id(x),id(w))

########################
# C4 Matrice init cu 0 #
########################

#initializam o matrice de 0 de dimnesniuni n,m
print("var 1 - gresit")
n,m=2,3
a=[[0]*m]*n
print(a)
a[0][0]=1
print(a)
print("var 2 - corect")
a=[[0 for i in range(m)] for j in range(n)]
print(a)
a[0][0]=1
print(a)
print("var 3 - gresit")
a=[[0 for i in range(m)]]*n
print(a)
a[0][0]=1
print(a)
print("var 4")
a=[[0]*m for j in range(n)]
print(a)
a[0][0]=1
print(a)
#rec- var 2
#operatorii <,<=,==, != - element cu element
ls=[1,2,4]
ls2=[3,1]
print(ls<ls2) #!!compar element cu element, deci ls2 e mai mare
#deoarece ls2[0]>ls[0]
print([1,3]==[3,1]) #fals

#sort vs sorted
ls=[7,1,5]
ls_sort=sorted(ls) #returneaza o noua lista
print(ls_sort,ls) #ls nu se modifica
ls.sort(reverse=True) #!!!nu retunreaza, modifca ls
print(ls)
m=[[6,9],[3,1],[1,11]]
m.sort()
"""(elemente sunt liste corespunzatoare liniilor)
sunt comparate aceste liste => crescator dupa prima coloana 
prin interschimbare de linii"""
print(m)
##############
# C4 Tupluri #
##############

#tuplu - clasa tuple
#"lista imutabila"
t=(6,4,8)
print(t,type(t))
#t[0]=13 #eroare does not support item assignment
#nu putem modifica ce refera t[0]
t=([8,5],[9,11])
#pputem modifica valoarea obiectlui referit de t[0]
t[0][0]=123
print(t)

#parantezele pot lipsi
t=5,6
print(t,type(t))
x,y=1,2
x,y=y,x
t=()
t=(2) #nu este tuplu
print(t,type(t))
t=(2,) #tuplu cu un element
print(t,type(t))
t=tuple('abc')
print(t)
t=tuple([2])
print(t,type(t))
#toate metode,  totii operatori - de la liste in afara celor care modifica ob
#in, count,len, idex, feliere
#!!NU comprehensiune
t=[i*i for i in range(1,10)] #list
print(t,type(t))
print(sum(t))
print(sum(t))
t=(i*i for i in range(1,10)) #nu e tuple
print(t, type(t)) #este generator
#genereaza "la crere" elemente dupa regula din copmprehsion
print(next(t))
print(next(t))
print(sum(t))
print(sum(t)) #!!0

################
# C4 Frecvente #
################

"""
Exp -> se citeste un sir de cifre
sa se afiseze frecventa fiecarei cifre in sir
"""
"""
v=[int(x) for x in input("dati sirul ").split()]
fr=[0]*10
for x in v:
    fr[x]+=1
for i in range(10):
    if fr[i]!=0:
        print(i,fr[i])
"""
"""
Exp -> se citeste o propozitie cu cuv separate prin spatiu 
sa se afiseze frecventa fiecarui cucvant din propozitie
un exemplu un alt exemplu
un 2
alt 1
exemplu 2
"""
#struct de date indexate dupa alt tip de cheie


d={} #frecv - alta structura - dictionar
p="un exemplu un alt exemplu"
for cuv in p.split():
    if cuv in d:
        d[cuv]+=1
    else:
        d[cuv]=1
for cuv in d:
    #if d[cuv]!=0: - nu este necesar
    print(cuv,d[cuv])
"""
Solutie de o(n^2) un de n=nr de cuvinte"""
l=p.split()
l_dist=set(l)
print(l_dist)
#l1=[(l[i],l.count(l[i])) for i in range(len(l)) if l.count(l[i])>0] - se repeta cuv
l1=[(cuv,l.count(cuv)) for cuv in l_dist ]
print(l1)

#########################
# C4 Multimi dictionare #
#########################

#Alte tipuri de colectii in Python
"""
Multmi, dictionare - sunt mmem cu tabele de dispersie
(tabele"de frcventa" indexate"" dupa chei care au asociate o valoare numerica (hash code)
Hash code depinde de valoarea obiectui => cheile pot fi doar de tipuri imutabile
(Care nu isi pot schimba valoarea))
"""
#cheie -> hash -> index in tabel
#t[index] - informatii despre toate cheile care au acelasi index
"""
ob cu aceeasi valoare => acelasi hash
ob cu valori difertite - poate avea acelasi hash (coliziuni)
Obs: Cautarea si stergrea in astfel de struct O(1) mediu (!!coliziuni)
"""

#MULTIMI
"""
Colectii de ob cu valori diferite
Nu sunt indexate de la 0 !!!!
elemntele din multime - tb sa fie imutabile+ sa aiba hash code
"""
s={6,1,3,1}
print(s) #ordine ain s- nu este garantata a fi cea de la adaugare/creare}
cuv="alfabet"
#multimea literelor din cuv
s=set(cuv)
print(s)
#s={[3,4],[5,6]} #unhashable type: 'list'
print(hash(cuv))

#operatii , incluziune
#op relationali - testeaza incluziunea < (stict inclus), <=
s1={3,1,5}
s2={1,5}
print(s2<s1) #s2 est inclus in s1 => adev
#op cu multimi - si operatori si metode
# (care modifica ob/returneaza rezultatul)
"""
reuniune:
operatorul |
metoda care returneaza mult obtinuta dupa reuniune: union
metoda care modifica ob: update
intersectie: & , intersection, intersection_update
"""
s1={4,5,6}
s2={6,7}
s3={5,11}
r=s1|s2|s3 #se pot inlantui
print(r)
r=s1.union(s2,s3,[7,34,78]) #metode- param pot sa fie si de alt tip decat set
print(r)
r.intersection_update({5,6,11,110}) #modifica r
print(r)
#multimea vida
#s={}#nu- dictionar
s=set()
#len, sorted,min, max
#NU s[i]

s={{1,3},{2,4,5}}
#set se poate modifica - add, remove, discard de un element
#->nu exista set de set-uri
#exista tipul de date frozenset

#######################
# C4 Liste completare #
#######################

#COPIERE
#copiere
l=[7,8]
l1=l #nume pentru aceeasi lista
l1[0]=9
print(l1,l)
l1=l.copy()
l1[0]=11
print(l1,l)
m=[[1,2],[4,5]]
m1=m.copy() #copiere superficiala -doar de referinta
m1[0][0]=13
print(m1)
print(m)
import copy
m2=copy.deepcopy(m)
m[0][0]=100
print(m)
print(m2)

#EXP - citrea unei matrice cu elementele de pe o linie date
#separate cu spatiu; dimenisiunile matricei - date separate
# cu spatiu pe olinie
"""
2 3
1 4 6
3 67 10
"""
#Matrice -lista de liste
#un element al listei - o linie
n,m=[int(x) for x in input("dati dimensiunile ").split()]
"""
a=[]
for i in range(n):
    linie=[int(x) for x in input().split()]
    a.append(linie)
"""
#citirea matrice - cu comprehension
a=[[int(x) for x in input().split()] for i in range(n)]

print(a)
for linie in a:
    for x in linie:
        print(x, end=" ")
    print()
#stil c++
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
    print()
#inint cu 0 -in alt fisier

##################
# C5 Dict puncte #
##################

"""
Se dau informatii de despre puncte in plan
x y eticheta
(in fisierul puncte.in)
a) Sa se memoreze punctele cu etichete intr-un dictionar
b) se citesc coordonatele unui punct, sa se afiseze eticheta acestuia
c) se citesc coordonatele unui punct, sa se stearga informatiile asociate lui
"""
#a)var 1- se pastreaza ca eticheta pentru un punct ultima eticheta
# (cea mai recenta)
f=open("puncte.in") #pt citire - implicit
d={}
for linie in f: #f este colectie de linii
    x,y,eticheta=linie.split(maxsplit=2)
    x=int(x)
    y=int(y)
    #eticheta=eticheta.strip("\n")  #elimina \n de la capetele sirului pana gaseste alt caracter
    #p=[x,y] #TypeError: unhashable type: 'list'
    p=(x,y)

    if p not in d: #doar pt var 2
        d[p]=eticheta.strip("\n")
    d.setdefault(p,eticheta) #doar pt var 2
f.close()
print(d)
#b)
#p=(int(x) for x in input().split()) #nu este tuplu
a,b=(int(x) for x in input().split())
t=(a,b)
if t in d: #cauta t in cheile lui d
    print(d[t])
else:
    print("nu exista punctul ",t)
#alternativ, fara if- puteam folosi get
print(d.get(t,"nu exista"))


#stergere
if t in d:
    del d[t]
print(f"am sters {d.pop(t," nimic ")}")

#var 2 la citire - sa pastreze prima eticheta (alte etichete ale aceluiasi punct- ignora)

##############################
# C5 Puncte toate etichetele #
##############################

"""
Se dau informatii de despre puncte in plan
x y eticheta
(in fisierul puncte.in)
a) Sa se memoreze punctele cu etichete intr-un dictionar
b) se citesc coordonatele unui punct, sa se afiseze eticheta acestuia
c) se citesc coordonatele unui punct, sa se stearga informatiile asociate lui
"""
#a)var 3- se pastreaza ca eticheta toate etichetele
# (cea mai recenta)
f=open("puncte.in") #pt citire - implicit
d={}
for linie in f: #f este colectie de linii
    x,y,eticheta=linie.split(maxsplit=2)
    x=int(x)
    y=int(y)
    eticheta=eticheta.strip("\n")  #elimina \n de la capetele sirului pana gaseste alt caracter
    #p=[x,y] #TypeError: unhashable type: 'list'
    p=(x,y)

    if p not in d: #doar pt var 2
        d[p]=[eticheta] #!!!lista cu o eticheta
    else:
        d[p].append(eticheta)
    """
    if p not in d: #doar pt var 2
        d[p]=[] #!!!lista 
    d[p].append(eticheta)
    """
f.close()
print(d)
#b)
#p=(int(x) for x in input().split()) #nu este tuplu
a,b=(int(x) for x in input().split())
t=(a,b)
if t in d: #cauta t in cheile lui d
    print(d[t])
else:
    print("nu exista punctul ",t)
#alternativ, fara if- puteam folosi get
print(d.get(t,"nu exista"))


#stergere
if t in d:
    del d[t]
print(f"am sters {d.pop(t," nimic ")}")

#var 2 la citire - sa pastreze prima eticheta (alte etichete ale aceluiasi punct- ignora)

############################
# C5 Dictionare parcurgere #
############################

d1={"unu":6,"doi":3,"trei":4}
d2={"unu":5,"doi":7,"patru":3}
print(d1.keys())
print(d1.values())
print(d1.items())
#implicit - parcurse cheile
for x in d1:
    print(x,d1[x])
print(sorted(d1))
#d.keys()- operatori cu multimi &,|
#Exp d1, d2- dictionare cu frecv cuv in 2 fisiere
#sa se afiseze cuv din cel doua fisiere reunie cu frecv lor
# sa se afiseze cuv din intersectie cu frec lor
d1={"unu":6,"doi":3,"trei":4}
d2={"unu":5,"doi":7,"patru":3}
d_reunit={k:d1.get(k,0)+d2.get(k,0)  for k in d1.keys()|d2.keys()}
#d_reunit={k:d1[k]+d2[k]  for k in d1.keys()|d2.keys()}
print(d_reunit)
d_intersect={k:min(d1[k],d2[k]) for k in d1.keys()&d2.keys()}
print(d_intersect)

##############
# C5 Functii #
##############

def f(x,y): #antet, x,y- param formali
    if x>y:
        return x-y, x*y #putem returna mai multe valori => tuplu
    else:
        return y-x, x*y
    #daca nu returneaza explicit val, implicit returneaza None

def afis(x,y):
    print(x,y)

t=f(3,4)
print(t,type(t))
a,b= f(3,4)
print(a,b)
x=afis(a,b)
print(x) #None

v=[5,1,6]
ls=sorted(v)
print(ls)
ls=v.sort()
print(ls)
v=v.sort() #!!!NU - v devine None
print(v)

#transmiterea parametrilor - prin atribuire
# (param formal= parm actual (param formal - vairabila locala)
def modifica(x):
    x=x+1
    print(x)
    print(locals())
a=8
modifica(a)
print(a)
"""
x=8
modifica(x)
print(x)
"""

def modificare_lista(ls):
    ls.append(6)
v=[7,8]
modificare_lista(v)
print(v)
def creare(v):
    v=[0]*10
v=[]
creare(v)
print(v)
#dupa exec fct se vad doar modificarile facute asupra
# valorii unui param mutabil ("deja alocat")

#################
# C5 Dictionare #
#################

#dict -dictionar
"""
memoreaza perechi cheie:valoare ai cautarea dupa cheie O(1) mediu
(si stergerea cheii (impreuna cu valoarea asociata)
"""
#Creare
d={"un":2,"cuvant":1}
print(d,type(d))
d={} #!!!dictionar vid, nu set vid
#Obs: cheia - imutabila + cu hash
#valoarea poate fi de orice tip
#pot fi chei in dict /elemente in set: str, tuple, frozenset
#nu pot fi chei: list, set

#se poate crea dict/set cu comprehensiune
s="abcdab"
d={lit:0 for lit in s}
print(d)
d={lit:s.count(lit) for lit in s} #ineficient -o(n2) - v curs trecut
print(d)
#si set se poate crea cu comprehensiune (completare la set)
#sa se determine multima cuvintelor cu cel putin k litere dintr-o propozite:
prop="aceasta este o propozitie aceasta"
k=5
s={w for w in prop.split() if len(w)>=k}
print(s)

#accesarea unui element din dictionar - dupa cheie
#d[cheie]- returneaza valoarea asociata cheii/KeyError daca nu exista cheia in dictionar
d={"un":2,"cuvant":1}
print(d["un"])
#d.get(cheie,valoare_default)- daca nu gaseste cheia
# returneaza valoare_default
print(d.get("trei","nu exista"))

#ACTUALIZARE
#d[cheie]=valoare -> daca nu exista cheie in dict,se adauga cheie:valoare,
#daca exista cheie - se modifica valoarea asociata
d={"un":2,"cuvant":1}
d["un"]=5
d["unu"]=1
print(d)

#d.setdefault(cheie,valoare) - adauga daca nu exista in dictionar cheie
#perechea cheie:valoare

#stergerea unei cheii (a perechii cheie:valoare
#del d[cheie]
#d.pop(cheie,valoare_default)
#d.clear()

####################
# C6 Functii part1 #
####################

"""
Tipuri de paramterii
"""

"""
1. Param obligatorii - trebuie sa primeasca valaore la apel
Se pot da
-prin pozitie (in ordinea in care sunt in antet 
-prin nume (nume_param_formal=)
- combinat - dar primii se dau cei prin pozitii
"""
def f(x,y,z):
    print(x,y,z)
f(3,4,5)
f(z=7,x=9,y=8) #prin nume-in orice ordine
f(3,z=89,y=2)

"""
2. Param cu valoare implcita - atribuita in antet
Daca la apel nu ii coresp o valoare, este folosita cea implicita
la final in antet
"""
def f(x,y,z=9):
    print(x,y,z)
f(7,8) #pentru z se foloseste valoare implicita

"""
3. Functii cu numar variabil de parametrii:
- in antet unul dintre parametri este prefixat de *
*parametru 
"""

def f(*numere):
    print(numere, type(numere))
    l=list(numere)
    print(l, type(l))
f(1,2)
f(1,2,3)
f(1,2,3,4)

#!!!parametrii de dupa cel cu * trebuie dati prin nume

#exemplu - suma numerelor primite ca param, dintr-un interval dat
def suma(*numere, lim_inf,lim_sup):
    s=0
    for nr in numere:
        if lim_inf<=nr<=lim_sup:
            s+=nr
    s=sum(nr for nr in numere if lim_inf<=nr<=lim_sup)
    return s

s=suma(100,45,79,105, lim_inf=50, lim_sup=100) #cei de dupa- prin nume
print(s)

#parametrii de dupa * pot avea si valoare implicita
def suma(*numere, lim_inf=0,lim_sup=100):
    s = sum(nr for nr in numere if lim_inf <= nr <= lim_sup)
    return s
s=suma(100,45,79,105, lim_sup=50) #lim_inf- s-a cons valoarea default
print(s)

#putem transmite ca parametrii si functii
#exp: suma generica suma(f(x) pentru numerele x primite ca param
#si funtia f primita ca param
def suma(*numere, f=int):
    s=0
    for nr in numere:
        s+=f(nr)
    return s
def finvers(x):
    return 1/x
import math
r=suma(9,16,100, f=math.sqrt)
print(r)
r=suma(9,16,100, f=finvers)
print(r)
r=suma(9,16,100) #lipseste f la apel -implicit int
print(r)

#map(f,lista) -> f aplicat elementelor listei
ls=["70",8,"90"]
#v=[int(x) for x in ls]

v=map(int,ls) #aplica functia fiecarui element
v=list(v)
print(v)
"""
filter(criteriu,lista) -> 
doar elementele din lista care verifica criteriul
unde criteriu - functie care returneaza True/False
"""
#Exp:
ls=[8,12,7,9,10]
#lista cu elementele pare
lsp=[x for x in ls if x%2==0]
def f(x):
    return x%2==0
lsp=list(filter(f,ls))
print(lsp)

#sortari
ls=["cuv","un","altul","doi","cinci","ab"]
#sort lista de cuvinte crescator dupa lungime si in caz de egalitate
#crescator lexicografic
#OBS: sortarea din python este stabila =
#doua elemente egale dupa sortare pastreaza ordinea din sirul initial

#Avem 2 criterii de sortare 1)llung, 2)lexicogr:
#var1- folosim sort de 2 ori, pentru criteriile in ordine inversa:
#sortam lexicografic !!sortare stabila
ls.sort()
#sortam dupa lungime
ls.sort(key=len) #keycheia de sortare key(v[i])
print(ls)

#var 2
ls=["cuv","un","altul","doi","cinci","ab"]
def f(x): #elementele se compara dupa f(v[i])
    #returnam un tuplu, fiecare element din tuplu corespunde unui criteriu
    #primul elemnt din ltuplu - primul criteriu)
    return len(x),x

ls.sort(key=f)
print(ls)

#functii fara nume
ls=["cuv","un","altul","doi","cinci","ab"]
ls.sort(key= lambda x:(len(x),x)) #lambda x : cheie asociata lui x)
print(ls)

####################
# C6 Functii part2 #
####################

"""
Recursivitate
"""
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
print(fact(50))
print(fact(70))
import sys
sys.setrecursionlimit(2000)
print(fact(1090))

###############################
# C6 Functii part3 continuare #
###############################

"""
FUNCTII-continuare
"""
#domeniul de vizibilitate pentru o variabila

"""
La accesara valorii unei variabile- este cautata is spatiul local 
si apoi in global (cautata dupa regula LEGB - local, enclonsing, 
global, builtin)
"""
def f():
    #spatiul local
    print(x)

x=9 #spatiul global
f()

#la actualizare:
"""
o variabila incepe sa existe la prima atribuire
(este creata in spatiul (domeniul) unde se face atribuirea,
daca nu exista)
"""
def f():
   y=7 #devine variabila locala (este prima atribuire in local)
   print(y)
   print(locals())
y=8
f()
print(y)

#putem preciza spatiul(domeniul) in care se cauta o variabila la atriburie
def f():
   global z #la atribuire - z din global
   z=7
   print(z)
   print(locals())
z=8
f()
print(z)

#####################
# C6 Structuri date #
#####################

ls_nr = [int(x) for x in input().split()]
print("stiva")
stiva = []
for x in ls_nr:
    stiva.append(x)
for i in range(2):
    if len(stiva)>0:
        print(stiva.pop(),end= " ")#extrage ultimul element adaugat
print("\ncoada")
import collections
coada = collections.deque()
for x in ls_nr:
    coada.append(x)
for i in range(2):
    if len(coada) > 0:
        print(coada.popleft(), end=" ") #extrage primul element adaugat
print("\ncoada 2: ")
import queue
coada = queue.Queue()
for x in ls_nr:
    coada.put(x)
for i in range(2):
    if coada.qsize() > 0:
        print(coada.get(), end=" ")#extrage primul element adaugat

print("\ncoada prioritati 1: ")
import heapq

h = [] #un heap este un vector
for x in ls_nr:
    heapq.heappush(h,x)
for i in range(2):
    if len(h) > 0:
        print(heapq.heappop(h),end=" ") #extrage elementul minim

import queue
print("\ncoada prioritati 2: ")
coada = queue.PriorityQueue()
for x in ls_nr:
    coada.put(x)
for i in range(2):
    if coada.qsize() > 0:
        print(coada.get(),end=" ")#extrage elementul minim

###################
# C10 DI_AlKMinim #
###################

from random import randint


def citire_vector(nume_fisier):
    f = open(nume_fisier)
    ls = [int(x) for x in f.read().split()]
    k = int(input("k="))
    return k, ls


def poz_rand(v, p, u):
    r = randint(p, u)
    v[r], v[p] = v[p], v[r]
    return poz(v, p, u)


def poz(v, p, u):
    i = p
    j = u
    depli = 0
    deplj = -1
    while i < j:
        if v[i] > v[j]:
            v[i], v[j] = v[j], v[i]
            # depli, deplj = -deplj, -depli
            aux = depli
            depli = -deplj
            deplj = -aux
        i += depli
        j += deplj

    return i


def sel_k_min(v, k, p, u):
    m = poz_rand(v, p, u)

    if m == k - 1:
        return v[m]
    if m < k - 1:
        return sel_k_min(v, k, m + 1, u)
    return sel_k_min(v, k, p, m - 1)


def sel_k_min_di(v, k):
    return sel_k_min(v, k, 0, len(v) - 1)


k, v = citire_vector("interclasare.in")
print(k, v)
print(sel_k_min_di(v, k))

#########################
# C10 DI_Cautare_Binara #
#########################

def citire_vector_ordonat(nume_fisier):
    f=open(nume_fisier)
    ls=[int(x) for x in f.read().split()]
    return ls


def cautare_binara(x,ls,p,u):
    if p > u:
        return (False,u)
    else:
        mij = (p + u) // 2
        if x == ls[mij]:
            return (True,mij)
        elif x < ls[mij]:
            return cautare_binara(x,ls, p, mij-1)
        else:
            return cautare_binara(x,ls, mij+1, u)

def cautare_binara_nerecursiv(x,ls):
    p=0
    u=len(ls)-1
    while p<=u:
        mij = (p + u) // 2
        if x == ls[mij]:
            return (True, mij)
        elif x < ls[mij]:
            u = mij - 1
        else:
            p = mij + 1
    return (False,u)

def cautare(x,ls):
    n = len(ls)
    return cautare_binara(x,ls,0,n-1)

def cautare(x,ls):
    n=len(ls)
    return cautare_binara(x,ls,0,n-1)

ls=citire_vector_ordonat("vector.in")
x=int(input("Dati valoarea cautata "))
rez=cautare(x,ls)
if rez[0]:
    print(f"{x} gasit pe pozitia {rez[1]}")
else:
    print(f"{x} nu este in vector {rez[1]}")

rez=cautare_binara_nerecursiv(x,ls)
if rez[0]:
    print(f"{x} gasit pe pozitia {rez[1]}")
else:
    print(f"{x} nu este in vector {rez[1]}")

####################
# C10 DI_QuickSort #
####################

from random import randint

def citire_vector(nume_fisier):
    f = open(nume_fisier)
    ls = [int(x) for x in f.read().split()]

    return ls

def poz_rand(v, p, u):
    r = randint(p, u)
    v[r], v[p] = v[p], v[r]
    return poz(v, p, u)

def poz(v, p, u):
    i = p
    j = u
    depli = 0
    deplj = -1
    while i < j:
        if v[i] > v[j]:
            v[i], v[j] = v[j], v[i]
            depli, deplj = -deplj, -depli
            #aux = depli;  depli = -deplj; deplj = -aux
        i += depli
        j += deplj

    return i

def quick_sort_di(v, p, u):

    if p >= u:
        return
    m = poz_rand(v, p, u)
    #m = poz(v, p, u)
    quick_sort_di(v, p, m - 1)
    quick_sort_di(v, m + 1, u)

def quick_sort(v):
    return quick_sort_di(v, 0, len(v) - 1)

v = citire_vector("interclasare.in")
quick_sort(v)
print(v)

#######################
# C10 DI_suma_matrice #
#######################

def citire_matrice(nume_fisier):
    f=open(nume_fisier)
    m=[]
    for linie in f:
        m.append([int(x) for x in linie.split()])
    f.close()
    return m

def suma(m,x,y,n):
    print(x,y)
    if n==1:
        return m[x][y] #!!da eroare cu n/2, e de tip float

    s1 = suma(m, x, y, n//2)
    s2 = suma(m, x+n//2, y, n//2)
    s3 = suma(m, x, y+n//2, n//2)
    s4 = suma(m, x+n//2, y+n//2, n//2)
    return s1+s2+s3+s4

def suma_matrice(m):
    return suma(m,0,0,len(m))
m=citire_matrice("matrice.in")
s=0
for linie in m:
    s=s+sum(linie)
print(s)
print(suma_matrice(m))

########################################
# C10 mediana_2_vectori_leetcode_var_1 #
########################################

class Solution:
    def mediana(self, v, pv, uv):
        n = uv - pv + 1
        m = (uv + pv) // 2
        if n % 2 == 0:
            return (v[m] + v[m + 1]) / 2
        else:
            return v[m]

    def calculMediana(self, pa, ua, pb, ub, a, b, r):
        print(pa, ua, pb, ub)
        n = ua - pa + 1
        m = (pb + ub) // 2
        #calcul direct pentru n=1,2- in functie de pozitia lui a[pa] in b fata de mediana
        if n == 0:
            return self.mediana(b, pb, ub)
        if n == 1:
            if r == 1:
                if a[pa] <= b[m]:
                    return b[m]
                elif b[m] <= a[pa] <= b[m + 1]:
                    return a[pa]
                else:
                    return min(b[m + 1], a[pa])
            else:
                if pb == ub:
                    return (a[pa] + b[pb]) / 2.0
                v = [a[pa], b[m], b[m + 1], b[m - 1]]
                return (sum(v) - min(v) - max(v)) / 2.0
        if n == 2:
            if r == 1:
                if a[pa] <= b[m] <= a[ua]:
                    return b[m]
                elif a[ua] <= b[m]:
                    return max(b[m - 1], a[ua])
                else:
                    return min(b[m + 1], a[pa])
            else:
                if a[ua] <= b[m]:
                    if m > 0:
                        return (max(b[m - 1], a[ua]) + b[m]) / 2.0
                    else:
                        return (a[ua] + b[m]) / 2.0
                elif a[pa] >= b[m + 1]:
                    if m + 2 <= ub:
                        return (b[m + 1] + min(b[m + 2], a[pa])) / 2.0
                    else:
                        return (a[pa] + b[m + 1]) / 2.0
                else:
                    return (max(a[pa], b[m]) + min(a[ua], b[m + 1])) / 2.0

        m1 = self.mediana(a, pa, ua)
        m2 = self.mediana(b, pb, ub)

        if m1 == m2:
            return m1
        if m1 > m2: #renuntam la acelasi numar de elemente
            return self.calculMediana(pa, pa + n // 2, pb + (n - 1) // 2, ub, a, b, r)
        else:
            return self.calculMediana(pa + (n - 1) // 2, ua, pb, ub - (n - 1) // 2, a, b, r)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1
        b = nums2
        n = len(a)
        m = len(b)
        if n > m:
            a, b = b, a
            n, m = m, n
        return self.calculMediana(0, n - 1, 0, m - 1, a, b, (m + n) % 2)

########################################
# C10 mediana_2_vectori_leetcode_var_2 #
########################################

class Solution:
    def getMedianBS(self,a,b,pa,ua): #a mai mic, in a cautam pe x
        n1, n2 = len(a), len(b)
        if pa<=ua:
            x = (pa + ua) // 2
            y = (n1 + n2 + 1) // 2 - x
            ax_1 = float("-inf") if x == 0 else a[x - 1] #bordam vectorii cu -∞, +∞
            by_1 = float("-inf") if y == 0 else b[y - 1]
            ax = float("inf") if x == n1 else a[x]
            by = float("inf") if y == n2 else b[y]
            if ax_1 <= by and by_1 <= ax:
                if (n1 + n2) % 2 == 0:
                    return (max(ax_1, by_1)+min(ax, by))/2
                else:
                    return max(ax_1, by_1)
            elif ax_1 > by:
                return self.getMedianBS(a,b,pa,x - 1)
            else:
                return self.getMedianBS(a,b,x+1,ua)

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        return self.getMedianBS(nums1,nums2,0,n1) #bordat vectorul cu inf - o pozitie in plus

############################
# C10 sortare_interclasare #
############################

def interclasare(v,p,m,u): #v[p...m] se interclaseaza cu v[m+1...u]
    b=[0]*(u-p+1)
    i=p
    j=m+1
    k=0
    while i<=m and j<=u:
        if v[i]>v[j]:
            b[k]=v[j]
            j+=1
            k += 1
        else:
            b[k] = v[i]
            i += 1
            k += 1

    while i <= m:
        b[k] = v[i]
        i += 1
        k += 1
    while j<=u:
        b[k] = v[j]
        j += 1
        k+=1
    v[p:u+1]=b #for i in range(len(b)): v[i+p]=b[i]

def sort_inter(v,p,u): #supb- data prin indicii p si u, nu v[p:u+1]
    if p>=u:  #rezolvam direct
        return
    else:
        m=(p+u)//2
        sort_inter(v,p,m)
        sort_inter(v,m+1,u)
        interclasare(v,p,m,u)
def sortare_interclasare(v):
    sort_inter(v,0,len(v)-1)
v=[5,1,6,3,1,9,11,-4]
sortare_interclasare(v)
print(v)

###################################
# C11 Traseu / Suma (ne)recursiva #
###################################

a=[[2],[4,5],[10,7,3],[1,5,2,1],[8,4,5,6,7,11]]
a=[[2],[4,5],[10,7,3],[1,5,2,1]]

def suma(i,j):
    global nr #numarul de apeluri recursive<=2*nr de elemente
    nr=nr+1
    if s[i][j] is not None: #daca este deja rezolvata-returnam valoarea, nu mai apelam recursiv
        return s[i][j]
    if i==n-1:
        s[i][j]=a[i][j]
        return a[i][j]
    s[i][j]=a[i][j]+max(suma(i+1,j), suma(i+1,j+1))
    return s[i][j]
    #return a[i][j]+max(suma(i+1,j), suma(i+1,j+1))-: exponential

def suma_nerec():
    s = [[None for j in range(i + 1)] for i in range(n)]
    #s[n-1][:]=a[n-1]
    for j in range(n):
        s[n-1][j]=a[n-1][j]
    for i in range(n-2, -1,-1):
        for j in range(i+1):
            s[i][j]=a[i][j]+max(s[i+1][j],s[i+1][j+1])
    print(s[0][0])
    print(s)

nr=0
n=len(a)
s=[[None for j in range(i+1)] for i in range(n)]
print(suma(0,0))
print(s)
print(nr,"apeluri")
suma_nerec()

def traseu(i,j):
    if i==n-1:
        print(i,j)
    else:
        print(i,j)
        if s[i][j]==a[i][j]+s[i+1][j]: #if s[i+1][j]>s[i+1][j+1]
            traseu(i+1,j)
        else:
            traseu(i+1,j+1)


traseu(0,0)

#Observatii:
#1. Putem afisa traseul si nerecursiv
#2. Putem folosi tot matricea a pentru a caclula suma, in loc de s

##############
# C12 Monede #
##############

S=12
S=19
v=[1,6,7]
inf=S+1
nr=[inf]*(S+1) #daca nu se poate descompune -> inf =S+1
nr[0]=0
desc=[inf]*(S+1)
for s in range(1,S+1):
    if s in v:
        nr[s]=1
        desc[s]=s
    else:
        nrmin=inf
        for moneda in v:
            if moneda<=s and nr[s-moneda]<nrmin:
                nrmin=nr[s-moneda]
                desc[s]=moneda
        if nrmin<inf:
            nr[s]=1+nrmin
print(nr)
print(desc)
if nr[S]==inf:
    print("nu se poate plati suma")
else:
    s=S
    while s!=0:
        print(desc[s],end=" ")
        s=s-desc[s]

def descompune(s):

    if nr[s] is not None:
        return nr[s]
    if s==0:
        nr[0]=0
        return 0
    nrmin = inf
    for moneda in v:
        if moneda <= s and  descompune(s - moneda)< nrmin: #ar fi mers memorat descompune(s - moneda) in variabia
            nrmin = descompune(s - moneda)
    if nrmin<inf:
        nr[s]=1+nrmin
    else:
        nr[s]=inf
    return nr[s]

S=19
nr=[None]*(S+1)
print()
print(descompune(S))

####################################
# C13 Programare dinamica - Rucsac #
####################################

f=open("rucsac.in")
g=[int(x) for x in f.readline().split()]
c=[int(x) for x in f.readline().split()]
G=int(f.readline())
f.close()
n=len(g)
g.insert(0,0) #obiectul 1 va fi pe pozitia 1
c.insert(0,0)
s=[[0 for i in range(G+1)] for j in range(n+1)]
#prima linie si prima coloana raman 0 (corespun 0 obiecte/greutate 0
for i in range(1,n+1):
    for gr in range(1, G+1):
        if g[i]>gr:
            s[i][gr]=s[i-1][gr] #nu putem lua obiectul i, are greutate prea amre
        else:
            s[i][gr] =max(s[i-1][gr], s[i-1][gr-g[i]]+c[i])
print(*s,sep="\n")
print(s[n][G])

#determinarea solutiei - de la coltul de jos inapoi
print("obiectele")
i=n
gr=G
while i>0 and gr >0:
    if s[i][gr]!=s[i-1][gr]: #luam obiectul i
        print(i)
        gr-=g[i]
        i-=1
    else:
        i-=1

############################
# C13 Subsir crescator max #
############################

#v=[5,3,7,8,6,10]
v=[8,3,1,4,6,5,11]
n=len(v)
lung=[1]*n
succ=[-1]*n #[None]*n

lung[n-1]=1 #stim direct
#ord de calcul - de la ultimul catre primul
for i in range(n-2,-1,-1):
    lmax=0
    for j in range(i+1,n):
        if v[i]<v[j] and lung[j]>lmax:
            lmax=lung[j]
            succ[i]=j
    lung[i]=1+lmax

print(*lung)
print(*succ)

pmax=0
for i in range(n):
    if lung[i]>lung[pmax]:
        pmax=i
print("lungimea maxima ",lung[pmax])

p=pmax
for i in range(lung[pmax]):
    print(v[p],end=" ")
    p=succ[p]

#numaram cate subisruri optime exista
print(lung)

nr=[0]*n
nr[n-1]=1
for i in range(n-2,-1,-1):
    for j in range(i+1,n):
        if v[i]<v[j] and lung[j]==lung[i]-1:
            nr[i]+=nr[j]
    if nr[i]==0:
        nr[i]=1
print(nr)
nr_optim=0
for i in range(n):
    if lung[i]==lung[pmax]:
        nr_optim+=nr[i]
print(nr_optim)

#######################
# C13 Aranjamente BKT #
#######################

"""
Aranjamente de m din multimea {1,2,..,n}
1 2 3
2 3 1
3 2 1
1. Reprez solutiei
x=x_0,.., x_{m-1}
2) Fiecare element x_k poate lua valorile
x_k - 1,2..., n
3) Conditiile finale
elementele sa fie distincte x_i!=x_j
4) Conditiile de continuare la pasul k (!!) - cand ii dam valoare lui x_k
x_k!=x_0,...,x_{k-1}
"""
def continuare(k,x):
    for i in range(k): #x[k]in x[:k] x.index(x[k],0,k)...
        if x[i]==x[k]:
            return False
    return True

def back(k,x,n,m):
    if k == m: #daca am completat toate pozitiile si incerc sa completez x_m -> avem solutie
        #testam conditiile finale - doar in cazul in care cond de continuare nu au fost suficiente
        print(*x)
        #daca x retine indici din A(!!!de la 1 la n)
        for i in range(m):
            print(A[x[i]-1],end=" ")
        print()
    else:
        #luam la rand valorile posibile pentru x_k
        for i in range(1,n+1): #for i in A, daca x contine direct elemente din A
            x[k]=i
            if continuare(k,x):
                back(k+1,x,n,m)
def aranjamente(m,n):
    x=[0]*m
    back(0,x,n,m)
A=["s1","s2","s3","s4"]
aranjamente(3,4)

#####################
# C13 Combinari BKT #
#####################

"""
Combinari  de m din multimea {1,2,..,n}
1 2 3 = 2 3 1 = 3 2 1 -> o generam doar pe cea ord crescator
1. Reprez solutiei
x=x_0,.., x_{m-1}
2) Fiecare element x_k poate lua valorile
x_k - 1,2..., n
3) Conditiile finale
elementele sa fie distincte x_i!=x_j +Crescator
4) Conditiile de continuare la pasul k (!!) - cand ii dam valoare lui x_k
x_k>x[k-1] (Deci x_k este diferit de x_0,..,x_{k-1}
"""
def continuare(k,x):
     return k==0 or x[k]>x[k-1]

def back(k,x,n,m):
    if k == m: #daca am completat toate pozitiile si incerc sa completez x_m -> avem solutie
        #testam conditiile finale - doar in cazul in care cond de continuare nu au fost suficiente
        print(*x)


    else:
        #luam la rand valorile posibile pentru x_k
        for i in range(1 if k==0 else x[k-1]+1,n+1):
        #for i in range(1,n+1):
            x[k]=i
            #if continuare(k,x):
            back(k+1,x,n,m)
def combinari(m,n):
    x=[0]*m
    back(0,x,n,m)

combinari(3,4)

#####################
# C13 Paranteze BKT #
#####################

def catalan(n):
    cat=[0]*(n+1)
    cat[0]=cat[1]=1
    cat[2]=2
    for j in range(3,n+1):
        for i in range(0,j):
            cat[j]+=cat[i]*cat[j-1-i]
    return cat[n]

def back(k,dif):
    global nr
    if k==2*n:
        print("".join(x))
        nr+=1
    else:
        #luam la rand valorile pentru x[k]:
        x[k]='('
        dif=dif+1
        if dif<=2*n-k:
            back(k+1,dif)
        dif-=1
        x[k]=')'
        dif-=1
        if dif>=0:
            back(k + 1, dif)
        dif+=1
n=4
x=[None for i in range(2*n)]
nr=0
back(0,0)
print(nr)
print(catalan(n))

#################
# C13 Permutari #
#################

"""
Permutarile multimii {1,2,..,n}
1. Reprez solutiei
x=x_0,.., x_{n-1}
2) Fiecare element x_k poate lua valorile
x_k - 1,2..., n
3) Conditiile finale
elementele sa fie distincte x_i!=x_j
4) Conditiile de continuare la pasul k (!!) - cand ii dam valoare lui x_k
x_k!=x_0,...,x_{k-1}
"""
def continuare(k,x):
    for i in range(k): #x[k]in x[:k] x.index(x[k],0,k)...
        if x[i]==x[k]:
            return False
    return True

def back(k,x,n):
    if k == n: #daca am completat toate pozitiile si incerc sa completez x_n -> avem solutie
        #testam conditiile finale - doar in cazul in care cond de continuare nu au fost suficiente
        print(*x)
    else:
        #luam la rand valorile posibile pentru x_k
        for i in range(1,n+1):
            x[k]=i
            if continuare(k,x):
                back(k+1,x,n)
def permutari(n):
    x=[0]*n
    back(0,x,n)
permutari(3)

def permutari_nerecursiv(n):
    x=[0]*n
    k=0
    while k>=0: #cand k devine -1 => stop
        if k==n:
            print(*x,sep=",")
            k-=1
        else: #dam lui x[k] urmatarea valoare posibila, daca mai sunt valori
            if x[k]<n:
                x[k]=x[k]+1
                if continuare(k,x):
                    k+=1
            else:
                x[k]=0
                k-=1
permutari_nerecursiv(3)

#########################
# C13 Pal min partition #
#########################

class Solution:
    def minCut(self, s: str) -> int:
        n=len(s)
        palindrom=[[True for i in range(n)] for j in range(n)]
  
        for dif in range(1,n)  :  
            for i in range(n-dif):
                j=i+dif
                #print(s[i:j+1],i,j,i+1,j-1,palindrom[i+1][j-1],s[i],s[j],s[i]==s[j] and palindrom[i+1][j-1])
                if s[i]==s[j] and palindrom[i+1][j-1]:
                    palindrom[i][j]=True
                else:
                    palindrom[i][j]=False
                #print(palindrom[i][j])
        
       #print(palindrom)
        dp=[float("inf") for i in range(n)]
        dp[0]=1
        for i in range(1,n):
            if palindrom[0][i]:
                dp[i]=1
            else:
                for j in range(1,i+1):
                    
                    if palindrom[j][i]:
                        dp[i]=min(dp[i],dp[j-1]+1)
        #print(dp)     
        return dp[n-1] -1

####################
# C13 Partitiile n #
####################

"""
n=5
1+1+1+1+1
1+1+1+2
..
2+3 (= 3+2)
5
x=(x1,...,xp) (lungime variabila
cond continuare suma<=n
valori pt xk: 1...n  -+ crescator nestrict (pentru unicitate)

"""
def back(k,s,x,n):
    if s==n:
        print(*x[:k],sep="+")
    else:
        for i in range(1 if k==0 else x[k-1],n+1):
            x[k]=i
            s+=i
            if s<=n:
                back(k+1,s,x,n)
            s-=i
def partitie(n):
    x=[0]*n
    back(0,0,x,n)
partitie(6)

##################################################
# C13 Subsir crescator max cu generare subsiruri #
##################################################

#v=[5,3,7,8,6,10]
v=[8,3,1,4,6,5,11]
n=len(v)
lung=[1]*n
succ=[-1]*n #[None]*n



lung[n-1]=1 #stim direct
#ord de calcul - de la ultimul catre primul
for i in range(n-2,-1,-1):
    lmax=0
    for j in range(i+1,n):
        if v[i]<v[j] and lung[j]>lmax:
            lmax=lung[j]
            succ[i]=j
    lung[i]=1+lmax

print(*lung)
print(*succ)

pmax=0
for i in range(n):
    if lung[i]>lung[pmax]:
        pmax=i
print("lungimea maxima ",lung[pmax])

p=pmax
for i in range(lung[pmax]):
    print(v[p],end=" ")
    p=succ[p]

#numaram cate subisruri optime exista
print(lung)

nr=[0]*n
nr[n-1]=1
for i in range(n-2,-1,-1):
    for j in range(i+1,n):
        if v[i]<v[j] and lung[j]==lung[i]-1:
            nr[i]+=nr[j]
    if nr[i]==0:
        nr[i]=1
print(nr)
nr_optim=0
for i in range(n):
    if lung[i]==lung[pmax]:
        nr_optim+=nr[i]
print(nr_optim)

"""
Toate subsirurile crescatoare de lungime maxima
1) repr sol:
x=(x0,..., x_{lung-1}) - indicii elementelor din subsir
2)
x0 - tb lung[x0]=lmax
x1: x0<x1 (dupa x0), v[x0]<v[x1] (subsir crescator) si lung[x1]=lung[x0]-1
analog pt xk
"""
lmax=lung[pmax]
def back(k):
    if k==lmax:
        for i in x:
            print(v[i],end=" ")
        print()
    else:
        for j in range(x[k-1]+1,n): #toate pozitiile de dupa x[k-1]
            x[k]=j
            if v[x[k-1]]<v[x[k]] and lung[x[k]]==lung[x[k-1]]-1:
                back(k+1)
#pentru primul element - dam valori separat
x=[0]*lmax
for i in range(len(v)):
    if lung[i]==lmax:
        x[0]=i
        back(1)

# Delete last check on 10th of January 2025
