'''
Mostrar en pantalla los N primero números primos. Se pide por teclado la cantidad 
de números primos que queremos mostrar.
'''
import math

def es_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True  
    if numero % 2 == 0:
        return False  
    for i in range(3, int(math.sqrt(numero)) + 1, 2):
        if numero % i == 0:
            return False
    return True

def primeros_n_primos(n):
    primos = []
    numero = 2  
    while len(primos) < n:
        if es_primo(numero):
            primos.append(numero)
        numero += 1
    return primos


cantidad_primos = int(input("Introduce la cantidad de números primos que quieres mostrar: "))


lista_primos = primeros_n_primos(cantidad_primos)


print(f"Los primeros {cantidad_primos} números primos son:")
for primo in lista_primos:
    print(primo)
