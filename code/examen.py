''' 
Model 2024-2025 Subiectul 1 a) (1.5 p.)
Scrieți o funcție divizori care primește un număr variabil de parametri numere
naturale și returnează pentru fiecare număr primit ca parametru lista divizorilor săi
primi sub forma unui dicționar cu perechi de forma număr: lista divizorilor. De exemplu,
pentru apelul divizori(50, 21) funcția trebuie să furnizeze dicționarul {50: [2,5], 21: [3,7]}.
'''

def este_prim(numar):
    """
    Verifică dacă un număr este prim.
    """
    if numar < 2:
        return False
    for i in range(2, int(numar**0.5) + 1):
        if numar % i == 0:
            return False
    return True

def divizori(*numere):
    """
    Returnează un dicționar cu numerele date și lista divizorilor lor primi.
    """
    rezultat = {}
    for numar in numere:
        divizori_primi = []
        for i in range(2, numar + 1):
            if numar % i == 0 and este_prim(i):
                divizori_primi.append(i)
        rezultat[numar] = divizori_primi
    return rezultat

dict_divizori = divizori(50, 21)
# print(dict_divizori)

''' 
Model 2024-2025 Subiectul 1 b) (0.5 p.) 
Înlocuiți punctele de suspensie din instrucțiunea litere_10 = […] cu o expresie astfel
încât lista să fie inițializată cu primele 10 litere mici din alfabetul englez.
'''

litere10 = [chr(i) for i in range (ord('a'), ord('a') + 10)]
# print(litere10)

''' 
Model 2024-2025 Subiectul 1 c) (1 p.)
Considerăm o funcție recursivă a cărei complexitate este dată de următoarea relație de
recurență:
T(1) = T(2) = 1
T(n) = T(n/3) + 2, pentru n ≥ 1
Determinați complexitatea funcției respective. 
'''

# O(log3(n))

'''
Model 2024-2025 Subiectul 2 - Metoda Greedy (3 p.)
Complexitatea maximă a soluției: O(nlog2 n )
Considerăm n spectacole S1, S2, ..., Sn pentru care cunoaștem intervalele lor de desfășurare
[s1, f1), ..., [sn, fn), toate dintr-o singură zi. Având la dispoziție o singură sală, în care putem
să planificăm un singur spectacol la un moment dat, să se determine numărul maxim de
spectacole care pot fi planificate fără suprapuneri. Un spectacol Sj poate fi programat
după spectacolul Si dacă sj ≥ fi. Justificați corectitudinea programului și complexitatea sa.
'''

''' 
Model 2024-2025 Subiectul 3 - Metoda Programării Dinamice (3 p.)
Complexitatea maximă a soluției: O(n2)
Să se determine un subșir crescător de lungime maximă al unui șir t format din n numere
întregi.
'''

''' 
Model 2024-2025 Subiectul 4 - Metoda Backtracking (3 p.)
Să se afișeze toate permutările mulțimii A = {1,2, ..., n}, unde n este un număr natural nenul
'''

'''
2021-2022 Restanta & Marire Subiectul 2
În vitrina magazinului CheapLuxury bijuteriile din aur sunt așezate pe 𝑚 ≥ 3 rânduri, iar
pe fiecare rând sunt câte n ≥ 3 bijuterii. Hoțul Gicuță vrea să spargă vitrina magazinului
și să fure bijuteriile, dar, deoarece sistemul de alarmă al magazinului este foarte
performant, el își dă seama că are nevoie de un plan bine pus la punct. În acest scop, Gicuță
se gândește să fure de pe fiecare din cele 𝑚 rânduri câte o singură bijuterie astfel încât
valoarea totală a acestora să fie maximă și, fiind lacom, vrea ca valoarea fiecărei bijuterii
să fie strict mai mare decât valoarea bijuteriei furate de pe rândul precedent.
Scrieți un program Python care citește de la tastatură două numere naturale nenule m și
n, o matrice cu m linii și n coloane care conține pe linia i valorile bijuteriilor de pe rândul
i exprimate în euro, după care afișează pe ecran, în forma indicată în exemplu, valoarea
totală a bijuteriilor pe care trebuie să le fure Gicuță, precum și pozițiile acestora
(rândurile sunt considerate ca fiind numerotate de la 1, la fel și pozițiile bijuteriilor în
cadrul unui rând). Dacă nu există nicio modalitate de a fura bijuteriile conform
restricțiilor indicate, atunci programul va afișa mesajul “Imposibil”.
Exemplu:
Date de intrare 
4 3
515.99 350.79 731.25
299.99 515.88 766.10
566.25 271.99 444.89
865.99 918.55 799.99
Date de ieșire
2351.47
1 2
2 2
3 1
4 2
'''

