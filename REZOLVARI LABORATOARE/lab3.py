# Primiti o lista de numere naturale mai mici decat 100. Sortati lista folosind functii din Python.
"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista.sort()
print(lista)
"""

# Primiti o lista de numere naturale mai mici decat 100. Sortati eficient lista (vectori de frecventa).
"""
lista = [ 93, 11, 63, 47,29, 84, 61, 7, 3, 100, 23, 77, 79, 64, 37, 15, 74, 96]
frecv = [0 for i in range(0, 101)]
listaord = []
for nr in lista:
    frecv[nr] += 1

for i in range(0, 101):
    if frecv[i] != 0:
        listaord.append(i)

print(listaord)
"""

# Primiti un string si o lista de cuvinte. Afisati pentru fiecare cuvant din acea lista daca apare sau nu in string.
"""
prop = "Ana are cinci mere si Maria ia doua mere cate mere are Ana"
cautate = ["are", "mere", "iar"]

for cuvant in cautate:
    if cuvant in prop:
        print(cuvant + ": apare")
    else:
        print(cuvant + ": nu apare")
"""

# Afisati frecventa literelor dintr-un sir: "ana are mere" => a = 3, n = 1 ...
"""
prop = "ana are cinci mere si maria ia doua mere cate mere are ana"
dictionar = {}

for i in range(len(prop)):
    if prop[i] in dictionar:
        dictionar[prop[i]] += 1
    else:
        dictionar[prop[i]] = 1

print(dictionar)
"""

# Afisati frecventa cuvintelor dintr-un sir.
"""
s = "Ana are cinci mere si Maria ia doua mere. Cate mere are Ana?"

delimitatori = ",./?!"

for delimitator in delimitatori:
    s = s.replace(delimitator, "")

cuvinte = s.split(' ')

dictionar = {}
print(cuvinte)

for cuvant in cuvinte:
    if cuvant in dictionar:
        dictionar[cuvant] += 1
    else:
        dictionar[cuvant] = 1
print(dictionar)
"""

# 6. Primiti un string. Trebuie sa afisati pentru fiecare litera la ce pozitii apare in string (nu neaparat in ordine). Exemplu: s = “ana are mere”, 
        # a - [0, 2, 4] n - [1], r - [5, 10] ...

"""
string = "Ana are cinci mere si Maria ia doua mere cate mere are Ana"
dictionar = {}

for i in range(len(string)):
    if string[i] != ' ':
        if string[i] in dictionar:
            dictionar[string[i]].append(i)
        else:
            dictionar[string[i]] = [i,]

print(dictionar)
"""

# 7. Primiti un string. Trebuie sa afisati pentru fiecare cuvant la ce pozitii apare in string. Exemplu: s = “ana are mere si ana vrea pere”, 

        # ana - [0, 4] # pozitii intre cuvinte
        # are - [1]

"""
s = "ana are mere si ana vrea pere"
cuvinte = s.split(' ')
dictionar = {}


for i in range(len(cuvinte)):
    if cuvinte[i] in dictionar:
        dictionar[cuvinte[i]].append(i)
    else:
        dictionar[cuvinte[i]] = [i,]

print(dictionar)
"""

# Primiti doua cuvinte formate din litere mici. Verificati daca sunt anagrame. 
# Exemplu: “emerit” si “treime” sunt anagrame, dar “emerit” si “treimi” nu sunt.

"""
a = "emerit"
b = "treime"
dictionar1 = {}
dictionar2 = {}

if len(a) != len(b):
    print('NU')
else:
    for i in range(len(a)):
        if a[i] in dictionar1:
            dictionar1[a[i]] += 1
        else:
            dictionar1[a[i]] = 1
    
    for i in range(len(b)):
        if b[i] in dictionar2:
            dictionar2[b[i]] += 1
        else:
            dictionar2[b[i]] = 1

    if dictionar1 == dictionar2:
        print("DA")
    else:
        print("NU")
"""

# 9. Primiti un sir de numere naturale si o serie de operatii. Operatiile sunt de 2 tipuri:

    # 1 a b - afisati suma elementelor dintre a si b
    
    # 2 a b - valoarea de pe pozitia a devine b

# Pentru fiecare operatie de tip 1, afisati suma.

"""
xs = [2, 9, 0, 5, 1, 8, 7, 3, 10, 4, 11, 6]
ops = [                                     # m
       (1, 0, 11),  # 66
       (2, 2, 5),
       (1, 0, 5),   # 30
       (1, 5, 10),  # 43
       (2, 6, 4),
       (1, 4, 7),   # 68
       (1, 0, 11)   # ...
]

for operatie in ops:
    if operatie[0] == 1:
        s = 0
        for i in range(operatie[1], operatie[2] + 1):
            s += xs[i]
        print(s)
    
    elif operatie[0] == 2:
        xs[operatie[1]] = operatie[2]
"""

# Ciurul lui Eratostene. Afisati numerele prime pana la n.
"""
n = 100
ciur = [ True for x in range(n + 1)] # Consideram un vector de bool, unde pozitia e numarul si valoarea din vector este
# True - pozitia e prima
# False - pozitia nu e prima

# 0 si 1 nu sunt prime, deci le notam cu False
ciur[0] = False
ciur[1] = False

for i in range(2, n + 1):
    if ciur[i] == True: # identificam in prima parcurgere ce numere sunt True pana la n
        for j in range(i * 2, n + 1, i):    # Dupa care mergem prin multiplii lor , pasul creste cu i pt ca v[i * 2], v[i * 3] ... nu sunt primi
            ciur[j] = False  # multiplii lui ciur[i] nu sunt primi

for i in range(n + 1):
    if ciur[i] == True:
        print(i)
"""   


