"""
Primiti un numar n. Afisati numarul 2^n folosind operatii pe biti.

Idee: folositi o shiftare pe biti.

-------------------------------------------------
n = 5
print(1 << n)
-------------------------------------------------

"""



"""
Primiti un numar in baza 2. verificati daca primul bit (0) este setat (daca numarul este impar) folosind operatii pe biti.

Idee: numarul 1 este impar; cum arata numerele impare in baza 2?

-------------------------------------------------
n = 4

if n & 1 == 1:
    print("Impar")
else:
    print("Par")
-------------------------------------------------
"""

"""
Primiti un numar in baza 2. Verificati daca bit-ul 2 este setat.

Exemplu: 13 = 1101; bit-ul 3 este 1, bit-ul 2 este 1, bit-ul 1 este 0, bit-ul 0 este 1.

-------------------------------------------------
n = 0b1101

if n >> 2 & 1 == 1:
    print("da")
else:
    print("nu")
"""

"""
Primiti un numar natural. Setati bit-ul 1 la 1.

Exemplu: n = 13 => afisati 15, pentru n = 14 => afisati 14

-------------------------------------------------

n = 14

print(n | 0b10)

"""

"""
Primiti un numar natural. De-setati bit-ul 0 (bit-ul 0 devine 0).

Exemplu: n = 4 => afisati 4, pentru n = 5 => afisati 4
"""
"""
n = 5

print((n >> 1) << 1)
"""

"""
Primiti un numar natural. Scrieti o instructiune (pe biti) pe care daca o executati de doua ori, primiti inapoi rezultatul initial. Ex fara biti:

x = 5
x = x * (-1) # numarul este -5
x = x * (-1) # numarul este 5

Idee: operatia XOR.

-----------------------------------------------------
x = 5
y = x ^ x
y = y ^ x

print(y)
-----------------------------------------------------
"""

"""
Optional. Convertiti un numar natural in baza 2 (sub forma unei liste din Python). 
Apoi convertiti lista formata din 0 si 1 inapoi in numarul initial.

Exemplu:
    f(12) = [1, 1, 0, 0]
    g([1, 1, 0, 0]) = 12
 
Idee: - extrageti cifrele unui numar din baza 10 mai intai
        (1523 -> [1, 5, 2, 3] si [1,9,3,4] -> 1934)   
      - pentru a inversa o lista: xs[::-1]   


-----------------------------------------------------
n = 12

def toBin(n):
    binstr = format(12, '0b')
    binlist = []
    
    for cifra in binstr:
        binlist.append(int(cifra))

    return binlist

lista = toBin(n)

print(lista)

def toDec(lista):
    numar = 0
    listainv = lista[::-1]

    for cifra in range(len(listainv)):
        if listainv[cifra] != 0:
            numar += 2 ** cifra
    
    return numar

n = toDec(lista)
print(n)       

-----------------------------------------------------
"""


"""
Verificare numar putere a lui 2

-----------------------------------------------------

n = 4
m = n - 1

if n & m == 0:
    print("DA")
else:
    print("NU")

-----------------------------------------------------
"""


"""
Schimbati toti biti de 0 de la final in 1

-----------------------------------------------------
n = 408
m = n - 1

print(bin(n | m))
-----------------------------------------------------
"""

"""
Stergeti ultimul bit de 1 setat

-----------------------------------------------------

n = 104
m = n - 1

print(bin(n & m))
"""

"""
Primiti 3 numere: n, i si j. Interschimbati bitii de pe pozitile i si j.


-----------------------------------------------------
n = input("Numarul:")
n = int(n, 2)

i = int(input("pozitia de pe i:"))
j = int(input("pozitia de pe j:"))

# extragem bitii cu shiftare la dreapta si AND 1

bit1 = (n >> i) & 1
bit2 = (n >> j) & 1

# XORezi bitii intre ei ca sa poti sa faci interschimbarea

x = bit1 ^ bit2

# faci loc pentru bitii interschimbati
x = (x << i) | (x << j)

# afisezi rezultatul Xorului cu numarul initial

print(bin(n ^ x))
-----------------------------------------------------
"""

"""
Primiti un numar pe 32 de biti. Construiti numarul care are biti in ordine inversa. Exemplu (8 biti):

n = input("Numar:")

print(bin(n)[:1,-1])
"""

"""
Doua cuvinte sunt p-rime daca au ultimele p litere egale. Scrieti o functie care primeste doua cuvinte si returneaza p maxim pentru care cuvintele sunt p-rime.

-----------------------------------------------------
s1 = “niciodata”
s2 = “fata”

find_p_rime(s1, s2) == 3

s1 = input("sir1:")
s2 = input("sir2:")

def find_p_rime(s1, s2):
    s1rev = s1[::-1]
    s2rev = s2[::-1]

    print(s1rev, s2rev)

    if len(s1) < len(s2):
        maxim = len(s2)
    else:
        maxim = len(s1)

    p = 0

    for index in range(maxim):
        if s1rev[index] == s2rev[index]:
            p += 1
        else:
            break
    
    return p

print(find_p_rime(s1, s2))
-----------------------------------------------------
"""

