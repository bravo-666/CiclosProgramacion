'''
Programa que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.
'''


def imprimir_tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")

    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
    print()  

for num in range(1, 6):
    imprimir_tabla_multiplicar(num)
