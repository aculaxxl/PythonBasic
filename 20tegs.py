def hash_tag_creator(user_message):
    if user_message == '' or user_message.isspace():
        raise ValueError('Введіть не пустий текст!')
    user_message = '#' + (user_message.replace(' ', '')).title()
    if len(user_message) > 30:
        print('false')
    else:
        print(user_message)
try:
    your_tag = input('Please, input your tag: ')
    hash_tag_creator(your_tag)
except ValueError as e:
    print(e)