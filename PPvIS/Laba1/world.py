from plant import Plant
from herbivore import Herbivore
import random

class World:
    def __init__(self, n, m):
        '''Задание параметров мира и его генерация'''
        self.size_pole_x = n
        self.size_pole_y = m
        self.step = 0
        self.pole = [[0] * m for i in range(n)]
        for i in range(n):
            for j in range(m):
                self.pole[i][j] = World.Cell((i,j))
        self.generate_world()
        self.make_step()

    def show_step(self):
        '''Вывод текущего состояния мира в консоль'''
        for i in range(self.size_pole_x):
            str_for_print = ''
            for j in range(self.size_pole_y):
                str_for_print +=self.pole[i][j].show_animals()
            print(str_for_print)  
        print('_______________________________')  
        
        #необязательные элементы, однако без них мир отображается недостаточно корректно: видно только одно существо из всех находящихся
        print('live:')
        for i in range(self.size_pole_x):
            for j in range(self.size_pole_y):
                for k in self.pole[i][j].essence_in_cell:
                    print( k.pic +' id = ', k.id, 'hp = ', k.hp, ' perg = ', k.pergancy, 'coords = ', (i,j))
        print( 'step  = ', self.step)
                

    def add_essence(self, essence, coords):
        '''Вспомогательная функция для добавления существа в клетку'''
        self.pole[coords[0]][coords[1]].essence_in_cell.append(essence)

    def remove_essence(self, essence, coords):
        '''Вспомогательная функция для удаления существа из клетки'''
        if essence in self.pole[coords[0]][coords[1]].essence_in_cell:
                self.pole[coords[0]][coords[1]].essence_in_cell.remove(essence)


    def generate_world(self):
        '''Первый шаг, совершается при невозможности открыть файл или создании нового мира. Рандомная генерация животных и растений по 
        клеткам'''
        for i in range(self.size_pole_x):
            for j in range(self.size_pole_y):
                decide = random.choice(['PLANT', 'HERBIVORE', 'HERBIVORE', 'EMPTY'])
                if decide == 'PLANT':
                    self.add_essence(Plant(), (i,j))
                elif decide == 'HERBIVORE':
                    self.add_essence(Herbivore(), (i,j))
                    

        self.show_step()


    def make_step(self):
        '''Метод обработки шага для симуляции, последовательно в каждой клетки для каждого животного по очереди.'''
        while True:
            if input('Нажмите Enter для продолжения, exit для прерывания и сохранения в файл: ') != 'exit':
                for i in range(self.size_pole_x):
                    for j in range(self.size_pole_y):
                        for essence in self.pole[i][j].essence_in_cell:
                            self.kill_plant(essence,self.pole[i][j].essence_in_cell, (i,j))
                            action =  essence.action(self.pole[i][j].essence_in_cell)
                            self.hangling_action(essence, action, (i, j))
                            self.move(essence, (i, j))
                self.step += 1
                self.show_step()
            else:
                return 'exit'


    def hangling_action(self, essence, action, coords):
        '''Обработка рождения и смерти, полученных от класса Essence и его потомков'''
        if action == 'DIE':
            self.remove_essence(essence, (coords[0], coords[1]))
        elif type(action) == Plant or type(action) == Herbivore:
            self.add_essence(action, self.random_coords((coords[0], coords[1]))) 
    

    def random_coords(self, coords):
        '''Нахождение нового места для потомка растения'''
        x = random.randint(0, self.size_pole_x - 1)
        y = random.randint(0, self.size_pole_y - 1)
        return (x,y)


    def kill_plant(self, essence, essences_in_cell, coords):
        '''Метод, при котором травоядное убивает растение только при необходимости поесть и до тех пор, пока не насытится'''
        if type(essence) == Herbivore:
            for food in essences_in_cell:
                if essence.hunger <= 0:
                    break
                else:
                    if type(food) == Plant:
                        print(f'Убито растение № {food.id} by herb №{essence.id}')
                        hp_from_killed = food.hp
                        self.remove_essence(food, coords)
                        essence.if_kill(hp_from_killed)  
    

    def find_plant_or_pair(self, essence, coords):
        '''Нахождение партнера (в первую очередь) и еды (во вторую) в клетках, которые окружают травоядное животное, или внутри нее'''
        if type(essence) == Herbivore:
            for i in range(coords[0] - 1, coords[0] + 1):
                for j in range(coords[1] - 1, coords[1] + 1):
                    if 0 <= i < self.size_pole_x and 0 <= j <self.size_pole_y:
                        for essence in self.pole[i][j].essence_in_cell:
                            if type(essence) == Herbivore:
                                return (i, j)
                            elif type(essence) == Plant:
                                return (i, j)
            return (i, j)

    

    def move(self, essence, coords):
        '''Перемещение существа из одной ячейки в другую'''
        if type(essence) == Herbivore:
            new_coords = self.find_plant_or_pair(essence, coords)
            if new_coords:
                self.add_essence(essence, new_coords)
                self.remove_essence(essence, coords)

    def save_simulation(self):
        '''Возможность сохранения информации о мире в соотвествии с принципами SOLID'''
        return self


    class Cell:
        '''Класс одной ячейки, хранит в себе информацию о животных, находящихся в ней'''

        def __init__(self, coords):
            self.coords = coords
            self.essence_in_cell = list()

        
        def show_animals(self):
            if self.essence_in_cell:
                return self.essence_in_cell[0].pic
            else:
                return ' . '