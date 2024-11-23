'''
Escribe un programa que diga si un número introducido por teclado es o no primo. 
Un número primo es aquel que sólo es divisible entre él mismo y la unidad. 
Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es 
divisible por algún otro número.
'''

print('Este programa te puede decir si un numero es primo o no')

import math

def es_primo(n1):
    if n1 <= 1:
        return False
    if n1 == 2:
        return True
    if n1 % 2 == 0:
        return False
    for x in range(3, int(math.sqrt(n1)) + 1, 2):
        if n1 % x == 0:
            return False
    return True

n1 = int(input('Escribe un numero: '))

if es_primo(n1): 
    print(f'El número {n1} es primo.') 
else: 
    print(f'El número {n1} no es primo.')
