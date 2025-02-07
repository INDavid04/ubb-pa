''' Subiectul 1 (3 p.) a) (1.5 p.)
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

''' b) (0.5 p.) Înlocuiți punctele de suspensie din instrucțiunea litere_10 = […] cu o expresie astfel
încât lista să fie inițializată cu primele 10 litere mici din alfabetul englez.
'''
litere10 = [chr(i) for i in range (ord('a'), ord('a') + 10)]
print(litere10)

''' c) (1 p.) Considerăm o funcție recursivă a cărei complexitate este dată de următoarea relație de
recurență:
T(1) = T(2) = 1
T(n) = T(n/3) + 2, pentru n ≥ 1
Determinați complexitatea funcției respective. 
'''
O(log3(n))

''' Subiectul 2 - metoda Greedy (3 p.)
Complexitatea maximă a soluției: O(nlog2 n )
Considerăm n spectacole S1, S2, ..., Sn pentru care cunoaștem intervalele lor de desfășurare
[s1, f1), ..., [sn, fn), toate dintr-o singură zi. Având la dispoziție o singură sală, în care putem
să planificăm un singur spectacol la un moment dat, să se determine numărul maxim de
spectacole care pot fi planificate fără suprapuneri. Un spectacol Sj poate fi programat
după spectacolul Si dacă sj ≥ fi. Justificați corectitudinea programului și complexitatea sa.
'''

''' Subiectul 3 - metoda Programării Dinamice (3 p.)
Complexitatea maximă a soluției: O(n2)
Să se determine un subșir crescător de lungime maximă al unui șir t format din n numere
întregi.
'''

''' Subiectul 4 - metoda Backtracking (3 p.)
Să se afișeze toate permutările mulțimii A = {1,2, ..., n}, unde n este un număr natural nenul
'''
