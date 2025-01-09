import os
from random import choice

os.system('COLOR B')


class MysticBall:
    def __init__(self, words):
        self.words = words

    def __call__(self):
        return choice(self.words)


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        strings = []

        with open(file_name, 'w+') as f:
            strings = f.readlines()

        with open(file_name, 'a+') as f:
            for l in strings:
                f.write(l)

    return write_everything


first = 'Мама мыла раму'
second = 'Рамена мало было'

l = list(map(lambda f, s: f == s, first, second))
print(l)

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

try:
    os.system('PAUSE')
except:
    os.system('CLS')
