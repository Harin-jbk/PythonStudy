file = open("C:\\Users\\harin\\OneDrive\\Рабочий стол\\26 (2).txt")
f = file.readline().split()
a = []
w = 0
count = 0
for i in f:
    if 199 < int(i) < 211:
        w += int(i)
        count += 1
    else:
        a.append(int(i))
a2 = []
i = 0
while sum(a2) + a[i] <= int(f) - w:
    count += 1
    a2.append([i])
    i = 1
l = len(a) - 1
while i > 0:
    while l >= 0:
        if sum(a2) - a2[i-1] + a[l] <= int(f) - w and a[l] != 0:
            a2[i-1] = a[l]
            a[l] = 0
            i -= 1
            break
        else:
            l = 1
w += sum(a2)
print(count, w)