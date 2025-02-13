'''
2021-2022 Subiect 01
Subiectul 4
'''

'''
2021-2022 Subiect 01
Subiectul 3
'''

'''
2021-2022 Subiect 01
Subiectul 2
'''

'''
2021-2022 Subiect 01
Subiectul 1 c)
'''

'''
2021-2022 Subiect 01
Subiectul 1 b)
'''

'''
2021-2022 Subiect 01
Subiectul 1 a)
'''

'''
2021-2022 Restanta & Marire
Subiectul 2
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

'''
MySolution
m, n = int(input().split())
for i in range(1, m + 1):
    for j in range (1, n + 1):
        a[i][j] = int(input())
pos = tuple()
minim1 = a[1][1]
for i in range(2, n + 1):
    if a[1][i] < minim1:
        minim1 = a[1][i]
        savei, savej = 1, i
        pos.append(savei)
        pos.append(savej)
sum = minim1
for i in range(2, m):
    minim2 = a[i][1]
    for j in range(2, n + 1):
        if a[i][j] < minim2 and a[i][j] > minim1:
            minim2 = a[i][j]
            savei, savej = i, j
            pos.append(savei)
            pos.append(savej)
    sum += minim2
    minim1 = minim2
maxim = a[m][1]
for i in range(2, n + 1):
    if a[m][i] > maxim:
        maxim = a[m][i]
        savei, savej = m, i
        pos.append(savei)
        pos.append(savej)
print(sum)
limit = len(pos)
for i in range(0, limit, 2):
    print(f"{pos[i]} {pos[i + 1]}")
'''

'''
GPT Solution
m, n = map(int, input().split())

# Inițializare corectă a matricei
a = [list(map(int, input().split())) for _ in range(m)]

# Listă pentru stocarea pozițiilor
pos = []

# Alegem cel mai mic element din prima linie
minim1 = min(a[0])
savei, savej = 0, a[0].index(minim1)
pos.append((savei + 1, savej + 1))  # Salvăm pozițiile 1-based

suma = minim1

# Căutăm cele mai mici valori din fiecare linie
for i in range(1, m - 1):
    minim2 = float('inf')
    for j in range(n):
        if minim1 < a[i][j] < minim2:
            minim2 = a[i][j]
            savei, savej = i, j

    if minim2 != float('inf'):
        suma += minim2
        pos.append((savei + 1, savej + 1))
        minim1 = minim2

# Găsim valoarea maximă din ultima linie
maxim = max(a[m - 1])
savei, savej = m - 1, a[m - 1].index(maxim)
pos.append((savei + 1, savej + 1))

# Afișare rezultate
print(suma)
for i, j in pos:
    print(i, j)
'''

''' 
Model Subiectul 1 (3 p.) a) (1.5 p.)
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
print(dict_divizori)

''' 
Model b) (0.5 p.) Înlocuiți punctele de suspensie din instrucțiunea litere_10 = […] cu o expresie astfel
încât lista să fie inițializată cu primele 10 litere mici din alfabetul englez.
'''
litere10 = [chr(i) for i in range (ord('a'), ord('a') + 10)]
print(litere10)

''' 
Model c) (1 p.) Considerăm o funcție recursivă a cărei complexitate este dată de următoarea relație de
recurență:
T(1) = T(2) = 1
T(n) = T(n/3) + 2, pentru n ≥ 1
Determinați complexitatea funcției respective. 
'''
O(log3(n))

'''
Model Subiectul 2 - metoda Greedy (3 p.)
Complexitatea maximă a soluției: O(nlog2 n )
Considerăm n spectacole S1, S2, ..., Sn pentru care cunoaștem intervalele lor de desfășurare
[s1, f1), ..., [sn, fn), toate dintr-o singură zi. Având la dispoziție o singură sală, în care putem
să planificăm un singur spectacol la un moment dat, să se determine numărul maxim de
spectacole care pot fi planificate fără suprapuneri. Un spectacol Sj poate fi programat
după spectacolul Si dacă sj ≥ fi. Justificați corectitudinea programului și complexitatea sa.
'''

''' 
Model Subiectul 3 - metoda Programării Dinamice (3 p.)
Complexitatea maximă a soluției: O(n2)
Să se determine un subșir crescător de lungime maximă al unui șir t format din n numere
întregi.
'''

''' 
Model Subiectul 4 - metoda Backtracking (3 p.)
Să se afișeze toate permutările mulțimii A = {1,2, ..., n}, unde n este un număr natural nenul
'''
