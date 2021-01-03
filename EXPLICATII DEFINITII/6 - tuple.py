# TUPLE - secventa de valori (obiecte Python)
# valorile pot fi comparabile si hash-uibile (valorile raman aceleasi)

# DECLARARE:

t = 1,2,3,4
# SAU
tupla = (1,2,3,4) #recomandat
tupla = tuple('string') # => (s,t,r,i,n,g)

# Tuplele sunt imutabile, o data ce le declari, asa raman, nu mai poti sa le modifici

# Accesarea elementelor: tuplu[index_element] SAU faci slice(functioneaza ca la lista)
# Traversarea unei tuple: cu un for
# Cautarea elementelor: cu operatorul "in" de exemplu, sau cautare liniara


# OPERATII PENTRU TUPLE:
#   -   Repetarea elementelor din tuplu (cu operatorul *)
#   -   Concatenarea a doua tuple   (cu operatorul +)
#   -   Cautarea unui element (cu in)

# METODELE PENTRU TUPLE:
#   -   .count(element_din_tuplu) -> repetitia elementului in tuplu 
#   -   .index(element_din_tuplu) -> indexul unui element din tuplu

# FUNCTII:
#   -   len(tuplu)
#   -   max(tuplu)
#   -   min(tuplu)
#   -   tuple(lista) -> converteste lista in tuplu 

# TUPLU VS LISTA
#   -   tuplul este imutabil / lista poate fi modificata
#   -   tuplele pot fi stocate in liste si vice-versa
#   -   si tuplele si listele sunt nested (poti face tuplu in tuplu si lista in lista)

# In general se folosesc tuplele pentru date heterogene si listele pentru date omogene
# Iterarea prin tuplu e mai rapida decat in lista
# Tuplele care contin elemente imutabile pot fi folosite ca pe o cheie pentru un dictionar

