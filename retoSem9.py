#El programa que desarrollarás debe tener las siguientes características: \
# 1. Que en un bucle infinito solicite al usuario una letra (debes especificar \
# al usuario la condición para terminar el programa. Por ejemplo, para salir, \
# escriba alto, presione 0 o cualquier otra que se te ocurra).2. Harás una función \
# que imprima en la pantalla la letra siguiente en el alfabeto y la letra anterior\
#  a la ingresada.3. El programa debe continuar en el bucle hasta que el usuario \
# decida salir del programa

resp =True
while resp != 0:
   entrada = input('dime una letra: ').lower()
   lista=('abcdefghijklmnopqrstuvwxyz')
   resp = int(input('escribe (1)= para seguir activo o (0) para cerrar el programa: '))
   let = lista.index(entrada)
   ant = lista[let-1]
   sig = lista[let+1]
   print(ant, entrada, sig)
   if resp == 0:
    break
print('fin del programa')

####################################################################################333

resp =True
while resp != 0:
   entrada = input('dime una letra: ').lower()
   lista=('abcdefghijklmnopqrstuvwxyz')
   resp = int(input('escribe (1)= para seguir activo o (0) para cerrar el programa: '))
   let = lista.index(entrada)
   def ant():
    ant = lista[let-1]
   def sig():
    sig = lista[let+1]
   print(ant, entrada, sig)
   if resp == 0:
    break
print('fin del programa')
