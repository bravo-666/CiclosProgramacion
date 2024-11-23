'''
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de 
números a introducir). El programa debe informar de cuantos números introducidos 
son mayores que 0, menores que 0 e iguales a 0
'''

cant = int(input('Cuantos numeros quieres introducir?:'))
me = 0 
ma = 0 
ig = 0 

for i in range(cant):
    num = int(input('Introduce un numero'))
    if num > 0:
        ma += 1
    elif num < 0:
        me += 1
    else:
        ig += 1
print(f'Numeros mayores a 0: {ma}')
print(f'Numeros menores a 0: {me}')
print(f'Numeros iguales a 0: {ig}')