# LISTE IN PYTHON - Tine o colectie ordonata (nu isi schimba pozitiile) de elemente

# DIFERENTA DINTRE VECTORI SI LISTE: La liste nu e obligatoriu ca elementele sa fie de acelasi tip

# OPERATII LISTE: (aproape asemanatoare ca la vectori fara cateva):

    # CREAREA UNEI LISTE: lista = [] (poti sa pui si elemente)
    # ACCESAREA UNOR ELEMENTE DIN LISTA: ca in vector, lista[2]
    # TRAVERSAREA UNOR ELEMENTE DIN LISTA: ca in vector, cu un for
    # ADAUGAREA UNUI NOU ELEMENT IN LISTA: append() -> lista.append(valoare) sau insert() -> lista.insert(pozitie, val)
                                        #  mai exista si extend(alta_lista) daca vrei neaparat
    # MODIFICAREA UNUI ELEMENT DIN LISTA: lista[pozitie] = alta_valoare
    # SLICING: operatorul slice ":"
    # STERGEREA UNUI ELEMENT DIN LISTA: pop -> (pt ultimul element) sau del lista[pozitie1 : pozitie2] SAU remove()
    # CAUTAREA UNUI ELEMENT DIN LISTA: poti folosi "in":
""" 
        for numar in lista:
                if 14 in lista:
                    print("da frate")
"""
    # sau putem folosi cautare liniara: (tot cu for)

    # CONCATENAREA A DOUA LISTE: se poate face cu operatorul +
"""
        a = [1,2,3]
        b = [4,5,6]
        c = a + b
        print(c)
"""
    # REPETAREA LISTEI DE MAI MULTE ORI: operatorul *
"""
        a = [0,1]
        a *= 4 # lista devine [0,1,0,1,0,1,0,1] (se repeta 0,1 de 4 ori)
"""
    # FUNCTII PREDEFINITE IN PYTHON PENTRU LISTE:
        # len(lista) -> numarul de elemente a listei
        # max(lista) -> elementul maxim din lista
        # min(lista) -> minimul din lista
        # sum(lista) -> suma elementelor din lista

    # LISTELE SI STRINGURILE:
        # daca folosim functia list peste un string, de exemplu:
"""
        a = 'lista'
        b = list(a) -> ['l','i','s','t','a']
"""
        # poti folosi a.split(delimitator) pentru a separa un string intr-o lista de cuvinte

#  OBSERVATII:
    #   anumite metode nu returneaza nimic, ci fac doar modificarile pe lista.
    #   sa ai grija la documentatie and stuff sa nu combini 2 operatii care fac acelasi lucru si sa faci o supa
    #   recomandabil ar fi sa faci un backup la lista 
