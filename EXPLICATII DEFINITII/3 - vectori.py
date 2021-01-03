# Vector - o colectie simpla de valori/obiecte

# PROPRIETATI VECTORI:
    #   - Poate stoca date de un anume tip specificat
    #   - Elementele din vector se afla in locuri foarte apropiate din memorie (elementele sunt unul langa altul)
    #   - Fiecare element are un index unic
    #   - Dimensiunea este predefinita si nu poate fi modificata

# TIPURI DE VECTORI:
    #   - unidimensionali V[100] (valori cu un singur index)
    #   - multidimensionali (valori cu mai multi incecsi, de ex matricea)

# VECTORII IN MEMORIE:
#   - in RAM, elementele din vector sunt asezate unul langa altul (proprietate)

# OPERATII DE BAZA CU VECTORI:

    # CREAREA UNUI VECTOR:
    #   - il atribuim unei variabile
    #   - definim tipul elementelor stocate
    #   - definim dimensiunea
    # In Python ca sa cream un vector importam modulul Array:
        # from array import *
        # vector = array(tipDate, [elemente/initializatori])

    # in locul lui tipDate, avem un cod care inseamna ceva:
        # 'b' = char cu semn
        # 'B' = char fara semn
        # 'u' = Py unicode
        # 'h' = short cu semn
        # 'H' = short fara semn
        # 'i' = int cu semn
        # 'I' = int fara semn
        # 'l' = long cu semn
        # 'L' = long fara semn
        # 'q' = long long cu semn
        # 'Q' = long long fara semn
        # 'f' = float
        # 'd' = double
"""
        from array import * 
        vector = array('i', [1, 2, 3, 4, 5])
        print(vector)   # complexitatea este O(1) 
"""

    # INSERAREA UNUI ELEMENT IN VECTOR:
        # vector[4] = 5 # daca nu are element pe pozitia 4
        # daca dorim sa adaugam un element pe o pozitie care are deja un element (time consuming):
            # - muti elementele la dreapta cu o pozitie daca ai posibilitatea,
            # ca altfel trebuie sa creezi un vector mai mare
            # - atribui

"""
        # OBS: INSERTIA LA INCEPUTUL VECTORULUI ARE O COMPLEXITATE O(N)
        # python are deja o functie de insert vector.insert(pozitie, valoare)
        vector.insert(5, 100)
        print(vector)   # 1, 2, 3, 4, 5, 100
"""
    # TRAVERSAREA UNUI VECTOR:
        # traversarea = trecerea prin fiecare element din vector pana la final
        # o faci cu un for
"""
        # traversarea unui vector are o complexitate O(n)
        for numar in vector:
            print(i)
"""
    # ACCESAREA UNUI ELEMENT DIN VECTOR:
        # vector[index]
    
    # CAUTAREA UNUI ELEMENT IN VECTOR:
        # daca stii pe ce pozitie se afla, poti folosi indexul (vector[2])
        # poti merge cu un for (cautare secventiala) O(n)
        # daca vectorul e sortat, poti face cautare binara O(logn)

    # STERGEREA UNUI ELEMENT DIN VECTOR:
        # muti elementele cu o pozitie la stanga (peste elementul respectiv)

# python are o functie de remove gata facuta: vector.remove(valoare_din_vector)

# PRACTICE VECTORI:

# 1. Createa unui vector si traversarea acestuia:

from array import *
vector = array('i', [1,2,3,4,5])

for i in vector:
    print(i)

# 2. Accesarea unui element individual prin index

print(vector[0])

# 3. Append la orice valoare cu append()

vector.append(100)
print(vector)

# 4. Inserarea unei valori in vector cu insert()

vector.insert(3, 150)
print(vector)

# 5. Extinde vectorul cu extend()

vector2 = array('i', [7, 8, 9, 10])
vector.extend(vector2)
print(vector)

# 6. Adauga elemente dintr-o lista intr-un array cu fromlist()

lista = [11,12,13,14]
vector.fromlist(lista)
print(vector)

# 7. Stergerea oricarui element cu remove()

vector.remove(100)
print(vector)

# 8. Stergerea ultimului element cu pop()

vector.pop()
print(vector)

# 9. Afla pe de index se afla un element folosind index()

print(vector.index(4))


# 10. Inverseaza un vector cu reverse()

vector.reverse()
print(vector)

vector.reverse()

# 11. Foloseste buffer_info() pentru informatii depspre buffer
print(vector.buffer_info())

# 12. Numara aparitiile unui element cu count()

print(vector.count(1))

# 13. Conversia de la vector la string cu tostring()

# string = vector.tostring() NU MERGE!
# print(string)

# 14. Conversia de la vector la lista cu tolist()

lista = vector.tolist()
print(lista)

# 15. Append la string cu fromstring()

# 16. Slicing in vector

print(vector[1:4]) # -> ia elementele de la 1 la 3 (4 - 1 ca sa faci asocierea corect)