### MySolution
# m, n = int(input().split())
# for i in range(1, m + 1):
#     for j in range (1, n + 1):
#         a[i][j] = int(input())
# pos = tuple()
# minim1 = a[1][1]
# for i in range(2, n + 1):
#     if a[1][i] < minim1:
#         minim1 = a[1][i]
#         savei, savej = 1, i
#         pos.append(savei)
#         pos.append(savej)
# sum = minim1
# for i in range(2, m):
#     minim2 = a[i][1]
#     for j in range(2, n + 1):
#         if a[i][j] < minim2 and a[i][j] > minim1:
#             minim2 = a[i][j]
#             savei, savej = i, j
#             pos.append(savei)
#             pos.append(savej)
#     sum += minim2
#     minim1 = minim2
# maxim = a[m][1]
# for i in range(2, n + 1):
#     if a[m][i] > maxim:
#         maxim = a[m][i]
#         savei, savej = m, i
#         pos.append(savei)
#         pos.append(savej)
# print(sum)
# limit = len(pos)
# for i in range(0, limit, 2):
#     print(f"{pos[i]} {pos[i + 1]}")

### GPT Solution
# m, n = map(int, input().split())
# # Inițializare corectă a matricei
# a = [list(map(int, input().split())) for _ in range(m)]
# # Listă pentru stocarea pozițiilor
# pos = []
# # Alegem cel mai mic element din prima linie
# minim1 = min(a[0])
# savei, savej = 0, a[0].index(minim1)
# pos.append((savei + 1, savej + 1))  # Salvăm pozițiile 1-based
# suma = minim1
# # Căutăm cele mai mici valori din fiecare linie
# for i in range(1, m - 1):
#     minim2 = float('inf')
#     for j in range(n):
#         if minim1 < a[i][j] < minim2:
#             minim2 = a[i][j]
#             savei, savej = i, j
#     if minim2 != float('inf'):
#         suma += minim2
#         pos.append((savei + 1, savej + 1))
#         minim1 = minim2
# # Găsim valoarea maximă din ultima linie
# maxim = max(a[m - 1])
# savei, savej = m - 1, a[m - 1].index(maxim)
# pos.append((savei + 1, savej + 1))
# # Afișare rezultate
# print(suma)
# for i, j in pos:
#     print(i, j)

'''
2021-2022 Subiect 01 Subiectul 1 a)
Scrieți o funcție palindrom care primește un număr variabil de cuvinte formate doar din litere mici ale alfabetului englez și returnează informații despre cuvintele palindrom sub forma unui dicționar de perechi {cuvant palindrom: lista de litere}. Cheia este cuvântul primit ca parametru dacă acesta este palindrom, iar lista de litere este formată din vocalele cuvântului dacă numărul vocalelor este mai mare decât numărul consoanelor, altfel lista va fi formată din consoanele cuvântului. Listele de litere vor fi sortate în ordine lexicografică. De exemplu, pentru apelul palindrom ('asa', 'merem', 'palindrom') funcția va returna dicționarul {'asa': ['a'], 'merem': ['m', 'r']}
'''

def palindrom(*cuvinte):
    d = dict()
    for cuvant in cuvinte:
        lista_cuvant = []
        for litera in cuvant:
            lista_cuvant.append(litera)
        lista_cuvant.reverse()
        inversul = "".join(lista_cuvant)
        if cuvant == inversul:
            vocale = []
            consoane = []
            cnt_vocale, cnt_consoane = 0, 0
            for litera in cuvant:
                if litera.lower() in ['a', 'e', 'i', 'o', 'u']:
                    if litera in vocale:
                        cnt_vocale += 1
                    else:
                        cnt_vocale += 1
                        vocale.append(litera)
                else:
                    if litera in consoane:
                        cnt_consoane += 1
                    else:
                        cnt_consoane += 1
                        consoane.append(litera)
            vocale.sort()
            consoane.sort()
            if cnt_vocale >= cnt_consoane:
                d[cuvant] = vocale
            else:
                d[cuvant] = consoane
    return d
