

dels = []
maxDelsList = []
maxDivisible = 0
for i in range(120115, 121251):
    dels = []
    for j in range(1, i + 1):
        if i % j == 0:
            dels.append(j)
    if len(dels) > len(maxDelsList):
        maxDelsList = dels
        maxDivisible = i
print(len(maxDelsList), maxDelsList, maxDivisible)