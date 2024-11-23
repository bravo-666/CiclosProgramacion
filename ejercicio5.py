'''
Programa que pida 10 números e imprima el promedio de estos.

Se utilizan los conceptos del programa anterior de contador y acumulador.
'''

acu = 0 
cont = 0 

for i in range(10):
    n1 = int(input('Ingresa un numero: '))
    acu += n1 
    cont += 1
prom = acu / cont
print(f'El promedio de los numeros es {prom} ')