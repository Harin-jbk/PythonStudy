file = open("27883.txt")
f = file.readlines()
countOfUser = int(f[0])
freePlace = int(f[0])
s = 543
f.pop(0)
f.pop(0)
f = sorted(f)
q = 0
for count in range(0, len(f)):
    if q + count > s:
        break
    q += f[count]
