
file = open("37350.txt", "r") # напоминаю, что такой путь к файл у работает только если файл лежит в одной папке с твоим скриптом
f = file.read()
temp = f.split("\n")
numbers = list(map(int, temp)) # map к каждому элементу коллекции применяет функцию
lenght = len(numbers)
counter = 0
maxSum = 0

for i in range(0, lenght - 1):
    for j in range(i + 1, lenght):
        if (numbers[i] + numbers[j]) % 2 == 1 and (numbers[i] * numbers[j]) % 3 == 0: # работаем с парой, если сумма элементов нечетна и их произведение делится на 3 (по условию)
            counter += 1
            maxSum = max(maxSum, numbers[i] + numbers[j]) # дальше все стандартно
print(counter, maxSum)



















# file = open("/Users/artemparfenov/Downloads/40733.txt", "r") # Открываем файл
# f = file.read() # Считываем данные из файла
# numbers = f.split("\n") # Убираем из нашей строки символ \n и разделяем по нему нашу строку
#
# lenght = len(numbers) # Получаем длину нашего массива с числами
# sum = 0
# count = 0
#
# for i in range(0, lenght - 1):
#     if int(numbers[i]) % 2 == 0:
#         sum += int(numbers[i])
#         count += 1
# average = sum / count # до сюда считаем среденее, думаю, тут понятно все
# # Заводим переменные - счетчики
# countOfPair = 0 # Количество пар
# currentMaxSum = 0 # Текущая максимальная сумма
#
# for i in range(0, lenght - 2): #Пробегаемся по массиву, можешь на пошаговой отладке посмотреть, почему именно до lenght -2 нужно рассматривать
#     if int(numbers[i]) % 3 == 0: # Если первое число из нашей пары нас устраивает, то идем дальше
#         if int(numbers[i]) < average:# Если первое число снова нас устраивает, то берем эту пару
#             countOfPair += 1
#             currentMaxSum = max(currentMaxSum, int(numbers[i]) + int(numbers[i + 1]))
#         elif int(numbers[i + 1]) < average: # Если второе число нас устраивает, то берем эту пару
#             countOfPair += 1
#             currentMaxSum = max(currentMaxSum, int(numbers[i]) + int(numbers[i + 1]))
#     elif int(numbers[i + 1]) % 3 == 0: # Если первое число нас не устроило, то смотрим на второе
#         if int(numbers[i]) < average: # Если первое число нас устраивает, то берем эту пару
#             countOfPair += 1
#             icurrentMaxSum = max(currentMaxSum, int(numbers[i]) + int(numbers[i + 1]))
#         elif int(numbers[i + 1]) < average: # Если второе число снова нас устроило, то берем эту пару
#             countOfPair += 1
#             currentMaxSum = max(currentMaxSum, int(numbers[i]) + int(numbers[i + 1]))
#
# print(countOfPair)
# print(currentMaxSum) # Выводим ответы)
#
# # Правильные ответы: 2288, 14875