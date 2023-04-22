from tqdm import tqdm
f = open("input.txt")
file = f.read()
numbers = file.split("\n")
# numbers = list(map(int, numbers))
lenght = int(numbers[0])
numbers.pop(0)


array = []

for i in tqdm(range(0, 201)):
    temp = []
    for j in range(0, 201):
        temp.append(0)
    array.append(temp)

for i in range(0, lenght, 2):
    string = numbers[i]
    string = string.split(" ")
    array[int(string[0])][int(string[1]) - 1] = 1

indexes = []
for i in range(0, 201):
    indexes.append(i)
indexes.reverse()
currentFreeSpace = 0
for i in indexes:
    for j in range(0, 201):
        if array[i][j] == 0:
            currentFreeSpace += 1
        if currentFreeSpace == 13 and array[i][j + 1] == 1:
            print(i, j)
        elif array[i][j] == 1:
            currentFreeSpace = 0