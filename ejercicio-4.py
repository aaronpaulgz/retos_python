# -*- coding: utf-8 -*-

p1 = raw_input('Escoge un número: ')
p2 = raw_input('Escoge un número: ')

def calc(x, y):
    if x > y:
        print('{} es mayor'.format(p1))
    elif x < y:
        print('{} es mayor'.format(p2))
    else:
        print('Hey! Tienen valores iguales')

calc(p1, p2)

if __name__ == '__main__':
    pass