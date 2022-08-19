resp =True
while resp != 0:
   entrada = input('dime una letra: ')
   lista=('abcdefghijklmnopqrstuvwxyz')
   resp = int(input('escribe (1)= para seguir activo o (0) para cerrar el programa: '))
   let = lista.index(entrada)
   ant = lista[let-1]
   sig = lista[let+1]
   print(ant, entrada, sig)
   if resp == 0:
    break
print('fin del programa')