# print(palindrom('asa', 'merem', 'palindrom'))

'''
2021-2022 Subiect 01 Subiectul 1 b)
Știind că matricea pătratică m este memorată sub forma unei liste de liste, înlocuiți punctele de suspensie din instrucțiunea numere = […] cu o secvență de inițializare (list comprehension) astfel încât, după executarea sa, lista să conțină pătratul elementelor aflate pe diagonala principală a matricei m. De exemplu, pentru matricea m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] trebuie ca lista numere să fie [1, 25, 81].
'''

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# numere = [v[i][i] ** 2 for i in range(m)] # Asa am scris pe foaie crezand ca avem o variabila m pentru ordinul matricei patratice. In plus, matricea este m, nu v.
numere = [m[i][i] ** 2 for i in range(len(m))]
# print(numere)

'''
2021-2022 Subiect 01 Subiectul 1 c)
Considerăm următoarea funcție recursivă:
```
def f(lista):
    if len(lista) <= 2:
        return sum(lista)
    k = len(lista) // 3
    aux_1 = lista[:k]
    aux_2 = lista[k: 2*k]
    aux_3 = lista[2*k:]
    return f(aux_1) + f(aux_2) + f(aux_3)
```
Determinați complexitatea funcției apelată pentru o listă L formată din n numere întregi astfel: f(L).
'''

# Daca lista are mai putin de doua elemente, avem o complexitate constanta, deoarece facem suma a doua sau chiar a unui singur element. Deci cazul de baza are complexitatea O(1).
# Altfel, facem 3 apeluri pentru fiecare treime a listei.
# T(n) = 3T(n/3) + O(1) => a = 3, b = 3, d = 0
# Teorema Master: T(n) = a*T(n/b) + O(n^d)
# d < log_b(a) => T(n) = O(n^(log_b(a)))
# d = log_b(a) => T(n) = O(n^d * log(n))
# d > log_b(a) => T(n) = O(n^d)
# d = 0
# log_b(a) = log_3(3) = 1
# 0 < 1 <=> d < log_b(a)
# Asadar, T(n) = O(n^log_3(3)) = O(n)

'''
2021-2022 Subiect 01 Subiectul 2
O balanță veche s-a defectat și acum se echilibrează nu doar pentru două obiecte având aceeași greutate, ci pentru orice două obiecte cu proprietatea că modulul diferenței dintre greutățile lor este mai mic sau egal decât un număr real g. Scrieți un program Python care citește de la tastatură un număr natural n, un număr real g și greutățile a n obiecte, după care afișează pe ecran numărul maxim de perechi de obiecte care echilibrează balanța defectă, precum și perechile respective, știind că orice obiect poate să facă parte din cel mult o pereche. Fiecare pereche afișată trebuie să fie de forma x + y, unde x și y sunt numerele de ordine ale celor două obiecte din pereche (obiectele sunt numerotate începând de la 1). Greutățile tuturor obiectelor și diferența g sunt exprimate prin numere reale strict pozitive, reprezentând grame. Nu contează ordinea în care se vor afișa perechile de obiecte pe ecran și nici ordinea numerelor de ordine ale obiectelor dintr-o pereche.
Exemplu:
Date de intrare
10
8.5
21.25
12
6.05
20.7
23.8
22
33.25
21
48.15
62.20
Date de ieșire
3
3 + 2
10 + 4
1 + 8
Explicații: Avem n = 10 și g = 8.5. Se pot forma maxim 3 perechi de obiecte care pot
echilibra balanța defectă. Soluția nu este unică, o altă soluție corectă obținându-se, de
exemplu, înlocuind perechea 1 + 6 cu perechea 1 + 5.
'''

def grame():
    n = int(input())
    g = float(input()) # float nu int
    numere = []
    for i in range(n):
        numar = float(input())
        numere.append((numar, i))
    print(numere[0][0]) # 21.25
    print(numere[0][1]) # 0
    print(numere[1][0]) # 12.0
    print(numere[1][1]) # 1
    numere.sort()
    maxim_perechi, i = 0, 0
    perechi = list() # Atentie! Initial am pus tuple, insa 'tuple object has no attribute append'
    while i < n - 1: # Atentie! Mergem pana la penultimul, nu pana la ultimul
        if numere[i + 1][0] - numere[i][0] <= g:
            perechi.append(numere[i][1] + 1) # Deoarece indexarea incepe de la 1, nu de la 0
            perechi.append(numere[i + 1][1] + 1) # Atentie! Nu putem da append la doua valori deodata, trebuie pe rand
            i += 2
            maxim_perechi += 1
        else:
            i += 1
    print("Date de iesire")
    print(maxim_perechi)
    for i in range(0, len(perechi), 2):
        print(f"{perechi[i]} + {perechi[i + 1]}")
