def score(n):
    try:
        n = int(n)
    except ValueError:
        raise ValueError('Кількість оцінок має бути числом! ')
    if n <= 0:
        raise ValueError('Кількість оцінок не може бути заданим числом!')
    score_list = []
    all_score = 0
    max_score = 0
    min_score = 12
    for i in range(0,n):
        m = input('Введіть оцінку: ')
        if m == '' or m.isspace():
            raise ValueError('Оцінка не може бути порожньою!')
        try:
            m = int(m)
        except:
            raise ValueError('Оцінка має бути числом!')
        if m < 0 or m > 12:
            raise ValueError('Некоректна оцінка!')
        score_list.append(m)
        all_score += m
        if m > max_score:
            max_score = m
        if m < min_score:
            min_score= m
    return (f'Середня оцінка {all_score/n}, найвища оцінка:  {max_score}, найнижча оцінка: {min_score}')
        
try:
    number_of_scores = input('Введіть кількість оцінок: ')
    print(score(number_of_scores))
except ValueError as e:
    print(e)