
f = open("36000.txt")
file = f.read()
numbers = file.split("\n")
numbers = list(map(int, numbers))
lenght = numbers[0]
numbers.pop(0)

maxSum = 0
count = 0


def find(number, array):
    for element in array:
        if element == number:
            return True
    return False


for i in range(0, lenght - 1):
    print(i, end = '')
    for j in range(i + 1, lenght):
        if (numbers[i] % 2 == 0 and numbers[j] % 2 == 1) or (numbers[i] % 2 == 1 and numbers[j] % 2 == 0):
            pairSum = numbers[i] + numbers[j]
            if find(pairSum, numbers):
                count += 1
                maxSum = max(maxSum, pairSum)

print(maxSum, count)