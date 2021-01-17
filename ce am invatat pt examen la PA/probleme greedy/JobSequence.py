"""
Avem o lista de joburi, fiecare job are un deadline si un profi asociat jobului daca jobul este terminat
inainte de deadline. Fiecare job ia o singura unitate de timp, deci deadline ul minim posibil pentru orice job
este 1. Cum sa maximizezi profitul daca un singur job poate fi programat la un timp anume?

Input: Four Jobs with following 
deadlines and profits
JobID  Deadline  Profit
  a      4        20   
  b      1        10
  c      1        40  
  d      1        30
Output: Following is maximum 
profit sequence of jobs
        c, a   


Input:  Five Jobs with following
deadlines and profits
JobID   Deadline  Profit
  a       2        100
  b       1        19
  c       2        27
  d       1        25
  e       3        15
Output: Following is maximum 
profit sequence of jobs
        c, a, e


Idee:
1. sortezi joburile dupa pret descrescator
2. mergi prin joburi in ordine descrescatoare a profitului.
    - gasesti un loc liber pt timp i, astfel incat timpul sa fie gol si i < deadline
    - pui jobul in loc si marchezi ca fiind umplut
    - daca nu exista niciun i, ignori
"""

arr = [['a', 2, 100],  # Job Array 
       ['b', 1, 19], 
       ['c', 2, 27], 
       ['d', 1, 25], 
       ['e', 3, 15]]

def jobSchedule(arr, t):
    # lungimea vectorului
    n = len(arr)

    # sortezi descrescator dpdv al protifului
    def pt_sort(arr):
        return arr[2]
    arr = sorted(arr, key=pt_sort, reverse=True)

    timp = [False] * t # lista pentru care vedem daca am ocupat toate deadline urile
    joburi = ['-1'] * t # secventa de joburi

    # mergem prin fiecare job dat:
    for i in range(len(arr)):
        # gasim un loc liber pentru job
        # pornim de la ultimul loc posibil
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            # am gasit un loc liber:
            if timp[j] == False:
                timp[j] = True
                joburi[j] = arr[i][0]
                break 

    print(joburi)



jobSchedule(arr, 3)