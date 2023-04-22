f = open("36037.txt", "r")
letters = f.read()
lenght = len(letters)
tempCounter = 0
totalCounter = 0

for i in range(0, lenght - 3):
    if letters[i] == 'X' and letters[i + 1] == 'Z' and letters[i + 2] == 'Z' and letters[i + 3] == 'Y': # предполагаем, что текущая буква - это начало "стоп-последовательности", проверяем все букваы наперед
        totalCounter = max(totalCounter, tempCounter) # если предположение было вкерным, то фиксируем длину цепочки
        tempCounter = 0
    tempCounter += 1 # если предположение было неверным, то увеличиваем счетчик длины текущей последоваетьности

print(totalCounter + 2) # ввыодим ответ, делая поправку на неточность работы алгоритма