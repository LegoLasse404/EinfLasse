events = [("event1", (1, 3)), ("event2", (2, 4)), ("event3", (2, 5)), ("event4", (6, 7))]

highest = 0


for i in range(len(events)):
    x = 0
    for j in range(len(events)):
        if i == j:
            continue
        if events[i][1][1] > events[j][1][0] and events[i][1][1] < events[j][1][1]:
            if x == 0:
                x = 2
            else:
                x = x + 1
            if x > highest:
                highest = x

print(highest)