try:
    file =  open('new_file.txt', "x")
except FileExistsError:
    print('FileExistsError')
with open('new_file.txt', 'w') as file:
    while True:
        raw = input('Input your message: ')
        if raw == '':
            break
        file.write(raw + '\n')

with open('new_file.txt', 'r') as file:
    print(file.read())