"""
Limba pasareasca
In limba pasareasca, de fiecare data cand avem o vocala intr-o propozitie vom concatena litera p si acea vocala. 
Primind un string in limba romana, scrie o functie encrypt care converteste string-ul in limba pasareasca si o functie decrypt care converteste un string din limba pasareasca in limba romana (daca se poate). 
Pentru verificare folositi: s == decrypt(encrypt(s))

-----------------------------------------------------

s = "maree"

def encrypt(s):
    sirnou = ""
    vocale = "aeiouAEIOU"
    for i in range(len(s)):
        if s[i] in vocale:
            sirnou += s[i]
            sirnou += "p" + s[i]
        else:
            sirnou += s[i]
    
    return sirnou

s2 = "maparepeepe"


def decrypt(s):
    pasarele = ["pa", "pe", "pi", "po", "pu"]

    for pasarea in pasarele:
        if pasarea in s:
            s = s.replace(pasarea, '')
    
    return s



print(encrypt(s))
print(decrypt(s2))
"""

"""
Primiti un string fara spatii in care literele se repeta des. Scrieti o functie care comprima string-ul astfel:

-----------------------------------------------------
s = "aabbbbaccc"

def functie(s):
    sirnou = ""
    p = 1

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            p += 1
        else:
            sirnou += s[i] + str(p)
            p = 1
    
    sirnou += s[i] + str(p)
    return sirnou

print(functie(s))
-----------------------------------------------------
"""

"""
Primiti o poezie, trebuie sa gasiti p cu prop. ca versurile sunt p-rime

poezie = “””A fost odată ca-n poveşti,
A fost ca niciodată.
Din rude mari împărăteşti,
O prea frumoasă fată.”””

print(find_p_rime(poezie))

Primiti poezia fara diacritice, dar cu semne de punctuatie!

Idee:
    i) scapati de semnele de punctuatie cu .replace(semn, ‘’);
    ii) faceti un split pe versuri .split(“ “);
    iii) pentru fiecare tip de rima, folositi functia de la problema 1 pentru a gasi p-ul;
    iv) luati valoarea maxima care este respectata de toate versurile;
Bonus:
    rezolvati problema care contine toata poezia (nu primiti doar o strofa,
    ci toata poezia; idee: faceti split initial pe strofe .split(“\n\n”) si 
    folositi functia de mai sus care merge pe strofe.
"""

"""
def find_p_rime(s1, s2):
    s1rev = s1[::-1]
    s2rev = s2[::-1]

    

    if len(s1) < len(s2):
        maxim = len(s2)
    else:
        maxim = len(s1)

    p = 0

    for index in range(maxim):
        if s1rev[index] == s2rev[index]:
            p += 1
        else:
            break
    
    return p



poezie = '''A fost odată ca-n poveşti,
A fost ca niciodată.
Din rude mari împărăteşti,
O prea frumoasă fată.

Şi era una la părinţi
Şi mândră-n toate cele,
Cum e Fecioara între sfinţi
Şi luna între stele.

Privea în zare cum pe mări
Răsare şi străluce,
Pe mişcătoarele cărări
Corăbii negre duce.

Îl vede azi, îl vede mâini,
Astfel dorinţa-i gata;
El iar, privind de săptămâni,
Îi cade draga fata.

Cum ea pe coate-şi răzima
Visând ale ei tâmple,
De dorul lui şi inima
Şi sufletu-i se împle.

Şi cât de viu s-aprinde el
În orişicare sară,
Spre umbra negrului castel
Când ea o să-i apară.'''



def rima_pe_strofa(strofa):

    semnePunctuatie = ",.;?!"
    for semn in semnePunctuatie:
        strofa = strofa.replace(semn, '')
        
    versuri = strofa.split("\n")

    # imperecheata
    p1 = find_p_rime(versuri[0], versuri[1])
    p2 = find_p_rime(versuri[2], versuri[3])

    min1 = min(p1, p2)

    # incrucisata
    p1 = find_p_rime(versuri[0], versuri[2])
    p2 = find_p_rime(versuri[1], versuri[3])

    min2 = min(p1, p2)

    #imbratisata
    p1 = find_p_rime(versuri[0], versuri[3])
    p2 = find_p_rime(versuri[1], versuri[2])

    min3 = min(p1, p2)
    raspuns = max(min1, min2, min3)
    return raspuns



def rima_pe_poezie(poezie):
    strofe = poezie.split('\n\n')
    lista_minimi = []

    for strofa in strofe:
        lista_minimi.append(rima_pe_strofa(strofa))
    
    print(max(lista_minimi))

rima_pe_poezie(poezie)

"""

