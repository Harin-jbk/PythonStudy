dictionary = dict()
counter = 0
numbers = 0
maxNumber = 0
for i in range(120115, 120201):
    for j in range(1, i + 1):
        if i % j == 0:
            counter += 1 # если число является делителем, то увеличиваем счетчик делителей
    dictionary[counter] = i # кладем в словарь пару "количество делителей - число, у которого есть эти делители"
    maxNumber = max(maxNumber, counter) # запоминаем максимальное значение количества делителей
    counter = 0 # обнуляем количество делителей у текущего числа
print(maxNumber, dictionary[maxNumber])
