# -*- coding: utf-8 -*-

cadena1 = raw_input("Dime una palabra: ")

palabra_al_reves = cadena1[::-1]

print(palabra_al_reves)

if( cadena1 == palabra_al_reves ):
    print("Es palíndromo")
else:
    print("No es palíndromo")

if __name__ == '__main__':
    pass