try:
    file = open('input.txt', "x")
    file.close()
except FileExistsError:
    print('Файл вже інсує')
with open('input.txt',"w") as file:
    while True:
        raw = input("input your message: ")
        if raw == 'stop':
            break
        file.write(raw + '\n')
