# Implementati o functie recursiva care returneaza ultimul element dintr-o lista.

lista = [1,2,3,4,5,6]

"""
def last(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return last(lista[1:])

print(last(lista))
"""

# Implementati o functie recursiva care returneaza elementul de pozitia i din lista. (Nu puteti folosi xs[i]).

"""
def eli(xs, i):
    if i == 0:
        return xs[0]
    else:
        return eli(xs[1:], i - 1)

print(eli(lista, i))
"""

# Implementati o functie recursiva care va inverseaza o lista.
"""
def my_reverse(xs):
    if len(xs) == 0:
        return []
    return my_reverse(xs[1:]) + [xs[0]]

print(my_reverse(lista))
"""

# Primiti o lista care poate contine alte liste. Scrieti o functie care "aplatizeaza" 
# lista: xs = [1, [2, [3, 4], 5], 6] --> [1,2,3,4,5,6]. 
# Puteti verifica daca o variabila are un anumit tip de date folosind: isinstance(xs, list) == True.

"""
def flatten(xs):
    rez = []
    for item in xs:
        if isinstance(item, list) == True:
            rez.extend(flatten(item))
        else:
            rez.append(item)

    return rez

print(flatten(lista))
"""

# 5. Scrieti o functie recursiva care va dubleza elementele. 
# Ex: duplicate([1,2,3]) -> [1,1,2,2,3,3]

"""
def duplicate(xs):
    
    if len(xs) == 0:
        return []
    else:
        return [xs[0], xs[0]] + duplicate(xs[1:])
    

print(duplicate(lista))
"""

# Scrieti o functie recursiva care va replica elementele de un numar n de ori. 
# Ex: replicate([1,2], 3) -> [1, 1, 1, 2, 2, 2].

"""
def replicate(xs, n):
    lista = []
    if len(xs) == 0:
        return []
    else:
        for i in range(n):
            lista.append(xs[0])
        return lista + replicate(xs[1:], n)

print(replicate(lista, 3))
"""

# Scrieti o functie recursiva care va sterge al k-lea element din lista si returneaza elementul sters si lista.
# Exemplu: remove_at([1,2,3,4,5,6], 3) --> (3, [1, 2, 3, 5, 6])

"""
def remove_at_secundar(xs, ind):
    if ind == len(xs) - 1:
        xs.pop(ind)
        return xs
    else:
        xs[ind] = xs[ind + 1]
        return remove_at_secundar(xs, ind + 1)


def remove_at(xs, ind):
    valoare = xs[ind]
    return (valoare, remove_at_secundar(xs, ind))

print(remove_at([1,2,3,4], 2))
"""

"""
Primiti un obiect iterabil. 
Afisati fiecare element cu print. Nu puteti folosi for. Utilizati iteratori si while.
"""
    






    






    
