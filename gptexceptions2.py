def divide(a,b):
    if a == '' or a.isspace() or b == '' or b.isspace():
        raise ValueError('Ви ввели пустий рядок')
    try:
        a = int(a)
        b = int(b)
    except:
        raise ValueError('Ви ввели не числа')
    if b == 0:
        raise ZeroDivisionError('На нуль ділити не можна')
    return a/b

num1 = input('Введіть ділене: ')
num2 = input('Введіть дільник: ')
try:
    print(divide(num1,num2))
except (ValueError,ZeroDivisionError) as e:
    print(e)