# crear un programa Que permita crear dos listas de distintas longitudes.
# ● Que la longitud y los elementos de cada lista sean especificados por el usuario.
# ● Que imprima las listas indicando que son las listas originales.
# ● Que elimine de la primera lista los nombres de la segunda.
# ● Que imprima la primera lista indicando que se han eliminado los elementos que estaban 
# también en la segunda.

def nombresRep(n1, n2):
    return (n1,n2)
'''guarda los valores introducidos por el usuario'''

numero = int(input('Cuantos elementos tendra la primera lista: '))

if numero < 1:
    print('elementos insuficientes')
else:
      primera = []
      for i in range(numero):
          palabra = input(f'dime nombre {i + 1}: ')
          primera += [palabra]
      print(f'La primera lista es: {primera}')

      for i in range(len(primera) - 1, -1, -1):
          if primera[i] in primera[:i]:
              del primera[i]

      numero2 = int(input('Cuántos nombres tendra la segunda lista: '))

      if numero2 < 1:
          print('elementos insuficientes')
      else:
          segunda = []
          for i in range(numero2):
              palabra = input(f'dime nombre {i + 1}: ')
              segunda += [palabra]
          print(f'La segunda lista es: {segunda}')

          for i in range(len(segunda) - 1, -1, -1):
              if segunda[i] in segunda[:i]:
                  del segunda[i]

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
