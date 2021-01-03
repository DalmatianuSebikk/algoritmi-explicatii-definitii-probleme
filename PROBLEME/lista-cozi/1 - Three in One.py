# Se da o lista, foloseste-o ca sa implementezi 3 stive

# Lista se poate imparti in 3 parti, astfel se pot forma 3 stive
# stiva 1 contine elementele de la 

lista = [1,2,3,4,5,6,7,8,9]
stiva1 = []
stiva2 = []
stiva3 = []

n = len(lista)

for x in range(n // 3):
    stiva1.append(lista[x])

for x in range(n // 3 , (2 * n) // 3):
    stiva2.append(lista[x])

for x in range((2*n) // 3, n):
    stiva3.append(lista[x])

print(stiva1)
print(stiva2)
print(stiva3)