f = open("27423.txt", "r")
f = f.read()

numbers = f.split('\n')
lenght = len(numbers)
numbers = list(map(int, numbers))

diskSize = numbers[0]
usersCount = numbers[1]
usedSpace = 0
numbers.pop(0)
numbers.pop(0) # тут удаляем первые два элемента
numbers.sort()
i = 0
while usedSpace < diskSize: # заполняем корзинку, останавливаемся, как только она переполняется
    usedSpace += numbers[i]
    i += 1
maxUser = 0
i -= 1
usedSpace -= numbers[i]
usedSpace -= numbers[i - 1] # делаем корректировку, убираем лишние бананы
freeSpace = diskSize - usedSpace # получаем свободное пространство
for j in range(0, lenght):
    if numbers[j] > freeSpace: # смотрим, что можно засунуть еще
        maxUser = numbers[j - 1]
        break
print(i, maxUser) # выводим ответ