file = open("37350.txt", "r")
f = file.read()
numbers = f.split("\n")

lenght = len(numbers)
numbers = list(map(int, numbers))
count = 0
maxCont = 0

for i in range(0, lenght - 1):
    for j in range(i + 1, lenght):
        if ((numbers[i] - numbers[j]) % 2 == 0) and ((numbers[i] % 31 == 0) or (numbers[j] % 31 == 0)):
            count += 1
            maxCont = max(maxCont, numbers[i] + numbers[j])
print(maxCont, count)
