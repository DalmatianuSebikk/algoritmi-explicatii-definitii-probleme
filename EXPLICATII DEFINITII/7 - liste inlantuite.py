# LISTA INLANTUITA - este o forma de colectie secventiala (care nu trebuie sa aiba neaparat o ordine)
# O lista inlantuita contine noduri independente care ar putea contine orice tip de date si fiecare nod
# are o referinta catre urmatorul nod.

# Lista inlantuita poate fi asociata cu un tren, pentru ca exact ca in lista inlantuita, vagoanele
# si locomotiva (in acest caz vagoanele si locosunt legate intre ele (idk cum se cheama chestia aia);
# Tot in acest caz, locomotiva este "capul" (head-ul), iar ultimul vagon este "coada" (tail). 
# Fiecare vagon este independent.
# Singura chestie la tren care nu respecta lista inlantuita este faptul ca in memorie nodurile nu sunt unele
# langa altele

# Head-ul este important intr-o lista inlantuita pentru a sti de unde incepe lista si cum ajungi intr-un anume nod
# Tail-ul este necesar pentru ca altfel pentru a ajunge in ultimul element ar trebui sa parcurgi toata lista

# OBSERVATIE: HEAD SI TAIL SUNT POINTERI, SALVEAZA REFERINTELE CATRE PRIMUL SI ULTIMUL NOD!!!!!!

# LISTE INLANTUITE VS VECTORI:
#   -   Elementele unei liste inlantuite sunt obiecte independente, in timp ce in vector nu sunt obiecte separate
#   -   Dimenstiunea variabila: in cazul listei inlantuite, nu definim marimea atunci cand cream lista, ci doar
#       marim sau scadem numarul de noduri
#   -   Adaugarea si stergerea elementelor este mult mai eficienta la liste
#   -   In vectori este mai eficienta cautarea/accesarea elementelor pentru ca sunt indexate. 
#       In timp ce la listele inlantuite, trebuie sa trecem prin toate nodurile

# TIPURI DE LISTE:
#   lista simplu-inlantuita
#   lista circulara simplu-inlantuita
#   lista dublu-inlantuita
#   lista circulara dublu-inlantuita

# LISTA SIMPLU-INLANTUITA: Fiecare nod din lista stocheaza valoarea si referinta urmatorului nod din lista.
#                          Nu are nicio referinta fata de nodul anterior, fiecare nod are 2 parti:
#                          Valoarea stocata si referinta catre urmatorul nod

# LISTA CIRCULARA SIMPLU-INLANTUITA: La fel ca la lista simplu-inlantuita, dar ultimul nod salveaza 
#                          Referinta primului nod, si avem optiunea de a merge inapoi la el

# LISTA DUBLU-INLANTUITA: Fiecare nod are doua referinte, catre cel din fata si catre cel din spate (poti sa 
#                           te gandesti la un player de muzica, butonul de inainte te duce la alt element din
#                           lista de melodii, iar butonul de inapoi la melodia anterioara)

# LISTA CIRCULARA DUBLU-INLANTUITA: La fel ca la lista circulara simplu-inlantuita, exista o legatura intre primul 
#                           si ultimul nod, dar de data asta e dubla (adica poti ai si invers)
#                           - poti sa asociezi asta cu alt-shift ul din windows, care traverseaza lista de aplicatii deschise.
#                           iar cand folosesti sagetile traversezi in ce directie vrei tu iar cand ajungi la final
#                           o ia de la un capat opus


# CUM SUNT STOCATE IN MEMORIE?
#   La array-uri, elementele din vector sunt stocate in memorie unul langa altul
#   La listele inlantuite, elementele nu sunt stocate unul langa altul, ci mai mult la intamplare, si elementele
#   sunt legate intre ele prin intermediul referintei de memorie. In listele inlantuite, fiecare nod are nevoie de
#   niste memorie extra pentru pointerii care retin adresa de memorie. 

#   Din cauza ca nu stim care este pozitia elementului, trebuie sa traversam element cu element lista, ceea ce
#   este un punct slab la liste.

# --------------------------------------------------------------------------------------------------

# CREAREA UNEI LISTE SIMPLU INLANTUITE (Pasi):
#       1. Creezi Head si Tail (pentru primul si ultimul nod) si le initializezi cu NULL
#       2. Creezi un nod gol si ii dai o valoare, iar referinta o faci nula (pentru ca e primul nod si nu mai exista altu)
#       3. Legi Head si Tail de nod 

"""
class Nod:
    def __init__(self, value=None):
        self.valoare = value
        self.next = None

class ListaSimpluInlantuita:
    def __init__(self):
        self.head = None
        self.tail = None

listaSIn = ListaSimpluInlantuita()
nod1 = Nod(1)
nod2 = Nod(2)

listaSIn.head = nod1
listaSIn.head.next = nod2
listaSIn.tail = nod2
"""

# Am creat o lista simplu inlantuita cu un element. Complexitatea este O(1) si ca timp si ca spatiu.


# INSERAREA UNUI ELEMENT IN LISTA SIMPLU INLANTUITA:
# 1. inserarea unui element la inceputul listei
# 2. inserarea unui element la mijloc
# 3. inserarea unui element la final

# 1. inserarea unui element la inceputul listei:
#       - alocam o memorie random in Heap pentru noul nod
#       - pasam noului nod introdus adresa primului nod din prezent
#       - mutam adresa Head-ului, sa fie pe nodul adaugat

# 2. inserarea unui element la mijlocul listei (sau dupa un nod anume)
#       - parcurgem lista pana cand ajungem la locul unde vrem sa adaugam in lista, si modificam referintele.
#       - nodul precedent va avea adresa nodului adaugat acum, iar nodul adaugat va avea adresa urmatorului.

# 3. inserarea la final al unui element in lista 
#       - parcurgi pana la final lista si aloci dinamic in memorie elementul pe care vrei sa l adaugi
#       - legam referinta de penultimul nod.

"""
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
"""


# TRAVERSAREA LISTEI SIMPLU INLANTUITE

"""
def traversSLL(self):
        if self.head is None:
            # nu avem nimic
            print("NU")
        else:
            nod = self.head
            while nod is not None:
                print(nod.valoare)
                nod = nod.next
"""
# Daca head nu este nul, atunci exista valori in lista inlantuita. Trecem din valoare in valoare pana nu ajungem
# la NULL si afisam valoarea nodului


# CAUTAREA UNUI ELEMENT

"""
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
"""
# STERGEREA UNUI ELEMENT DIN LISTA SIMPLU INLANTUITA

"""
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
"""

# STERGEREA INTREGII LISTE

# Garbage collectorul in acest caz te ajuta foarte mult, adica daca tailul si head-ul le atribui Null, el inlatura
# toata lista

# CREAREA LISTELOR SIMPLU CIRCULAR INLANTUITE:

# Vom crea capul si coada, cream nodul gol si ii vom trimite referinta catre el insusi

"""
def createCSLL(self, valoareNod):

        nod = Nod(valoareNod)
        nod.next = nod           # adaugam referinta catre el insusi
        self.head = nod
        self.tail = nod
"""

