"""
Hacer un programa que cree una lista de hasta 10 alumnos, que capture el nombre, tres calificaciones o mínimo una \
mostrar una linea por cada alumno con su calificacion promedio
"""""
lista = []
alumnos = 0
while alumnos <= 10:
    opcion = input ('Agregar alumno (1) o terminar (2): ')
    if opcion == '1':
        nombre = input ('Ingrese el nombre del alumno: ').capitalize()
        calif1 = int(input(f'Ingrese la primera calificacion de {nombre}: '))
        calif2 = int(input(f'Ingrese la segunda calificacion de {nombre}: '))
        calif3 = int(input(f'Ingrese la tercera calificacion de {nombre}: '))
        cal = [int(calif1), int(calif2),int(calif3)]
        promCal = sum(cal)/float(len(cal))
        alumno = [nombre, promCal]
        lista.append(alumno)
        alumnos += 1
    elif opcion == '2':
        print(f'Fin del programa con {alumnos} alumnos ')
        break
    else:
        print('Opción inválida')
        continue 
print('Esta es la lista de calificaciones por alumno: ')
for i in lista:
    print(i, end='')
    print()