with open('input.txt', "r") as f, open("short.txt", "w") as f2:
    for line in f:
        print(len(line), ": ", line)
        if len(line.strip()) < 10:
            f2.write(line)
