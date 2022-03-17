from essence import Essence
from random import *

class Herbivore (Essence):

    id_counter = 0
    #cчетчик всех животных этого вида, реализуется в __init__


    def __init__(self):
        '''Инициация травоядного, с начальными параметрами: возраст смерти; время, необходимое для размножения(рандомно);
        также присваивается порядковый номер. Вводится понятие беременности '''
        super().__init__()
        self.max_age = 20
        self.pic = ' H '
        self.hunger = 0

        self.time_to_make_child = randint(1,3)
        
        Herbivore.id_counter += 1
        self.id = Herbivore.id_counter


    def reproduce(self, list_of_other_essences):
        ''' Метод для зачатия, рождения ребенка, и вынашивания'''
        if self.hp > self.hp*0.5 and self.pergancy == 0:
            for essence in list_of_other_essences:
                if type(essence) == Herbivore and essence is not self:
                    self.pergancy += 1
                    print(f"НАЙДЕН ПАРТНЕР ДЛЯ ЖИВОТНОГО №{self.id} - {essence.id}")
        elif self.pergancy >= self.time_to_make_child:
            child = Herbivore()
            self.pergancy = 0
            
            return child
        elif self.pergancy > 0:
            self.pergancy += 1


    def action(self, list_of_other_essences):
        ''' Действие, которое изменяет только параметры этого животного. Передается в мир для дальнейшей обработки при появлении нового 
        существа или удаления этого '''
        self.be_hungry()
        self.grow_old()
        self.fall_sick()
        
        if self.hp<0 or self.age>self.max_age:
            print(f'Животное {self.id} умерло')
            return 'DIE'
        child = self.reproduce(list_of_other_essences)
        return child if child else "No"


    def if_kill(self, hp_from_killed):
            '''Процесс пополнения здоровья и утоления голода от умершего растения'''
            self.hunger -= 20
            if self.hunger < 0:
                self.hunger = 0
            self.hp += hp_from_killed*0.1


    def be_hungry(self):
        ''' Процесс голодания животного, происходит каждый ход вне зависимости от его действий'''
        self.hunger += 10
        if self.hunger >= self.max_hunger:
            self.hp -= 20