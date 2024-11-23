'''
Realizar un programa para determinar cuánto ahorrará una persona en un año, 
si al final de cada mes deposita cantidades variables de dinero; 
además, se quiere saber cuánto lleva ahorrado cada mes.
'''

def calcular_ahorros_anuales():
    ht = 0
    hm = []

    for mes in range(1, 13):
        deposito = float(input(f'Introduce la cantidad ahorrada en el mes {mes}: '))
        ht += deposito
        hm.append(ht)
    
    print('\nResumen de Ahorros:')
    for mes, ahorro in enumerate(hm, start=1):
        print(f'Mes {mes}: {ahorro}')

    print(f'\nTotal ahorrado en el año: {ht}')

calcular_ahorros_anuales()
