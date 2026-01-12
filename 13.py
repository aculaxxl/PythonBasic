import random
set_var = set([1,2,2,3,3])
print(set_var)
list_var = []
for i in range(10):
    list_var.append(random.randint(0,4))
print(list_var)
set_var = set(list_var)
print(set_var)
set_var.add(8)
print(set_var)
print(frozenset(set_var))
s = frozenset(set_var)
set_var_2 = {s, 2}
print(set_var_2)
text_files = ['text1','text2', 'text2', 'text1','text3' ]
print(frozenset(text_files))
set_01 = {1,2,3,4,5}
set_02 = {4,5,6,7,8,}
print(set_01 - set_02)
print(set_01 | set_02)
print(set_01 & set_02)
print(set_01 ^ set_02)
for item_set in set_02:
    if item_set in set_01:
        print(item_set)