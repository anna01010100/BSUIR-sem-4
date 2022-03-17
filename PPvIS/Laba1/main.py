from world import *
import sys
import pickle


if (len(sys.argv) > 1):
    '''Возможность запуска новой симуляции с командной строки'''
    name_of_prog, size_x, size_y = sys.argv
elif input('Enter "continue" to open file:') =='continue':
    '''Запуск симуляции с сохраненного файла'''
    pass
else:
    size_x = input('Please, enter size x of pole:')
    size_y = input('Please, enter size y of pole:')
    new_world = World(int(size_x), int(size_y))


def save_to_file(world):
    with open(r'saved_game.txt', 'wb') as file:
        pickle.dump(world, file)
        for i in range(world.size_pole_x):
            for cell in range(world.size_pole_y):
                pickle.dump(world.pole[i][cell], file)
        print("saved")
