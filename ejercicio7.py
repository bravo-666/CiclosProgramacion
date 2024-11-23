'''
lgoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL' 
en caso contrario, el programa termina cuando se introduce un espacio.
'''

def voc(letra):
    return letra.lower() in 'aeiou'
while True:
    letra = input('Introduce una letra (preciona espacio para salir): ')
    if letra == ' ':
        break
    elif voc(letra):
        print('Vocal')
    else:
        print('No es vocal')