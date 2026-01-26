class Counter:
    def __init__(self, minimal: int, maximum: int, amount: int, start: int):
        self.minimal = minimal
        self.maximum = maximum
        self.amount = amount
        self.value = start
        self.start = start
        if self.minimal >= self.maximum or self.minimal > self.start or self.maximum < self.start:
            raise ValueError('Початкові значення введені некоректно! ')
        
    def increment(self):
        self.value += self.amount
        if self.value > self.maximum:
            raise ValueError('Ви вийшли за межі максимуму')
        
    def decrement(self):
        self.value -= self.amount
        if self.value < self.minimal:
            raise ValueError('Ви вийшли за межі мінімуму')
        
    def restart(self):
        self.value = self.start
        
    def get(self):
        return self.value

user_minimal = int(input('Введіть мінімальний показник: '))
user_maximum = int(input('Введіть максимальний показник: '))
user_amount = int(input('Введіть крок лічильника: '))
user_start = int(input('Введіть стартове значення: '))

try:
    count = Counter(user_minimal, user_maximum, user_amount, user_start)
    count.decrement()
    print(count.get())
    
except ValueError as e:
    print(e)
