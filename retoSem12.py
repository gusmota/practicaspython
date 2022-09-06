# #Hacer un programa que pida las ventas en un rango de determinados años\
# #que pida las ventas de cada año dentro del rango
# #que muestre mediante una gráfica de líneas las ventas de cada año.

# #Ejemplo: si el usuario introduce 2015 como año inicial y 2022 como año final, \
# #debe pedirle las ventas de 2015 hasta 2022. Después debe graficar cada uno de esos datos.

def graficar(venta, color):
    plt.bar (venta.keys(), venta.values(), color=color)
    

import matplotlib.pyplot as plt

añoIn = int(input('cual es el año inicial: '))
añoFin = int(input('cual es el año final: '))

ventas = {}
for años in range(añoIn, añoFin+1):
    ventas[años] = float(input('Dime las ventas por año: '))
graficar(ventas, 'red')
plt.show()
