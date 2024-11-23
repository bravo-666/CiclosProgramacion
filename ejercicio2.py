'''
Crea un programa que permita adivinar un número. La aplicación genera un 
número aleatorio del 1 al 100. A continuación va pidiendo números y va 
respondiendo si el número a adivinar es mayor o menor que el introducido,
a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). 
El programa termina cuando se acierta el número (además te dice en cuantos 
intentos lo has acertado), si se llega al limite de intentos te muestra el 
número que había generado.
Para genear un número entero aleatorio se utiliza la función randint
del paquete random

import random
aleatorio = random.randint(limite_inf, limite_sup)
'''


import random
al = random.randint(1, 100)

inten = 10

while inten > 0:
    inten -= 1 
    num = int(input('Ingresa un numero del 1 al 100: '))

    if num == al:
        print('Felicidades adivinaste el numero!')
    elif inten == 0:
        print('Se terminaron tus intentos :(  El numero era: ', al)
    elif num < al:
        print(f'El numero es mayor al introducido, sigue intentando.  Te restan {inten} intentos')
    elif num > al:
        print(f'El numero es menor al introducido, sigue intentando.  Te restan {inten} intentos')
    else:
        print('Fin del Juego')
        break
