from random import randint

m = int(input('Введіть кількість стовпців: '))
n = int(input('Введіть кількість рядків: '))
our_matrix = [[randint(1,50) for i in range(m)] for j in range(n)]

def summ(matrix, m, n):
    for i in range(n):
        row_sum = 0
        for j in range(m):
            row_sum += matrix[i][j]
        matrix[i].append(row_sum)
    matrix.append([])
    for i in range(m):
        row_sum = 0
        for j in range(n):
            row_sum += matrix[j][i]
        matrix[n].append(row_sum)


summ(our_matrix, m, n)
#for i in range(n+1):
 #   for j in range(m+1):
  #      if i == n and j == m:
   #         break 
    #    print(f'{our_matrix[i][j]:5}', end = '')
    #print('\n')

for i in range(n):
    for j in range(m):
        print(f'{our_matrix[i][j]:5}', end='')   # перші m елементів
    print(' |', f'{our_matrix[i][m]:5}')   

print('-' * (5*(m+1) + 3))
for j in range(m):
    print(f'{our_matrix[n][j]:5}', end='')