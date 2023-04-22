file = open("27883.txt", "r")
num = list()
for i in file:
    a = i.split()
    b = i.split()
    a = int(a)
    b = int(b)
    num.append([a, -b])
num.sort()
k = 0
l = 0
for i in range(1, num - 1):
    if num[i][0] == num[i - 1][0]:
        if num[i][1] - num[i - 1][1] == 14:
            k = num[i][0]
            l = -num[i][1] + 1
print(k, l)