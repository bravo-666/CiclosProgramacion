'''
Escribe un programa que dados dos números, uno real (base) y un entero positivo 
(exponente), saque por pantalla el resultado de la potencia. No se puede 
utilizar el operador de potencia.
'''

n1 = int(input('Escribe un numero: '))
ex = int(input('Escribe su potencia (numero positivo): '))

for i in range(ex):
    re = n1 * n1
    print('EL resultado es: ', re)