# grame()  

'''
2021-2022 Subiect 01 Subiectul 3
Schiorel a urcat cu telecabina până în vârful stațiunii și își dorește să ajungă cât mai obosit la una din cabanele stațiunii ca să se poată hidrata cât mai intens. Stațiunea e reprezentată ca o matrice pătratică de dimensiune n în care în fiecare pătrat avem gradul de oboseală pe care îl va acumula Schiorel dacă trece prin acel câmp sau -1, însemnând că în acel câmp avem o cabană. Schiorel poate începe traseul de oriunde de pe linia de sus și se poate opri la orice cabană, voi trebuie să-l ajutați să ajungă cât mai obosit! Schiorel poate coborî drept sau în diagonală, adică din (i,j) în {(i+1,j-1), (i+1, j), (i+1, j+1)} evident fără a părăsi stațiunea.
Scrieți un program Python care citește de la tastatură dimensiunea tablei n și pentru
fiecare pătrățică de coordonate (i,j) (cu i=1,..,n, j=1,...,n) o valoare cij cu semnificația:
• dacă cij este număr natural, el reprezintă gradul de oboseală acumulat de Schiorel când trece prin acea zona a stațiunii.
• dacă cij este -1, atunci în acea zonă se află o cabană!
și afișează un traseu al lui Schiorel până la o cabană, astfel încât să ajungă cât mai obosit (odată ajuns la o cabană, Schiorel se oprește și nu mai continuă drumul).
Intrare de la tastatură
4
5 2 6 11
-1 7 1 -1
4 10 3 5
1 6 -1 2
Ieșire pe ecran
Gradul de oboseala maxim 23
1 3
2 2
3 2
4 3
Explicații: Părtia este o matrice de dimensiuni 4x4 în care elementele reprezintă oboseala
acumulată trecând prin acel punct, respectiv -1 în locul în care avem cabană. Pe traseul
(1,3), (2,2), (3,2), (4,3) acumulează oboseala 23 (!traseul trebuie să înceapă pe prima linie
și să se termine cu o pătrățică de valoare -1). 
Intrare de la tastatură
4
5 2 6 31
-1 7 -1 -1
4 10 3 5
1 6 -1 2
Ieșire pe ecran
Gradul de oboseala maxim 31
1 4
2 3
Odată ajuns la o cabana, Schiorel se oprește din schiat.
P.S. Lui Schiorel îi place oboseala.
'''

'''
2021-2022 Subiect 01 Subiectul 4 a)
Petrișor ar vrea să își schimbe parolele și are o mulțime de litere preferate L și o mulțime S de simboluri (caractere care nu sunt litere) pe care ar vrea să le folosească în parole pentru a crește siguranța acestora . Pentru a îi fi mai ușor să le țină evidența, el ar vrea să își construiască parole de aceeași lungime după un anumit tipar. Tiparul este un șir de caractere de lungime n format doar cu caracterele 'l' și 's' cu semnificația: dacă în tipar pe poziția i este caracterul 'l', atunci în parolă pe poziția i va fi o literă din mulțimea L, iar dacă în tipar pe poziția i este caracterul 's', atunci în parolă pe poziția i va fi un simbol din mulțimea S. Mai mult, Petrișor și-ar dori ca orice simbol din S și orice literă din L să apară cel mult o dată în parolă. Scrieți un program Python care să citească de la tastatură numărul n, tiparul T și mulțimile L și S, după afișează toate parolele care verifică cerințele lui Petrișor sau mesajul "Imposibil" dacă nu există nicio parolă având proprietățile cerute.
Exemplu: Pentru n = 6, tiparul 'lslsll', mulțimea L de litere 'a', 'b', 'c', 'D' și mulțimea S de simboluri '@','.' trebuie afișate următoarele 48 de parole (nu neapărat în această ordine):
a@b.cD
a@b.Dc
a@c.bD
a@c.Db
a@D.bc
a@D.cb
a.b@cD
a.b@Dc
a.c@bD
a.c@Db
a.D@bc
a.D@cb
b@a.cD
b@a.Dc
b@c.aD
b@c.Da
b@D.ac
b@D.ca
b.a@cD
b.a@Dc
b.c@aD
b.c@Da
b.D@ac
b.D@ca
c@a.bD
c@a.Db
c@b.aD
c@b.Da
c@D.ab
c@D.ba
c.a@bD
c.a@Db
c.b@aD
c.b@Da
c.D@ab
c.D@ba
D@a.bc
D@a.cb
D@b.ac
D@b.ca
D@c.ab
D@c.ba
D.a@bc
D.a@cb
D.b@ac
D.b@ca
D.c@ab
D.c@ba
'''

