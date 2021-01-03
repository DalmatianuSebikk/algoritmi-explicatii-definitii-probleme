# DICTIONARUL - O colectie care nu are ordine, care este schimbabila si indexata.
# Orice valoare poate fi identificata daca ii stim cheia (indexul)

dictionar = {'cuvant': 'definitie'} # cuvant este cheia, definitia este valoarea

# CUM CREEZI UN DICTIONAR?
    # - fie folosesti dict  dictionar = dict()
    # - fie declari in acolade {}   dictionar = {}, dictionar = {'1': 'unu', '2':'doi'}

# Cum accesezi elemente din dictionar?
    # - dictionar[cheie]

# Dictionarele in python sunt implementate prin intermediul hash-tables
# Hash-table reprezinta o modalitate de a cauta ceva prin intermediul unui key-value lookup. 
# Pui ceva in vector, apoi folosesti o functie de hash pentru a gasi indexul celulei din vector care corespunde
# cu perechea ta key-value

# OBS: functia de hash ar trebui sa evite cazurile in care se gaseste acelasi index pentru 2 perechi key-value.

# Pentru schimbarea valorii unui element din dictionar: dictionar[cheie] = alta_valoare

# Ca sa adaugi un element in dictionar: Efectiv declari o valoare cheii chiar daca nu exista:
#   - dicionar[cheie_care_exista_sau_nu] = valoare

# Cum traversezi un dictionar?
#   - cu un for: for cheie in dictionar print(cheie, dictionar[cheie])

# Cautarea unui element in dictionar:
#   - cautarea liniara: un for cheie in dictionar if dictionar[cheie] == ceCautEu: print('gasit') break

# Stergerea unui element din dictionar: 
#   - poti folosi pop(): dictionar.pop(cheie) (IN ACELASI TIMP METODA RETURNEAZA CE AI STERS DACA DAI PRINT)
#   - popitem(): scoate un element random din dictionar
#   - clear(): sterge toate elementele din dictionar
#   - del: sterge un element din dictionar: del dictionar[cheie] 

# Metode pt dictionare in Python:
#   - clear(): sterge toate elementele din dictionar 
#   - copy(): copiaza un dictionar
#   - fromkeys(chei, valoare): te ajuta in momentul in care vrei sa atribui aceeasi valoare mai multor chei
#   - get(cheie, valoare): primesti din dictionar tupla cheie valoare (parametrul valoare e optional)
#   - items(): returneaza un obiect care afiseaza o lista de tuple care sunt elemente cheie-valoare din dict.
#   - keys(): afiseaza cheile din dictionar
#   - popitem(): returneaza si sterge un element arbitrat din dictionar (il returneaza ca tuplu)
#   - setdefault(cheie, val_default): returneaza valoarea cheii daca cheia e in dictionarl, iar daca nu, o adauga cu val_default
#   - pop(cheie, valoare_default)
#   - values(): returneaza o lista cu valorile cheilor din dictionar
#   - update(alt_dictionar): adauga elemente apartinand altui dictionar sau face update la valori daca cheia exista

# BUILT IN FUNCTIONS care functioneaza cu dictionare (si nu numai):
#   - in: verifica daca un element e in dictionar: if valoare in dictionar: print('DA')
#   - for: e structura repetitiva
#   - all(dictionar): daca toate valorile sunt True (sau e goala lista) returneaza True, altfel False 
#   - any(dictionar): daca exista macar o valoare True (sau nu e goala lista si ai un True) returneaza True, altfel False
#   - len(dictionar): lungimea dictionarului
#   - sorted(dictionar): returneaza dictionarul sortat

# DIFERENTE DINTRE DICTIONAR SI LISTA:

#   DICTIONAR           |           lISTA
#   neordonata          |           Ordonata

#   accesare cu chei    |           accesare cu index

#   Colectie chei-valori|           colectie de elemente

#   Preferabil cand ai  |           Preferabil cand ai 
#  chei cu valoare unica|           elemente sortate

#   Fara elemente duplicate |        Accepta elemente duplicate

