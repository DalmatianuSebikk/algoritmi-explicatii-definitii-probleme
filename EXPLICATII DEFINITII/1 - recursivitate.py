# RECURSIA - o modalitate de a rezolva o problema cu o functie care se autoapeleaza (faci problema din ce in ce mai mica)

# PROPRIETATI:
"""
    1. Aceeasi operatie, diferite inputuri
    2. La fiecare pas, sunt inputuri mai mici pentru a face problema mai mica (pentru a gasi mai optim soluatia)
    3. Conditia de baza este necesara, altfel vei avea o bucla infinita 
"""

# ASEMANAREA DINTRE FUNCTIILE RECURSIVE SI PAPUSILE RUSESTI

# def russianDoll(doll):
#     if doll == 1:
#         print("dolls are opened")
#     else:
#         russianDoll(doll - 1)

# DE CE AVEM NEVOIE DE RECURSIE?
# Reduci problema la ceva mai mic

# Cand recunosti recursia?
"""
    1. Cand poti imparti problema in mai multe subprobleme
    2. Design-ul unui algoritm care calculeaza al n-ulea [...]
    3. Algoritm care afiseaza n
    4. metoda care calculeaza toate cele de mai sus
    5. practice (ca sa identifici problemele cu recursivitate)
"""
# Cel mai des recursivitatea se utilizeaza la arbori si grafuri

# CUM FUNCTIONEAZA RECURSIA?

# def functieRecursiva(parametrii):
#     if iesire daca conditia e satisfacuta:
#         return valoare:
#     else:
#         functieRecursiva(parametrii modificati)

# functia recursiva este stocata in stiva (LIFO). Fiecare apelare se pune intr-o stiva si la final se goleste.
# consideram o functie recursiva 

# def f1(n):
#     if n < 1:
#         print("n mai mic decat 1")
#     else:
#         f(n - 1)
#         print(n)

# OUTPUT PT N = 5: n mai mic decat 1, 1 2 3 4 5

# RECURSIV VS ITERATIV

""" RECURSIV
def putereDoi(n):
    if n == 0:
        return 1
    else:
        return 2 * putereDoi(n - 1)

print(putereDoi(3))"""

""" ITERATIV
def putereDoi(n):
    i = 0
    putere = 2
    while i < n:
        putere *= 2
        i += 1
    return putere

print(putereDoi(3))"""

# Rezolvarea recursiva este mai ineficienta din punct de vedere a spatiului si al memoriei 
# din cauza folosirii stivei si faptului ca procesorului ii ia mai mult timp sa faca push si pop

# CAND SA FOLOSESTI RECURSIA?
'''
    - cand putem imparti problema in mai multe sub probleme similare
    - cand suntem ok cu folosirea a mai mult timp si spatiu
    - cand avem nevoie de o solutie functionala in loc de una eficienta
    - traversarea unui arbore
'''

# CAND SA NU FOLOSESTI RECURSIA?
'''
    - cand timpul si memoria conteaza
'''

# CUM SCRII FUNCTII RECURSIVE?
# PASUL 1: identifici relatia de recursivitate (cum depind intre ei termenii de exemplu)
# PASUL 2: identifici conditia de oprire (ca sa nu ai bucla infinita)
# PASUL 3 (optional): verifici alte conditii care ar putea sa produca erori

