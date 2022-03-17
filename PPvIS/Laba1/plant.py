from essence import Essence
from random import *

class Plant(Essence):

    id_counter = 0
    #cчетчик всех животных этого вида, реализуется в __init__


    def __init__(self):
        super().__init__()
        '''Инициация растения, с начальными параметрами: возраст смерти(рандомно); время, необходимое для размножения(рандомно);
        также присваивается порядковый номер'''
        self.max_age = randint(5,7)
        self.pic = ' P '
        self.time_to_make_child = randint(1,3)

        Plant.id_counter += 1
        self.id = Plant.id_counter


    def reproduce(self, list_of_other_essences):
        '''Воспроизведение ребенка при хп> половины, и вынашивание ребенка'''
        if self.hp > self.hp*0.5:
            self.pergancy += 1
            if self.pergancy >= self.time_to_make_child:
                child = Plant()
                self.pergancy = 0
                #необязательное поле
                print(f'Создан ребенок растения {self.id}')
                return child
        else:
            self.pergancy = 0


    def action(self, list_of_other_essences):
        ''' Действие, которое изменяет только параметры этого растения. Передается в мир для дальнейше обработки при появлении нового 
        существа или удаления этого '''
        self.grow_old()
        self.fall_sick()
        if self.hp<0 or self.age>self.max_age:
            print(f'Растение {self.id} умерло')
            return 'DIE'
        child = self.reproduce(list_of_other_essences)
        return child if child else "No"

        

        





    

        