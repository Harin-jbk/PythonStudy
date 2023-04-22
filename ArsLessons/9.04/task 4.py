for i in range(185311, 185331):
    delit = []
    for j in range(1, int(i**0.5) + 1):
        if i % j == 0:
            delit.append(j)
            if i//j != j:
                delit.append(i//j)
    if len(delit) == 4:
        delit.sort()
        print(delit[0],delit[1],delit[2],delit[3])