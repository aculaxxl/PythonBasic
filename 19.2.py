def number_sum(number):
    if number < 0:
        raise ValueError("Ви ввели не позитивне число")
    else:
        number = list(map(int,str(number)))
        temp = number
        summa = 0
        for item in number:
            summa += item
        print(f'Ваше число {temp} сумується як: ', summa)

num = int(input('Введіть число: '))
number_sum(num)