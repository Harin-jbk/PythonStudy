file = open("26 (2).txt")
f = file.read().split()
countOfProducts = int(f[0])
capacity = int(f[1])
f.pop(0)
f.pop(0)
a = []
w = 0
count = 0
for i in f:
    if 199 < int(i) < 211:
        w += int(i)
        count += 1
    else:
        a.append(int(i))
a2 = 0
i = 0
a.sort()
last = 0
while a2 + a[i] <= capacity - w:
    count += 1
    a2 += a[i]
    i += 1
    last = a[i]
a2 -= last
freeSpace = capacity - (a2 + w)
for j in range(0, len(a)):
    if a[j] > freeSpace:
        a2 += a[j - 1]
        break
print(count, a2 + w)
