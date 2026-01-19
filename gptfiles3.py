try:
    file = open('reversed.txt', "x")
    file.close()
except FileExistsError:
    print('Фійл іже існує')
with open('input.txt', "r") as file2:
    lines = file2.readlines()
with open('reversed.txt', "w") as file:
        for line in reversed(lines):
            file.write(line)
