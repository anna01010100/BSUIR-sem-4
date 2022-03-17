
from random import randint


class Essence:

    def __init__(self):
        self.hp = 100
        self.age = 0
        self.pergancy = 0
        self.max_hunger = 40 #необходимо только для животных
        self.current_hunder = 0
        self.need_food_for_one_step = 5
        

    def action(self):
        pass

    def reproduce(self):
        pass

    def be_hungry(self):
        pass

    def fall_sick(self):
        ''' Болезнь существа'''
        chance_to_fall_sick = randint(0,2)
        if chance_to_fall_sick == 1:
            self.hp -= randint(10, 60)

    def get_hp_from_rain(self):
        ''' Рандомное пополнение здоровья в клетке для всех существ '''
        self.hp +=10

    def grow_old(self):
        ''' Cтарение. Происходит каждый ход'''
        self.age += 1
        self.hp -= randint(0, 5)

    


    
