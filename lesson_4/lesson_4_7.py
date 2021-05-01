def fact(m):
    for i in range(1, m + 1):
        yield i


factorial = 1
n = int(input('Введите целое положительное число. Программа вычислит факториалы всех чисел до него включительно: '))
for el in fact(n):
    factorial = factorial * el
    print(el, '!', '=', factorial)
