from random import randint
m = []
for i in range(10):
    m.append(randint(0,50))
print(m)
for i in range(9):
    for j in range(9-i):
        if m[j] > m[j+1]:
            m[j], m[j+1] = m[j+1], m[j]
    print(m)
print('\n\n',m)