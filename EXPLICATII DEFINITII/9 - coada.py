# COADA - structura de date ce stocheaza elementele First-In-First-Out (primul venit, primul servit)
# Adaugarea se face la finalul cozii

# OPERATIILE COZII
#   - creeaza lista
#   - enqueue -> adauga elemente in coada
#   - dequeue -> sterge primul element din lista
#   - Peek -> primul element din coada (varful cozii)
#   - isEmpty -> verifica daca e goala
#   - isFull -> verifica daca e full
#   - delete -> sterge coada

# no size limit:

class Coada:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self, valoare):
        self.items.append(valoare)
    
    def dequeue(self):
        if self.isEmpty():
            return "NU"
        else:
            self.items.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "NU"
        else:
            return self.items[0]
    
    def delete(self):
        self.items = None