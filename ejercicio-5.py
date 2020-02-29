# -*- coding: utf-8 -*-

num = float(raw_input('Escoge un número: '))

def calc(x):
    if x > 0 and x <= 10:
        print('{} está entre 0 y 10'.format(x))
    else:
        print('Nope. Es mayor a 10')

calc(num)

if __name__ == '__main__':
    pass