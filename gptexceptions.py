def get_age(age_str):
    if age_str == '' or age_str.isspace():
        raise ValueError("Вік не може бути пустим")
    try:
        age_str = int(age_str)
    except ValueError:
        raise ValueError("Вік має бути числом")
    if age_str <= 0 or age_str > 120:
        raise ValueError("Некоректний вік")
    return age_str

try:
    user_age = input('Введіть вік: ')
    print('Ваш вік: ', get_age(user_age))
except ValueError as e:
    print(e)