books = [ 
    [34587, 'Learning Python, Mark Lutz', 4, 40.95], 
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95], 
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99] 
]
orders = []
quantity = int(input('Введіть кількість замовлень: '))
for i in range(0,quantity):
    order_number = int(input('Введіть номер замовлення: '))
    book = str(input('Введіть назву книги: '))
    amount = int(input('Введіть кількість: '))
    price = float(input('Введіть вартість книги: '))
    orders.append([order_number, book, amount, price])
print('Замовлення у магазині: ', orders)
def book_orders(i): 
    summ = orders[i][2]*orders[i][3]
    if summ < 100:
        summ += 10
    return summ

orders_list = []
for i in range(0,quantity):
    order = (orders[i][0], orders[i][1], book_orders(i))
    orders_list.append(order)
    print(orders_list[i], "\n")
