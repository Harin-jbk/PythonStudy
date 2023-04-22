list = []

for i in range(174457, 174506):
    for j in range(1, i + 1):
        if i % j == 0 and j != 1 and j != i:
            list.append(j)
    if len(list) == 2:
        print(list[0], list[1])
    list.clear()