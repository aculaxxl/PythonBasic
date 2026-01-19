def calculator(a,b,sign):
    if a == '' or a.isspace() or b == '' or b.isspace() or sign == '' or sign.isspace():
        raise ValueError('Ви ввели пусті значення')
    sign_list = ['+', '-', '/', '*']
    if sign not in sign_list:
        raise ValueError('Ви ввели  не підходящий символ')
    try:
        a = int(a)
        b = int(b)
    except:
        raise ValueError('Ваші символи не є числами')
    if sign == '/' and b == 0:
        raise ZeroDivisionError('Дільник не може бути рівний нулю')
    operation = str(a) + sign + str(b)
    return eval(operation)
num1 = input('Введіть перше число: ')
num2 = input('Введіть друге число: ')
s = input('Введіть операцію: ')
try:
    print(calculator(num1,num2,s))
except (ValueError, ZeroDivisionError) as e:
    print(e)