#El programa que desarrollarás debe tener las siguientes características: \
# 1. Que en un bucle infinito solicite al usuario una letra (debes especificar \
# al usuario la condición para terminar el programa. Por ejemplo, para salir, \
# escriba alto, presione 0 o cualquier otra que se te ocurra).2. Harás una función \
# que imprima en la pantalla la letra siguiente en el alfabeto y la letra anterior\
#  a la ingresada.3. El programa debe continuar en el bucle hasta que el usuario \
# decida salir del programa

def calcularletras(n1, n2, n3):
    return (n1, n2, n3)

resp =True
while resp != 0:
    n2 = input('dime una letra: ').lower()
    lista=('abcdefghijklmnopqrstuvwxyza')
    let = lista.index(n2)
    n1= (lista[let-1])
    n3= (lista[let+1])
    letras = calcularletras(n1, n2, n3)
    print(letras)
    resp = int(input('escribe (1)= para seguir activo o (0) para cerrar el programa: '))
    if resp == 0:
        print('fin del programa')
        break
