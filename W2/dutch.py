liste = [0,1,2,0,1,2,0]

offset = 0

print(liste)

for i in range(len(liste)):
    if liste[i+offset] == 2:
        liste.append(liste[i+offset])
        liste.pop(i+offset)
        offset -= 1
        print("2:", liste)
    if liste[i+offset] == 0:
        liste.insert( 0, liste[i+offset])
        offset += 1
        liste.pop(i+offset)
        print("0:", liste)
    else:
        print("1:", liste)
print(liste)