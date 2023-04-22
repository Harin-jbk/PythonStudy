dels = []
for i in range(312614, 312652):
    dels = []
    for j in range(1, i + 1):
        if i % j == 0:
            dels.append(j)
        if len(dels) > 6:
            break
    if len(dels) == 6:
        print (dels[0], dels[1], dels[2], dels[3], dels[4], dels[5])