# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
n = int(input("Введите количество монеток: "))
count = 0
for i in range(n):
    coin = int(input('Введите значение 1 - "орёл" или 0 - "решка": '))
    count += coin
    i += 1
if count <= n//2:
    print("Минимальное количество монет, которые нужно перевернуть ", count)
else:
    print("Минимальное количество монет, которые нужно перевернуть ", n - count)