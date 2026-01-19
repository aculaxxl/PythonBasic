from random import randint

def our_sort(matrix, size):
    matrix.append([])
    for i in range(size):
        matrix[size].append(0)
        for j in range(size):
            matrix[size][i] += matrix[j][i]

    for i in range(size):
        for j in range(size-i-1):
            if matrix[size][j] > matrix[size][j+1]:
                matrix[size][j], matrix[size][j+1] = matrix[size][j+1], matrix[size][j]
                for f in range(size):
                    matrix[f][j], matrix[f][j+1] = matrix[f][j+1], matrix[f][j]

    for i in range(size - 1):
        if i % 2 == 0:
            for j in range(size - 1):
                for f in range(size - j -1):
                    if matrix [f][i] < matrix [f+1][i]:
                        matrix [f][i], matrix [f+1][i] = matrix [f+1][i], matrix [f][i]
        
        else:
            for j in range(size - 1):
                for f in range(size - j -1):
                    if matrix [f][i] > matrix [f+1][i]:
                        matrix [f][i], matrix [f+1][i] = matrix [f+1][i], matrix [f][i]
        

while True:
    m = int(input('Введіть розмір матриці М:'))
    if m > 5:
        break
    print('Введіть число, яке більше за 5!')

our_matrix = [[randint(1,50) for i in range(m)] for j in range(m)]

our_sort(our_matrix, m)
for row in our_matrix:
    print(row)