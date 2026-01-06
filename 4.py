import sys
i = int(input("ВВедіть ваше число: "))
k = 0
m = i
while i != 0:
    i = int(input("ВВедіть ваше число: "))
    k += 1
    m += i
print("Кількість введених чисел: ", k, '\n', "Сума чисел: ", m)