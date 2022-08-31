# reto de esta semana es una variante del reto de la semana pasada: un programa que permita 
# crear listas y elimine los valores existentes en otras listas, pero ligeramente diferente.
# 1.Todas las funciones que emplees deberán estar en un archivo diferente, llamado 
# m_retosemanal.py.
# 2. Esta vez, se podrán crear varias listas; el usuario del programa especificará cuántas.
# 3. La longitud de cada lista la definirá el usuario.
# 4. Imprime las listas e indica que son las originales. 
# 5. Se eliminarán los elementos de una lista que estén también en las listas posteriores. 
# 6. Imprime las listas indicando que se eliminaron los elementos que estaban, también, 
# en las listas posteriores.

import m_retosemanal as fn

lista1 = []  
acumulado = []
listaOriginal = []
norepetidos = []
contador=1
nodeListas=int(input('Escribe el número de listas: '))
for i in range(nodeListas):
    elementos = int(input(f'Cuantos elementos tendra la lista número {contador-1}: '))
    if elementos < 1:
        print('elementos insuficientes')

    else:
        for i in range(elementos):
            nombres = input(f'dime nombres {i + 1}: ')
            lista1 += [nombres]
            lista= fn.crear_listas(lista1,nombres)
            acumulado.append(nombres)
            noRepetidos = set(acumulado)
            listaOriginal.append(nombres)
            si= fn.comparar_listas(lista1,nombres) 
            contador+=1        
        print(f'La lista número {contador-1} es: {lista1}')
        
print('----------------------------------------------------------------------------------------------')
print(f'Los elementos de las listas originales son: {listaOriginal}')
print(f'Los elementos no repetidos son: {norepetidos}')