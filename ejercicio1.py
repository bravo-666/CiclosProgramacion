'''
Crea una programa que pida un número y calcule su factorial (El factorial de 
un número es el producto de todos los enteros entre 1 y el propio número y se 
representa por el número seguido de un signo de exclamación. 
Por ejemplo 5! = 1x2x3x4x5=120)
'''

n1 = int(input('Escribe un numero para calcular su factorial:'))
f = 1
for t in range(1, n1+1):
    f = f*t
print('Su factorial es', f)