import sys
N = int(input("Введіть потрібне число: "))
k = 1
while k**2 <= N:
    print(k**2, end =" ")
    k += 1
