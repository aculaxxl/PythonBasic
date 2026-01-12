s = "витя любит лизу"
new_dict = {}
for value in s:
    if value not in new_dict:
        new_dict[value] = 1
    else:
        new_dict[value] += 1
print(new_dict)
grades = {
    "Ann": 90,
    "Bob": 75,
    "Kate": 88
}
middle = 0
for key in grades:
    middle += grades[key]
middle = middle / len(grades)
print(middle)
k = 0
for key in grades:
    if grades[key] > k:
        k = grades[key]
print(k)

words = ["apple", "banana", "apple", "orange", "banana"]
new_dict_2 = {}
for item in words:
    if item not in new_dict_2:
        new_dict_2[item] = 1
    else:
        new_dict_2[item] += 1
print(new_dict_2)


d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d1.update(d2)
print(d1)

words = ["hi", "hello", "cat", "python", "dog"]
new_dict_3 = {}
for item in words:
    if len(item) not in new_dict_3:
        new_dict_3[len(item)] = [item]
    else:
        new_dict_3[len(item)] += [item]
print(new_dict_3)

d = {
    "a": [1, 2],
    "b": [2, 3],
    "c": [1]
}
new_dict_4 = {}
for key in d:
    for value in d[key]:
        if value not in new_dict_4:
            new_dict_4[value] = [key]
        else:
            new_dict_4[value] += [key]
print(new_dict_4)

text = "Python is great and python is easy"
text = text.lower()
print(text)
text_dict = {}
for word in text.split(' '):
    if word not in text_dict:
        text_dict[word] = 1
    else:
        text_dict[word] += 1
print(text_dict)

prices = {
    "apple": 30,
    "banana": 20,
    "orange": 25
}
prices_dict = {}
for key in prices:
    if prices[key] > 22:
        prices_dict[key] = prices[key]
print(prices_dict, "\n\n")

data = {
    "user1": {"age": 25, "city": "Kyiv"},
    "user2": {"age": 17, "city": "Lviv"},
    "user3": {"age": 30, "city": "Kyiv"}
}
city_dict = {}
for user, info in data.items():
    if info['city'] not in city_dict:
        city_dict[info["city"]] = {user:info['age']}
    else:
        city_dict[info["city"]].update({user:info['age']})
print(city_dict)
users = {
    "Ann": 22,
    "Bob": 17,
    "Kate": 30,
    "Tom": 16
}
users_dict = {}
for user, age in users.items():
    if age >= 18:
        users_dict[user] = age
print(users_dict)

d = {
    "a": 1,
    "b": 2,
    "c": 1,
    "d": 2
}
new_dict_5 = {}
for key in d:
    if d[key] not in new_dict_5:
        new_dict_5[d[key]] = [key]
    else:
        new_dict_5[d[key]] += [key]
print(new_dict_5, '\n\n')

words = ["apple", "ant", "banana", "boat", "cat"]
new_dict_6 = {}
for word in words:
    if word[0] not in new_dict_6:
        new_dict_6[word[0]] = [word]
    else:
        new_dict_6[word[0]] += [word]
print(new_dict_6)

items = ["pen", "book", "pen", "pencil", "book", "pen"]
new_dict = {}
for wor in items:
    if wor not in new_dict:
        new_dict[wor] = 1
    else:
        new_dict[wor] += 1
print(new_dict)

shop = {
    "apple": {"price": 30, "qty": 10},
    "banana": {"price": 20, "qty": 5},
    "orange": {"price": 25, "qty": 8}
}
shop_price = {}
for key, value in shop.items():
    shop_price[key] = value['price']*value['qty']
print(shop_price)

users = {
    "u1": {"age": 25, "city": "Kyiv"},
    "u2": {"age": 30, "city": "Lviv"},
    "u3": {"age": 17, "city": "Kyiv"},
    "u4": {"age": 40, "city": "Lviv"}
}

text = "dog cat dog bird cat dog"
dog_dict = {}
for item in text.split(' '):
    if item not in dog_dict:
        dog_dict[item] = 1
    else:
        dog_dict[item] += 1
print(dog_dict)
dog_list = []
for item in dog_dict:
    dog_list.append((item,dog_dict[item]))
print(dog_list)

text = "apple banana apple orange banana apple grape"
fruit_dict = {}
for item in text.split(' '):
    if item not in fruit_dict:
        fruit_dict[item] = 1
    else:
        fruit_dict[item] += 1
fruit_list = []
for item in fruit_dict:
    fruit_list.append((item, fruit_dict[item]))
print(fruit_list)
fruit_list.sort(key=lambda x: x[1])
print(fruit_list)