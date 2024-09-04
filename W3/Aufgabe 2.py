ar1 = [2, 3, 3, 5, 5, 6, 7, 7, 8, 12, 20, 20]
ar2 = [5, 5, 6, 8, 8, 9, 10, 20]

ausgabe = []

for i in range(len(ar1)):
    if ar1[i] in ar2:
        if ar1[i] not in ausgabe:
            ausgabe.append(ar1[i])

print(ausgabe)