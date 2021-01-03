class Nod:
    def __init__(self, value=None):
        self.valoare = value    # valoare reprezinta valoarea nodului
        self.next = None        # next reprezinta referinta catre urmatorul nod

class ListaSimpluInlantuita:
    def __init__(self):
        self.head = None        # head reprezinta 
        self.tail = None

    def __iter__(self):
        nod = self.head

        # expresie ca sa faci afisabila lista
        while nod:
            yield nod
            nod = nod.next 

    # inserare in lista inlantuita
    def insertSLL(self, value, location):

        # creezi un nou nod 
        nodNou = Nod(value)

        # verificam valoarea de Head daca e nula sau nu. Daca e nula, atunci nu avem elemente in lista
        if self.head == None:
            self.head = nodNou
            self.tail = nodNou

            # De ce amandoua? Pentru ca lista este goala initial. Si dupa ce adaugi un element, ala e si primul
            # si ultimul din lista.

        # verificam parametrul locatie. 
        else:
            if location == 0:
                # atunci adaugam la inceputul listei. 
                nodNou.next = self.head # salvam in next valoarea primului element de dinainte de adaugare
                self.head = nodNou # nodNou devine primul nod, deci referinta lui head va fi catre nod nou

            elif location == 1:
                # atunci adaugam la finalul listei
                nodNou.next = None
                
                # ca sa accesam ultimul element de dinainte de adaugare, folosim tailul. In tail.next este salvata
                # referinta catre ultimul nod.
                self.tail.next = nodNou # am adaugat referinta catre penultimul element
                self.tail = nodNou # am adaugat referinta catre noul element

            else:
                # adaugam dupa un nod anume
                tempNode = self.head # ca sa traversam trebuie sa incepem de la Head
                index = 0
                while index < location - 1 and tempNode != self.tail:
                    tempNode = tempNode.next # traverseaza din referinta in referinta
                    index += 1

                # introducem nodNou intre tempNode si nextNode si pasam referintele
                # consideram nextNode ca fiind tempNode.next
                nodNou.next = tempNode.next
                tempNode.next = nodNou
    
    def traversSLL(self):
        if self.head is None:
            # nu avem nimic
            print("NU")
        else:
            nod = self.head
            while nod is not None:
                print(nod.valoare)
                nod = nod.next

    def searchSLL(self, valoareNodCautat):
        if self.head is None:
            # nu avem nimic
            print("NU")
        else:
            nod = self.head
            index = 0
            gasit = 0
            while nod is not None and gasit == 0:
                if valoareNodCautat == nod.valoare:
                    print(index)
                    gasit = 1
                
                nod = nod.next
                index += 1
            
            if gasit == 0:
                print("nu am gasit ce vrei tu")

    def deleteSLL(self, location):
        if self.head is None:
            print("NU")
        else:
            if location == 0:
                # cazul 1: e la inceput

                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next

            elif location == 1:
                # cazul 2: e la final 
                if self.head == self.tail:
                    self.head = None
                    self.tail = None 
                
                else:
                    nod = self.head

                    while nod is not None:
                        if nod.next == self.tail:
                            break
                        nod = nod.next

                    nod.next = None
                    self.tail = nod
            
            else:
                index = 0
                tempNode = self.head

                while index < location - 1 and tempNode is not None:
                    tempNode = tempNode.next
                    index += 1

                nextNode = tempNode.next
                tempNode.next = nextNode.next
    
    def deleteEntireSLL(self):
        if self.head is None:
            print("Nu")
        else:
            self.head = None
            self.tail = None
                    
listaSIn = ListaSimpluInlantuita()
listaSIn.insertSLL(1, 0)
listaSIn.insertSLL(2, 1)
listaSIn.insertSLL(3, 1)
listaSIn.insertSLL(4, 1)
listaSIn.deleteSLL(2)
listaSIn.traversSLL()