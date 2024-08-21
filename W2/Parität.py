list = [12, 34, 45, 9, 8, 90, 3]

offset = 0
for i in range(len(list)):
    if list[i+offset] % 2 != 0:
        list.append(list[i+offset])
        list.pop(i+offset)
        offset -= 1



print(list)