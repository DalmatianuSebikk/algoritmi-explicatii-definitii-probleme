"""
Se considera n proiecte, pentru fiecare proiect cunoscandu-se profitul, un termen limita 
(sub forma unei zi din luna) si faptul ca implementarea sa dureaza exact o zi. 
Sa se gaseasca o modalitate de planificare a unor proiecte astfel incat profitul total sa fie maxim.

Input:
BlackFace     2     800
Test2Test     5     700
Java4All      1     150
BestJob       2     900
NiceTry       1     850
JustDoIt      3     1000
FileSeeker    3     950
OzWizard      2     900
 
Output:
Ziua 1: BestJob 900
Ziua 2: FileSeeker 950
Ziua 3: JustDoIt 1000
Ziua 5: Test2Test 700
 
Profit maxim: 3550

sortati dupa profit. Rezolvati proiectele cat mai tarziu.
"""

proiecte = [
    # ['BlackFace', 1, 800],
    # ['Test2Test', 5, 700],
    # ['Java4All', 1, 150],
    # ['BestJob', 2, 900],
    # ['NiceTry', 1, 850],
    # ['JustDoIt', 3, 1000],
    # ['FileSeeker', 3, 950],
    # ['OzWizard', 2, 900]
    ["a", 1, 700],
    ["b", 2, 800],
    ["c", 3, 900]
]

def programareProiecte(proiecte, numar_zile):
    # salvam lungimea listei de proiecte
    n = len(proiecte)

    # sortez descrescator dpdv al profitului
    def sortezDescrescatorProfitului(lista):
        return lista[2]
    
    proiecte = sorted(proiecte, key=sortezDescrescatorProfitului, reverse=True)

    # fac o lista unde marchez timpii:
    timpiMarcati = [False] * numar_zile
    listaJoburi = ['-1'] * numar_zile

    for index in range(len(proiecte)):
        # gasim un loc liber pentru proiect
        # pornim de la ultimul loc posibil
        # pornesc de la index 2 care va fi minimul dintre numarul maxim de zile si ziua in care e programat
        # proiectul - 1, adica verificam daca exista zile in care nu facem absolut nimic, ca sa punem
        # un proiect cu profit mare.
        for index2 in range(min(numar_zile, proiecte[index][1] - 1), -1, -1):
            # cautam daca pe timpiMarcati[index2] gasim False, daca e False inseamna ca nu facem nimic in ziua
            # aia. Deci punem o activitate.
            if timpiMarcati[index2] == False:
                # am gasit o zi libera pentru un job.
                timpiMarcati[index2] = True
                listaJoburi[index2] = proiecte[index][0] # punem numele proiectului pe index2 care retine si timpul
                break


    for index in range(len(listaJoburi)):
        print("Ziua " + str(index + 1) + ": " + listaJoburi[index])    

programareProiecte(proiecte, 3)
