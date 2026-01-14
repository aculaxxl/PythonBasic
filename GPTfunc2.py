#Програма просить ввести дані юзерів, а потім дані для пошуку юзера за конкретним значенням-вік та місто
new_users = []
i = int(input('Введіть кількість користувачів: '))
for j in range(i):
    user_j = {'name': input('Введіть юзера:'), 'age' : int(input('Введіть вік:')), 'city' : input('Введіть місто: ') }
    new_users.append(user_j)
print(new_users)
age_find = int(input("Age: "))
city_find = input("City: ")
def filter_user(u:list, a:int, b:str ):
    i = 0
    for item in u:
        if item['age'] == a and item['city'] == b:
            print(item['name'])
            i += 1
    if i == 0:
        print("Такого користувача не існує!")

filter_user(new_users, age_find, city_find)  