"""
Rot(13)
Primiti un string s si un numar k. Trebuie sa rotiti fiecare litera din s cu k pozitii mai la dreapta.
"""
"""
s = "ehfc"
k = 3

def rot(s, k):
    sirnou = ""
    for caracter in s:
        ordin = ord(caracter)
        if ordin + k <= 122:
            ordin += k
            sirnou += chr(ordin)
        else:
            ordin += k
            ordin = ordin - 122 + 96 # NU 97 pentru ca pe 97 este a, si noi "am trecut deja" de a 
            sirnou += chr(ordin)
    
    return sirnou

def irot(s, k):
    # putem roti de 26 - k ori ca sa ajungem la inceput (operatia %), ca sunt 26 de litere (fara diacritice) in alfabet
    return rot(s, 26 - k)

print(irot(s, 3))
"""

"""
Daca aveti o multime Q = {1, 2, 3}, multimea partilor lui Q se noteaza 
2Q = {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}. 
Exista o functie bijectiva intre numerele {0, … n - 1} si multimea 2Q. 
Gasiti aceasta functie si implementati un program care va afiseaza pentru o lista xs data,
multimea partilor lui xs. --- BACKTRACKING FUTU TI MORTII MA TII
"""

"""
set = [10, 23, 42, 1 ,4]
parts_set = []

def subsets(set, k):
    if k == len(set):
        print(parts_set)
    else:
        subsets(set, k + 1)
        parts_set.append(set[k])
        subsets(set, k + 1)
        parts_set.pop()
    
subsets(set, 0)
"""

"""
Definim greutatea unui numar ca numarul de biti de 1 din reprezentarea sa in binar. 
Scrieti un program care pentru un numar x dat, gaseste y, care este cel mai apropiat numar de acesta a.i.:

i) greutate(x) == greutate(y)
ii) ∀z care respecta i) |y - x| <= |z - x|

"""
"""
# 1. gasesti cea mai mica putere a lui 2 mai mare sau egala decat x

x = 1110
x = str(x)
x = int(x, 2)   # l am convertit din baza 2 in 10

# vad cati de unu are x
aux = x
numarDeUnu = 0
while aux > 0:
    if aux % 2 == 1:
        numarDeUnu += 1
    aux //= 2

putere = 2
exponent = 0

while putere ** exponent < x:
    exponent += 1   

putereMaxima = putere ** exponent - 1 # am calculat cati biti folosim
formatBinar = '{0:0' + str(exponent) + 'b' + '}' # ne ajuta sa scriem cum trebuie numerele

# fac o lista cu numerele care au aceeasi greutate
lista_valizi = []

for i in range(1, putereMaxima):
    aux = i
    catiDeUnuAvem = 0
    while aux > 0:
        if aux % 2 == 1:
            catiDeUnuAvem += 1
        aux //= 2
    if catiDeUnuAvem == numarDeUnu and i != x:
        lista_valizi.append(i)
    
# fac un dictionar pentru fiecare cheie element valid ii atribui valoarea dif absolute
diferente = {}
for i in lista_valizi:
    diferente[i] = abs(i - x)

diferente = diferente.items()

def tuplu(tuple):
    return tuple[1]

diferente = sorted(diferente, key=tuplu)
tupluBun = diferente[0]
print(formatBinar.format(tupluBun[0]))
"""


"""
Calculati x * y, fara a folosi operatorul *
"""
"""
x = 2
y = 3
adunare = 0

if x <= y:
    for i in range(x):
        adunare += y
    print(adunare)
else:
    for i in range(y):
        adunare += x
    print(adunare)
"""

"""
Primiti un string s. Trebuie sa gasiti k maxim astfel incat s sa se poate scrie ca t+t+...+t de k ori.

Exemplu: s = “abcabc” => gasim t = “abc” => s = t + t => k = 2
"""

"""
s = "cicici"
t = ""

i = 1
while i <= len(s):
    t = s[0:i]
    stringNou = t * (len(s) // i)
    if stringNou == s:
        print(len(s) // i)
        break
    i += 1
"""

"""
Primiti o adresa IP fara puncte. 
Trebuie sa afisati toate adresele IP posibile care se pot forma (sa puneti 3 puncte)
 1721601 -> 172.16.0.1 | 17.216. 0. 1 | 1.72.160.1
"""

"""
def verificare(ip):
    ip = ip.split(".")
    
    for i in ip:
        if len(i) >3 or int(i) < 0 or int(i) > 255: # cand nu e ceva intre 0 si 255 pa
            return False
        if len(i) > 1 and int(i) == 0:  # cand incepe cu 0 pa
            return False
        if (len(i) > 1 and int(i) != 0 and i[0] == '0'): # asemanator cu conditia de mai sus
            return False
    
    return True

def convert(s):
    lungime = len(s)

    if lungime > 12:
        return []

    l = []
    ipnou = s
    # Generarea combinatiilor:
    for i in range(1, lungime - 2):
        for j in range(i + 1, lungime - 1):
            for k in range(j + 1, lungime):
                ipnou = ipnou[:k] + "." + ipnou[k:]
                ipnou = ipnou[:j] + "." + ipnou[j:]
                ipnou = ipnou[:i] + "." + ipnou[i:]
                
                if verificare(ipnou):
                    l.append(ipnou)
                
                ipnou = s

    return l

A = "1721601"
print(convert(A))
"""






















