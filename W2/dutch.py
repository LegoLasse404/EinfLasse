liste = [0,1,2,0,1,2,0]

offset = 0

print(liste)
print(liste)
for i in range(len(liste)):
    if liste[i+offset] == 2:
        liste.append(liste[i+offset])
        print(liste)
        liste.pop(i+offset)
        offset -= 1
    elif liste[i+offset] == 0:
        liste.insert( 0, liste[i+offset])
        print(liste)
        liste.pop(i+offset)
        offset += 1

print(liste)