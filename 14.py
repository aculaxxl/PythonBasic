user_sring = input('Введіть ваш текст: ')
words_dict = {word:user_sring.count(word) for word in user_sring.split(' ')}
print(words_dict)