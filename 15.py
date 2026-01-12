import random
d = {
    'apple': ['malum', 'pomum', 'popula'],
    'fruit' : ['baca', 'bacca', 'popum'],
    'punisment': ['malum', 'multa']
}
print(d['apple'])
print(d)
new_dict = {}
for key, values in d.items():
    for value in values:
        if value not in new_dict:
            new_dict[value] = key
        else:
            value += '1'
            new_dict[value] = key
print(new_dict)

set_01 = set()
set_02 = set()
for i in range(0,10):
    set_01.add(random.randint(0,9))
    set_02.add(random.randint(0,9))
print(set_01, set_02)
k = len(set_01) + len(set_02) - len(set_01 & set_02)*2
print(k)
print('Унікальні у першому рядку: ', len(set_01) - len(set_01 & set_02), 'Унікальні у другому рядку: ', len(set_02) - len(set_01 & set_02))