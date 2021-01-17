"""
Consideram n activitati cu timpurile de incepere si de terminare. Trebuie sa alegi numarul maxim de activitati
care pot fi facute de o singura persoana, asumand faptul ca persoana poate face doar o singura activitate 
o data.

Exemplu: Consideram 3 activitati ale caror start si finish il stim:
start  =  {10, 12, 20};
finish =  {20, 25, 30};

Omul respectiv poate sa faca doar 2 activitati, adica cea de la 10 la 20 si de la 20 la 30. Nu poate face
12 25 pentru ca se suprapune

Alt exemplu:

activitatile sunt sortate dupa ordinea de terminare
start[]  =  {1, 3, 0, 5, 8, 5};
finish[] =  {2, 4, 6, 7, 9, 9};

Omul respectiv poate face doar 4 activitati, adica cea de la 1 la 2, de la 3 la 4, de la 5 la 7, de la 8 la 9

"""

start = [5, 8, 5, 1, 3, 0]
finish = [7, 9, 9, 2, 4, 6]

lista_tuple_activitati = []

for i in range(len(start)):
    lista_tuple_activitati.append((start[i], finish[i]))

# sortam dupa timpul de terminare
def pentru_sortare_tuplu(t):
    return t[1], t[0]

lista_tuple_activitati = sorted(lista_tuple_activitati, key=pentru_sortare_tuplu)

max = 0
nr_activitati = 0 # presupunem ca nu face niciuna, lenes

for tupla in lista_tuple_activitati:
    if max == 0:
        max = tupla[1] # prima activitate pe care o face
        print(tupla)
        nr_activitati = 1
    else:
        if tupla[0] < max:
            # nu e ok, se suprapune
            pass
        else:
            print(tupla)
            nr_activitati += 1
            max = tupla[1]

print(nr_activitati)