'''
2021-2022 Subiect 01 Subiectul 4 b)
Modificați o singură instrucțiune din program astfel încât să fie afișate doar parolele care încep cu o vocală. Pentru exemplul anterior, aceste soluții sunt cele scrise cu roșu. 
'''

'''
O tema de prin cursuri (pe la inceput in drive-ul lui Fabian)
x = 272 # 256 + 16

print(bin(x)) # 0b100010000

print(bin(x & 0b10001), x & 0b10001) # 0b000010000 16
# 0b100010000 &
# 0b000010001 =
# 0b000010000 = 16

print(bin(17 | 0b10001), 17 | 0b10001) # 0b10001 17
# 17 = 16 + 1 = 0b10001
# 0b10001 |
# 0b10001 =
# 0b10001 = 17

print(bin(~x), ~x) # 0b011101111 239; De ce in terminal primesc -0b100010001 -273
# x =   272
# x =   0b100010000
# ~x =  0b011101111
# ~x =  1 + 2 + 4 + 8 + 32 + 64 + 128 = 131 + 108 = 239 
# NU este chiar asa! ~x = -(x + 1) = - (272 + 1) = -273
# 0b011101111 -> 0b100010000 + 0b1 = 0b100010001 

print(bin(x >> 1), x >> 1) # 0b010001000 136
# x =       0b100010000
# x >> 1 =  0b010001000 = 8 + 128 = 136
# x >> 1 i.e. x // 2
'''

'''
2021-2022 Subiect 02 Subiectul 1 a)
Scrieți o funcție aparitii care primește un număr variabil de numere naturale și returnează un dicționar care conține pentru fiecare număr primit ca parametru o listă de perechi în care pentru fiecare cifră distinctă a numărului avem perechea formată din valoarea cifrei și frecvența sa în acel număr. De exemplu, pentru apelul aparitii(1011, 234, 8158558) funcția trebuie să returneze dicționarul {1011: [(1,3), (0,1)], 234: [(2,1), (3,1), (4,1)], 8158558: [(1,1), (5,3), (8,3)]}
'''

def aparitii(*numere):
    d = dict()
    for numar in numere:
        lista_aparitii = []
        aparitii = [0] * 10
        for cifra in str(numar):
            aparitii[int(cifra)] += 1
        for i in range(10):
            if aparitii[i]:
                lista_aparitii.append((i, aparitii[i]))
        d[numar] = lista_aparitii
    return d
# print(aparitii(1011, 234, 8158558))

'''
2021-2022 Subiect 02 Subiectul 1 b)
Considerând un dicționar cu același format ca dicționarul de la punctul a), scrieți o secvență de inițializare pentru o listă (list comprehension) care să conțină cheile din dicționar care au cel puțin 3 cifre distincte. De exemplu, pentru dicționarul anterior, se va obține lista [234, 8158558].
'''

dictionar_aparitii = aparitii(1011, 234, 8158558)
# print([x for x in dictionar_aparitii.keys() if len(dictionar_aparitii[x]) >= 3])

'''
2021-2022 Subiect 02 Subiectul 1 c)
Considerăm următoarea funcție recursivă:
```
def f(lista, p, u):
    if u - p <= 2:
        return sum(lista[p: u+1])
    k = (u - p + 1) // 3
    aux_1 = sum(lista[p: p + k])
    aux_2 = f(lista, p + k + 1, p + 2 * k - 1)
    aux_3 = sum(lista[p+2*k+1: u+1])
    return sum([aux_1, aux_2, aux_3])
```
Determinați complexitatea funcției apelată pentru o listă L formată din n numere întregi astfel: f(L, 0, n-1).
'''

