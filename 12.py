new_list = []
z = int(input("Введіть необхідну кількість елементів: "))
for i in range(0,z):
    new_list.append(input('Введіть елемент: '))
print(new_list)
k = int(input("Введіть індекс елемента, який необхідно видалити: "))
for i in range(k,z-1):
    new_list[i] = new_list[i+1]
new_list.pop()
print(new_list)