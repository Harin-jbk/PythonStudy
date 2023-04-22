file = open("37344.txt", "r")
f = file.read()
numbers = f.split("\n")

lenght = len(numbers)

pairsCounter = 0
maxSum = 0

for i in range(0, lenght - 1):
    for j in range(i + 1, lenght):
        if int(numbers[j]) * int(numbers[i]) % 10 == 0:
            pairsCounter += 1
            maxSum = max(maxSum, int(numbers[i]) + int(numbers[j]))

print(pairsCounter)
print(maxSum)