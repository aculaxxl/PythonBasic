h = int(input('Введіть висоту фігури:'))
def treingle_a(hight):
    for i in range(hight):
        list_traingle = []
        for j in range(hight*2-1):
            if i == hight - 1:
                list_traingle.append('*')
            elif j == hight-i-1 or j == (hight+i-1):
                list_traingle.append('*') 
            else:
                list_traingle.append(' ')
        print("".join(list_traingle))
treingle_a(h)
print('\n\n')
def treingle_b(hight):
    for i in range(hight):
        list_traingle = []
        for j in range(hight*2-1):
            if i == hight - 1:
                list_traingle.append('*')
            elif hight-i-1 <= j <= (hight+i-1):
                list_traingle.append('*') 
            else:
                list_traingle.append(' ')
        print("".join(list_traingle))
treingle_b(h)

print('\n\n')

def treingle_c(hight):
    for i in range(hight):
        list_traingle = []
        for j in range(hight*2-1):
            if i == hight - 1:
                list_traingle.append('*')
            elif hight-i-1 <= j <= (hight+i-1):
                list_traingle.append('*') 
            else:
                list_traingle.append(' ')
        print("".join(list_traingle))
    for i in range(1, hight+1):
        list_traingle = []
        for j in range(hight*2-1):
            if j == i-1 or j == (hight*2-i-1):
                list_traingle.append('*') 
            else:
                list_traingle.append(' ')
        print("".join(list_traingle))

treingle_c(h)

print('\n\n')

def treingle_d(hight):
    for i in range(hight):
        list_traingle = []
        for j in range(hight*2-1):
            if i == hight - 1:
                list_traingle.append('*')
            elif hight-i-1 <= j <= (hight+i-1):
                list_traingle.append('*') 
            else:
                list_traingle.append(' ')
        print("".join(list_traingle))
    for i in range(1, hight+1):
        list_traingle = []
        for j in range(hight*2-1):
            if j == i-1 or j == (hight*2-i-1) or j == hight-1:
                list_traingle.append('*') 
            else:
                list_traingle.append(' ')
        print("".join(list_traingle))

treingle_d(h)