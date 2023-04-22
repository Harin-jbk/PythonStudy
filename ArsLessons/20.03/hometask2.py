# я думаю, как решать эту задачу ты разобрался, напоминаю лишь особенности работы с листом
delit = []
for i in range(110203, 110246):
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            if j % 2 == 0:
                delit.append(j)
    if len(delit) == 4:
        print(delit)
    delit = []