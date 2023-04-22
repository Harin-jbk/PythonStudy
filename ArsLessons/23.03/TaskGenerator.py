import random
matrixSize = 5 # размер матрицы
symbol = 7 # символ, который ищем
matrix = []
file = open("output.txt", 'r+')
random.seed(8)

# блок заполнения нашей матрицы
for i in range(matrixSize):
    inputList = [] # создаем массив
    for j in range(matrixSize):
        inputList.append(random.randint(1, 9)) # во внутренний массив в цикле кладем числа
    matrix.append(inputList) # во внутренний массив добавляем
print(matrix[3][4])
# ------------------------------
# Блок записи в файл

for i in range(0, matrixSize):
    for j in range(0, matrixSize):
        number = random.randint(1, 9) # генерируем число в диапазоне от 1 до 9
        file.write(str(number) + " ") # записываем число в строку
    file.write("\n")

# ------------------------------
# Блок подсчета количества встречающихся символов
counter = 0
for i in range(0, matrixSize):
    for j in range(0, matrixSize):
        if matrix[i][j] == symbol:
            counter += 1 # если текущий символ тот, который нам нужен, то увеличиваем счетчик
print(counter)
