class Lamp:
    def __init__(self, status: bool):
        self.status = status

    def unknown_turn(self):
        if self.status is True:
            self.status = False
        else:
            self.status = True

    def turn_on(self):
        self.status = True
    
    def turn_off(self):
        self.status = False
    
    def get_status(self):
        if self.status is True:
            return True
        else:
            return False
    
class Switch:
    def press(self, lamp):
        if lamp.get_status() == True:
            lamp.turn_off()
        else:
            lamp.turn_on()
    
        
user_lamp = Lamp(True)
user_lamp.turn_off()
user_lamp.unknown_turn()
user_lamp_2 = Lamp(False)
switch = Switch()
switch.press(user_lamp)
print(f'Статус лампочки 1: {user_lamp.get_status()} \n Статус лампочки 2: {user_lamp_2.get_status()}')