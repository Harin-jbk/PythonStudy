f = open("35915.txt", "r")
file = f.read()
numbers = file.split()
lenght = len(numbers) - 1
maxAverage = 0
pairsCounter = 0

def myFind(numbers, average): # функция определения наличия элемента в последовательности
    for i in range(1, len(numbers)):
        if numbers[i] == average:
            return True
    return False

for i in range(1, lenght - 1):
    if int(numbers[i]) % 2 == 1: # если первый элемент в паре - нечетный
        for j in range(i + 1, lenght):
            if int(numbers[j]) % 2 == 1: # если второй элемент в паре - нечетный
                pairsCounter += 1 # если ооба элемента - нечетные, то мы нашли нужную пару, учитываем ее
                average = (int(numbers[i]) + int(numbers[j]) % 2) / 2 # считаем среднее арифметическое пары
                if myFind(numbers, average): # если среднее арифметическое есть в послежовательности
                    maxAverage = max(maxAverage, average) # обновим счетчик максимального значения среднего
        print(i) # для понимания скорости работы программы
print(pairsCounter, maxAverage)