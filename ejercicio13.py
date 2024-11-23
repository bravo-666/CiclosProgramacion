'''
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 
euros, el segundo 20 euros, el tercero 40 euros y así sucesivamente. 
Realizar un programa para determinar cuánto debe pagar mensualmente y el total 
de lo que pagó después de los 20 meses.
'''

def calcular_pagos():
    meses = 20
    pi = 10
    ttp = 0

    print("Mes y Pago mensual ")

    for mes in range(1, meses + 1):
        pm = pi * (2 ** (mes - 1))
        ttp += pm
        print(f"{mes}  seria  {pm}")
    
    print(f"Total pagado después de {meses} meses: {ttp} euros")

calcular_pagos()
