class Counter:
    def __init__(self, minimal: int, maximum: int, start: int):
        self.minimal = minimal
        self.maximum = maximum
        self.start = start
    
    def count(self) -> int:
        if self.minimal <= self.start <= self.maximum:
            self.start += 1
            return self.start
        else:
            return ('Ви ввели невірні поаткові дані!')
    
user_minimal = int(input('Введіть мінімальне значення лічильника: '))
user_maximum = int(input('Введіть максимельне значення лічильника: '))
user_start = int(input('Введіть стартову позицію: '))
user_counter = Counter(user_minimal, user_maximum, user_start)
print('Значення лічильника: ', user_counter.count())

