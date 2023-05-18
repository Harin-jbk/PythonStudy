file = open("27883.txt")
f = file.readlines()
e = f[0].split()
e = int(e[0])
f.pop(0)
s = 543
f = sorted(f)
q = 0
for count in range(0, len(f)):
    if q + f[count] > s:
        break
    q += f[count]
ost = e - q
for p in range(0, len(f)):
    if f[p] - f[count - 1] <= ost:
        ands = f[p]
print(count, ands)

