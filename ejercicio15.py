'''
Realizar un programa que pida al usuario un número entero y muestre el mismo número en binario
'''

def entero_a_binario():
    num = int(input("Introduce un número entero: "))
    
    nb = bin(num)[2:]
    
    print(f"El número {num} en binario es {nb}")

entero_a_binario()
