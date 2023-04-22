count = 0
divisors = []
maxDivisors = []
maxCount = 0
divisible = 0
for i in range(120115, 121251):
    divisors = []
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
            divisors.append(j) # добавляем еще один делитель
    if len(divisors) > maxCount: # если количество делителей у текущего числа больше, чем у всех, что были до этого
        maxDivisors = divisors
        maxCount = len(divisors)
        divisible = i 
print (divisible, len(maxDivisors), maxDivisors)