import random
print(random.uniform(0,10))
list_random = []
m = int(int(input("Введіть необхідну кількість чисел: ")))
for i in range(m):
    list_random.append(random.randint(0,10))
print(list_random)
k = 0
for i in range(1,m-1):
    if list_random[i-1]<list_random[i] and list_random[i]>list_random[i+1]:
        k += 1
print("Кількість елементів, які більше двох сусідів: ", k)


]