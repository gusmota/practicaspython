# crear un programa Que permita crear dos listas de distintas longitudes.
# Que la longitud y los elementos de cada lista sean especificados por el usuario.
# Que imprima las listas indicando que son las listas originales.
# Que elimine de la primera lista los nombres de la segunda.
# Que imprima la primera lista indicando que se han eliminado los elementos que estaban 
# también en la segunda.

# .... DEFINE FUNCIONES ...............................................
def crea_lista(elementos):
    lista = []
    for i in range(elementos):
        palabra = input(f'dime nombre {i + 1}: ')
        lista += [palabra] # doble punto
    #print(f'La primera lista es: {primera}')
    return lista

def elimina_elementos(lista1, lista2):
    comunes = []
    for i in primera:
        if i in segunda:
            comunes += [i]
    print(f'nombres que se repiten en las dos listas: {comunes}')

    soloPrimera = []
    for i in primera:
        if i not in segunda:
            soloPrimera += [i]
    print(f'nombres que sólo aparecen en la primer lista: {soloPrimera}')

    soloSegunda = []
    for i in segunda:
        if i not in primera:
            soloSegunda += [i]
    print(f'nombres que sólo aparecen en la segunda lista: {soloSegunda}')

    todas = comunes + soloPrimera + soloSegunda
    nombresRep = todas
        
    print(f'todos los nombres {nombresRep}')

    return soloPrimera


def nombresRep(n1, n2):
    return (n1,n2)
'''guarda los valores introducidos por el usuario'''



# .... DEFINE EL PROGRAMA ...............................................


numero = int(input('Cuantos elementos tendra la primera lista: '))

### DRY - Don't Repeat Yourself ###
### DOT - Do one thing ###

# validación
if numero < 1:
    print('elementos insuficientes')
else:
    #llamo la función
    primera = crea_lista(numero)
    print(f'La primera lista es: \n {primera}')

numero2 = int(input('Cuántos nombres tendra la segunda lista: '))

if numero2 < 1:
    print('elementos insuficientes')
else:
    segunda = crea_lista(numero2)
    print(f'La segunda lista es: \n {segunda}')

lista_unica = elimina_elementos(primera, segunda)

