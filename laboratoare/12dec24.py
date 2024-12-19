# Seminar 6
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