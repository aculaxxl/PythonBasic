string = input("Input your message: ")
symbol = input("Input your sybol: ")
i = string.find(symbol)
if i == -1:
    print("The text does not include this character.")
else:
    print("index of your symbol is: ", end = '')
    while i != -1:
        print(i, end = ' ')
        i = string.find(symbol, i +1)
   
