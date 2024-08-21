list = [6, 34, 4, 12, 5, 2]
summenliste = []

def summenproblem(n):
    for i in list:
        if i > n:
            list.remove(i)

    while sum(summenliste) != n:
        for i in range(len(list)):
            summenliste.append(list[i])
            if sum(summenliste) == n:
                print(True)
                break
            if sum(summenliste) > n:
                summenliste.pop()
        list.pop(0)
        summenliste.clear()

summenproblem(9)