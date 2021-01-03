class Nod:
    def __init__(self, value=None):

        self.valoare = value    # valoarea nodului
        self.next = None        # referinta

class CircularSingledLinkList:
    def __init__(self):

        self.head = None
        self.tail = None

    def __iter__(self):

        nod = self.head
        while nod:
            yield nod
            if nod.next == self.head:
                break            # pentru ca e circulara, si daca ajungem din nou la head inseamna ca am parcurs tot

            nod = nod.next
    
    # Crearea listei circulare simplu inlantuite
    def createCSLL(self, valoareNod):

        nod = Nod(valoareNod)
        nod.next = nod           # adaugam referinta catre el insusi
        self.head = nod
        self.tail = nod
    
    def insertCSLL(self, valoareNod, locatie):

        nod = Nod(valoareNod)
        
        if locatie == 0:
            # cazul 1, e la inceput
            if self.head is None:
                nod.next = nod
                self.head = nod
                self.tail = nod
            else:
                nod.next = self.head
                self.head = nod
                self.tail.next = nod

        elif locatie == 1:
            # cazul 2, e la final
            if self.head is None:
                nod.next = nod
                self.head = nod
                self.tail = nod
            else:
                nod.next = self.head
                self.tail.next = nod
                self.tail = nod
        
        else:
            # cazul 3, e intre 2 noduri

            index = 0
            tempNod = self.head

            while index < locatie - 1 and tempNod is not None:
                tempNod = tempNod.next
                index += 1
            
            nod.next = tempNod.next
            tempNod.next = nod
    
    def traverseCSLL(self):
        nod = self.head
        while nod.next != self.head:
            print(nod.valoare)
            nod = nod.next 
        print(nod.valoare)

    def searchCSLL(self, nod):
        nodCautat = Nod(nod)
        tempNode = self.head
        index = 0
        gasit = 0

        while tempNode.next != self.head:
            if nodCautat.valoare == tempNode.valoare:
                print("l-am gasit pe indexul:" + str(index))
                gasit = 1
                break
            tempNode = tempNode.next
            index += 1

        if nodCautat.valoare == tempNode.valoare and gasit != 1:
            print("l-am gasit pe indexul:" + str(index))
            gasit = 1

        else:
            if gasit == 0:
                print("N-am gasit nimic man")
    
    def deleteCSLL(self, locatie):
        if self.head is None:
            print("NU")
        else:
            if locatie == 0:
                # cazul 1, e la inceput
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            
            elif locatie == 1:
                # cazul 2, e la final
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                
                else:
                    tempNode = self.head

                    while tempNode.next != self.tail:
                        tempNode = tempNode.next
                    
                    tempNode.next = self.head
                    self.tail = tempNode
            
            else:
                index = 0
                tempNode = self.head

                while index < locatie - 1:
                    tempNode = tempNode.next
                    index += 1
                
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def deleteEntireCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None

    



circularSLL = CircularSingledLinkList()
circularSLL.createCSLL(1)
circularSLL.insertCSLL(0, 0)
circularSLL.insertCSLL(2, 1)
circularSLL.insertCSLL(3, 2)
circularSLL.deleteCSLL(3)
circularSLL.traverseCSLL()
    
