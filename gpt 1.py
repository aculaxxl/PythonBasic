str = input("Enter your text: ")
i = 0
for word in str.split(' '):
    i += len(word)
print("Your string contains", i, "symbols")
for i in range(len(str)):
    if str[i].isdigit() == True:
        print(i)
print(str[len(str)::-1])

     