counter = 0
file = open("37336.txt")
numbers = [int(i) for i in file]
lenght = len(numbers)
maxpars = -20001
for i in range(len(numbers) - 1):
    if (numbers[i] % 3 == 0) or (numbers[i + 1] % 3 == 0):
        counter += 1
        maxpars = max(maxpars, numbers[i]+ numbers[i + 1])
print(counter, maxpars)