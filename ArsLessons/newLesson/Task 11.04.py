file = open("33198.txt")
a = []
w = 0
count = 0
for i in file:
    if 199 < int(i) < 211:
        w += int(i)
        count += 1
    else:
        a.append(int(i))
a.sort()
aa = []
i = 0
while sum(ss) + s[i] <= int(b) - w:
    count += 1
    aa.append(a[i])
    i += 1
k = len(a) - 1
while i > 0:
    while k >= 0:
        if sum(aa) - aa[i-1] + a[k] <= int(b) - w and a[k] != 0:
            aa[i-1] = a[k]
            a[k] = 0
            i -= 1
            break
        else:
            k -= 1
w += sum(aa)
print(count, w)