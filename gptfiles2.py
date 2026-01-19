from datetime import datetime
import string
try:
    f = open('diary.txt', 'x')
    f.close()
except FileExistsError:
    print('Щоденник вже існує')
with open('diary.txt', 'a') as f:
    now = datetime.now()
    formatted = now.strftime("%d.%m.%Y %H:%M")
    print(formatted, ': ')
    f.write(formatted + ": " + input() + '\n')