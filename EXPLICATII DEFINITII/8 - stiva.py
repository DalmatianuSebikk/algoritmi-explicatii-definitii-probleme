# STIVA - e o structura care stocheaza elementele "pe verticala"/ Last-In-First-Out, adica ultimul adaugat in
# stiva este primul care este scos din stiva

# CAND AVEM NEVOIE DE O STIVA?
# Avem nevoie de o stiva atunci cand trebuie ca ultimele date introduse sa fie folosite primele.

# OPERATII STIVA
#   - creeaza stiva -> creezi obiectul de tip stiva
#   - push  -> adaugi un element in stiva
#   - pop   -> stergi un element in stiva
#   - peek  -> returneaza varful stivei
#   - isEmpty   -> returneaza daca e goala lista sau nu 
#   - isFull    -> returneaza daca e umpluta sau nu
#   - delete   -> stergi tot ce e in stiva


# IMPLEMENTAREA STIVEI CU LISTE FARA LIMITA DE MARIME

"""
class Stiva:
    # creeaza stiva
    def __init__(self):
        self.list = []
    
    # afisajul sub forma de lista
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    # isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self, value):
        self.list.append(value)
    
    def pop(self):
        if self.isEmpty():
            return "NU"
        else:
            self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "NU"
        else:
            return self.list[len(self.list) - 1]

    def delete(self):
        self.list = None



customStack = Stiva()

customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.pop()
print(customStack.peek())
print(customStack)
"""

# UTILIZAREA UNEI STIVE CU UN NUMAR LIMITAT ELEMENTE

"""
class Stiva:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []
    
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    # isempty
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # isFull
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
    
    # push
    def push(self, element):
        if self.isFull():
            return "NU"
        else:
            self.list.append(element)
    
    # pop
    def pop(self):
        if self.isEmpty():
            return "NU"
        else:
            self.list.pop()

    # peek
    def peek(self):
        return self.list[maxSize - 1]
    
    # delete
    def delete(self):
        self.list = None
"""

# CAND SA FOLOSESTI SI CAND SA NU FOLOSESTI STIVA:

#   Da:
#   - cand vrei functionalitate LIFO
#   - sansa sa se corupa datele este minima

#   Nu:
#   - Random access nu este posibil

