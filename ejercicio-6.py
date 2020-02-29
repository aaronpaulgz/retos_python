# -*- coding: utf-8 -*-

num = float(raw_input('Escoge un número: '))

def calc(x):
    if(x >= 0 and x <= 10):
        print('{} está entre 0 y 10'.format(x))
    elif(x >= 11 and x <= 20):
        print('{} está entre 11 y 20'.format(x))
    elif(x >= 21 and x <= 30):
        print('{} está entre 21 y 30'.format(x))
    else:
        print('Nope. Es mayor a 30 o bien menor a 0')

if __name__ == '__main__':
    calc(num)