A = []

liste = []

for i in range(len(A)):
    liste.append((A[i].start, 0))

for i in range(len(A)):
    liste.append((A[i].finish, 1))

liste.sort()

count = 0
max = 0

for i in range(len(liste)):
    if liste[i][1] == 0:
        count += 1
        if count > max:
            max = count
    else:
        count -= 1