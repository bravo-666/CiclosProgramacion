'''
Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma
y la media de todos los números introducidos.

Para este problema se requiere de un acumulador y un contador

Contador: Variable que va, como su nombre lo indica, contando elementos (iteraciones),
por cada iteración el contador va incrementando en 1

Ejemplo:
contador = 0
for i in range(5):
    contador = contador + 1
print(contador)

Acumulador: Variable que va, como su nombre lo indica, acumulando valores en cada iteración,
por cada iteración al valor inicial se le suman nuevos valores al acumulador

Ejemplo:
acumulador = 0;
for i in range(5):
    acumulador = acumulador + i
print(acumulador)
'''
con = 0
acu = 0

while True:
    n = float(input('Escribe un numero (0 para terminar): '))
    if n == 0:
        break
    acu += n
    con += 1

if con > 0:
    media = acu/con

else:
    media = 0

print(f'La suma de los numero introducidos: {acu}')
print(f'La media de los numero introducidos: {media}')