# Daca u - p <= 2 atunci functia returneaza suma unei liste de u - p elemente, ceea ce inseamna ca functia are complexitate constanta, O(1)
# Altfel:
# Pentru, aux_1 si aux_3 avem O(k) intrucat facem suma sublistei de la p la p + k - 1 pentru aux_1, analog si pentru aux 3
# Pentru aux_2 avem T(n/3)
# T(n) = T(n/3) + O(n) => a = 1, b = 3, d = 1
# log_b(a) = log_3(1) = 0 < 1 i.e. d > log_b(a)
# T(n) = O(n^d) = O(n^1) = O(n), complexitate liniara.
# N.B. Cand avem apelul functiei, avem T(ceva), altfel daca sunt operatii sau functii simple avem O(complexitatea operatiilor sau functiilor). De exemplu, pentru aux_1 si aux_3 avem O(n) si pentru aux_2 avem T(n/3)

'''
2021-2022 Subiect 02 Subiectul 2
Se organizează un concurs de tip trivia în limbajul Python la care participă nea Vasile împreună cu alți N oameni. Fiecărui om din cei N i se asociază o valoare strict pozitivă X_i, mai puțin lui Vasile căruia i se asociază implicit valoarea 0 (practic, Vasile este complet subestimat atât de către organizatori, cât și de ceilalți participanți). Concursul se desfășoară în mai multe runde eliminatorii, până când rămâne un singur om care este declarat câștigătorul. Într-o rundă la care participă K oameni (inclusiv Vasile!) sunt eliminați toți cei care nu știu răspunsul corect la întrebarea respectivă, iar scorul rundei se calculează ca fiind ∑(x_i/k) pentru toți indicii i ai oamenilor eliminați în runda respectivă. Câștigătorul concursului va primi o sumă de bani egală cu suma scorurilor tuturor rundelor. Nea Vasile știe tot ceea ce s-ar putea ști despre limbajul Python (adică este imposibil ca el să piardă concursul!), deci îl interesează doar să afle suma maximă de bani pe care ar putea să o câștige.
Scrieți un program Python care să citească de la tastatură numărul natural nenul N, reprezentând numărul de concurenți (în afară de nea Vasile) și cele N numere strict pozitive asociate celor N participanți (separate între ele prin câte un spațiu), după care afișează un singur număr real (cu 3 zecimale) reprezentând suma maximă de bani pe care ar putea să o câștige nea Vasile. 
Exemplu:
Date de intrare
2
6 6
Date de ieșire
5
Explicații: Suma maximă de bani pe care o poate câștiga Vasile este 5 = 2 + 3. În prima rundă ar trebui să iasă un singur adversar de-ai lui nea Vasile, scorul rundei fiind 6 / 3 = 2. În a doua rundă va ieși și ultimul adversar, scorul rundei fiind 6 / 2 = 3.
'''

def nea_Vasile():
    N = int(input())
    X = list(map(int, input().split()))
    print(X)
    k = N + 1
    # Stiind ca numitorul scade de la N + 1, ar trebui ca numaratorul sa creasca. Deci, pentru a obtine o suma maxima, sortam lista crescator
    X.sort()
    suma = 0
    for i in range(N):
        suma += X[i] / k
        k -= 1
    print(f"{suma:.3f}")
# nea_Vasile()

