transactions = [120, 50, 300, 450, 20]
threshold = int(input('Введіть лімітну сумму: '))
def large_transactions(x,y):
    if x > y:
        print(x) 

def count_large_transactions(x,y):
    count = 0
    for i in x:
        if i > y:
            count += 1
    return count
        
for item in transactions: 
    large_transactions(item, threshold)
print(count_large_transactions(transactions, threshold))

price = float(input('Введіть вартість товару:'))
discount = float(input('Введіть знижку на товар: '))
def count_discount(x,y):
   new_price = x - x * y * 0.01
   return new_price
print(f'Ціна за знижкою: {count_discount(price, discount):.2f} grivenь')

order = []
i = 1
while True:
    i = int(input('Введіть кількість товару:'))
    if i == 0:
        break
    y = float(input('Введіть вартість товару:'))
    order.append([i, y])
print(order)

def total_order_price(amount, price):
    return amount * price

total_order = []
price_total = 0
item_total = 0
for item in order:
    item_total = total_order_price(item[0], item[1])
    total_order.append(item_total)
    price_total += item_total

if price_total < 100:
    price_total += 10

print('Вартість по кожній позиції товару: ', total_order, 'Загальна вартість замовлення: ', price_total)
