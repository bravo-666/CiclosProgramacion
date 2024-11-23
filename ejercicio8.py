'''
Escribir un programa que imprima todos los números pares entre dos números que 
se le pidan al usuario.
'''
print('Bienvenido, programa que imprima todos los números pares entre dos números que se le pidan al usuario.')

n1 = int(input('Introduce el primer numero: '))
n2 = int(input('Introduce el segundo numero: '))

for i in range(n1, n2):
    if i % 2 == 0:
        print(i)
        