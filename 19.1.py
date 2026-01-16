def number_sum(number):
    try:
        number = int(number)
        if number < 0:
            raise ValueError("Ви ввели не позитивне число")
    except (TypeError, ValueError):
       print('Ви ввели не число або не позитивне число!')
    else:
        number = list(map(int,number))
        temp = number
        summa = 0
        for item in number:
            summa += item
        print(f'Ваше число {temp} сумується як: ', summa)

num = input('Введіть число: ')
number_sum(num)

