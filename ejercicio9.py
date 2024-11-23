'''
Escribe un programa que pida el limite inferior y superior de un intervalo. 
Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0. 
Cuando termine el programa dará las siguientes informaciones:
	* La suma de los números que están dentro del intervalo (intervalo abierto).
	* Cuantos números están fuera del intervalo.
	* He informa si hemos introducido algún número igual a los límites del intervalo.
'''

def solicitar_limites():
    while True:
        limi = float(input("Introduce el límite inferior del intervalo: "))
        lims = float(input("Introduce el límite superior del intervalo: "))
        if limi < lims:
            return limi, lims
        else:
            print("El límite inferior debe ser menor que el límite superior. Por favor, inténtalo de nuevo.")

def procesar_numeros(limi, lims):
    sdi = 0
    cfi = 0
    lim = False

    while True:
        numero = float(input("Introduce un número (0 para terminar): "))
        if numero == 0:
            break
        if limi < numero < lims:
            sdi += numero
        else:
            cfi += 1
        if numero == limi or numero == lims:
            igual_a_limites = True

    print(f"Suma de los números dentro del intervalo: {sdi}")
    print(f"Números fuera del intervalo: {cfi}")
    if igual_a_limites:
        print("Se introdujo algún número igual a los límites del intervalo.")
    else:
        print("No se introdujo ningún número igual a los límites del intervalo.")