'''
2021-2022 Subiect 02 Subiectul 3
Alice ar vrea să își schimbe parola la contul de email și are un șir de caractere preferat (format din caractere ASCII) de lungime n și un număr preferat k. Ea se gândește la următorul algoritm de construcție a unei parole din șirul ei de caractere preferat: șterge caractere din șir astfel încât șirul obținut după ștergere verifică următoarea proprietate - pentru orice două caractere aflate pe poziții consecutive în șir diferența dintre codurile lor ASCII (în modul) este mai mare sau egală cu k. Alice ar vrea ca parola să fie cel mai lung șir care se poate obține astfel din șirul ei preferat și numărul ei preferat k și vă roagă pe voi să scrieți un program Python care să citească șirul ei preferat și numărul k și să afișeze o parolă de lungime maximă care să verifice cerințele ei. În plus vă mai roagă îi spuneți și dacă soluția afișată este unică sau există mai multe astfel de parole de lungime maximă, afișând un un mesaj corespunzător: solutia optima este unica/ solutia optima nu este unica
Intrare de la tastatură
iepurasul_si_Alice_@.tara_minunilor
15
Ieșire pe ecran - nu este unică
euas_s_Al@.tarau
solutia optima nu este unica
Explicații: Codurile ASCII ale caracterelor din șir sunt
105 101 112 117 114 97 115 117 108 95 115 105 95 65 108 105 99 101 95 64 46 116 97
114 97 95 109 105 110 117 110 105 108 111 114
iar ale caracterelor din parolă sunt
101 117 97 115 95 115 95 65 108 64 46 116 97 114 97 117
Oricare două coduri consecutive din parolă diferă prin cel puțin 15 și nu există un alt șir de lungime mai mare cu această proprietate care se poate obține ștergând caractere din șirul inițial. Soluția optimă nu este unică, o altă soluție fiind de exemplu euas_s_Al@.tar_u (cu codurile 101 117 97 115 95 115 95 65 108 64 46 116 97 114 95 117)
'''

# TODO Nice to check why we receive 'solutia optima este unica' instead of 'soluti optima nu este unica'
def parola_Alice():
    sir_caractere_preferat = input()
    k = int(input())
    parola = [sir_caractere_preferat[0]]
    litera_anterioara = sir_caractere_preferat[0]
    for litera in sir_caractere_preferat:
        if abs(ord(litera) - ord(litera_anterioara)) >= k:
            parola.append(litera)
        litera_anterioara = litera
    lista_noua_sir_preferat = []
    for litera in sir_caractere_preferat:
        lista_noua_sir_preferat.append(litera)
    lista_noua_sir_preferat.reverse()
    parola_cu_sirul_inversat = [lista_noua_sir_preferat[0]]
    litera_anterioara = lista_noua_sir_preferat[0]
    for litera in lista_noua_sir_preferat:
        if abs(ord(litera) - ord(litera_anterioara)) >= k:
            parola_cu_sirul_inversat.append(litera)
        litera_anterioara = litera
    solutieUnica = True
    parola = "".join(parola)
    parola_cu_sirul_inversat.reverse()
    parola_cu_sirul_inversat = "".join(parola_cu_sirul_inversat)
    if parola == parola_cu_sirul_inversat:
        solutieUnica = False
    print(parola)
    if solutieUnica:
        print("solutia optima este unica")
    else:
        print("solutia optima nu este unica")
parola_Alice()

'''
2021-2022 Subiect 02 Subiectul 4 a)
O țeavă cu lungimea de p metri (1 ≤ p ≤ 50) trebuie să fie tăiată în cel puțin două bucăți ale căror lungimi să fie divizori ai lungimii sale. De exemplu, o țeavă cu lungimea de 4 metri poate fi tăiată în 4 bucăți de câte 1 metru, 2 bucăți de câte 2 metri sau 2 bucăți de câte 1 metru și 1 bucată de 2 metri, dar nu poate fi tăiată într-o bucată de 1 metru și o bucată de 3 metri (deoarece 3 nu este un divizor al lui 4). Scrieți un program Python care să citească de la tastatură numărul natural p și afișează toate modalitățile distincte în care poate fi tăiată corect o bară de lungime p metri, precum și numărul acestora. Două modalități de tăiere se consideră identice dacă sunt formate din aceleași bucăți de țeavă, dar în altă ordine. De exemplu, pentru o țeavă cu lungimea de 4 metri, modalitățile de tăiere 1+1+2, 1+2+1 și 2+1+1 sunt considerate identice. 
Exemplu:
Pentru p = 6 trebuie afișate următoarele 7 modalități de tăiere (nu neapărat în această ordine):
1+1+1+1+1+1
1+1+1+1+2
1+1+1+3
1+1+2+2
1+2+3
2+2+2
3+3
Nr. modalitati: 7
'''

'''
2021-2022 Subiect 02 Subiectul 4 b)
Precizați cum ar trebui adăugată o singură instrucțiune în program astfel încât să fie afișate doar modalitățile de tăiere în care au fost utilizate exact două tipuri distincte de bucăți de țeavă. Pentru exemplul anterior, aceste soluții sunt cele scrise cu roșu
'''