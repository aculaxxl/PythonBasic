list_to_sort = [1,10,5,16,-3,25,14,8,-7,2]

def insertion_sort(list):
    for i in range(1,len(list)):
        temp = list[i]
        print('temp = ', temp)
        min_index = i
        while min_index > 0 and temp < list[min_index-1]:
            list[min_index] = list[min_index - 1]
            min_index -= 1
            print(list, '\n')
        list[min_index] = temp
        print('   ',list, '   ',list[min_index])
    return list
print(insertion_sort(list_to_sort))

