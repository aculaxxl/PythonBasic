file_name = input('Введіть назву файлу, з якого скопіювати вміст: ')
new_file_name = input('Введіть назву нового файлу: ')
with open(file_name + ".txt", "r") as file:
    lines = file.read()
try:
    file2 = open(new_file_name + ".txt" , "x")
    file2.close()
except FileExistsError:
    print('Такий файл вже існує, перезаписуємо у нього')
with open(new_file_name + ".txt", "a") as file2:
        file2.write(lines)