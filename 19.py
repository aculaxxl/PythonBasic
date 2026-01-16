
def expanded_form(number):
    try:
        number = int(number)
    except (TypeError, ValueError):
       print('Ви ввели не число!')
    else:
        expanded_number = ''
        temp = number
        for i in range(len(str(number))-1, -1, -1):
            num_i = number // 10**i
            expanded_number += str(num_i*10**i)
            if i != 0:
                expanded_number += '+'
            number -= num_i*10**i
        print(f'Ваше число {temp} розгортається як: ', expanded_number)

num = input('Введіть число: ')
expanded_form(num)
