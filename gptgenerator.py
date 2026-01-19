data = [12, "305", 7]
def gen(d):
    for item in d:
        yield from(int(x)*2 for x in str(item))
for x in gen(data):
    print(x)

def couples(n):
    for item in n:
        if int(item) % 2 == 0:
            yield item
num = input("Input your number: ")
for x in couples(num):
    print(x)