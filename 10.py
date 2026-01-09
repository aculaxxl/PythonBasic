list_num = []
while True:
    try: 
        num = int(input("input num: "))
    except ValueError:
        print("Try again input NUM: ")
    if num == 0:
        break
    list_num.append(num)
print(list_num)
print(list(enumerate(list_num)))
print(type(list(enumerate(list_num))[1]))
i = int(input('input searching number: '))
k = 0
list_inx = []
while True:
    try:
        k = list_num.index(i, k)
        list_inx.append(k)
        k = k + 1
    except ValueError:
        break
    
print('Your index is: ', list_inx)
