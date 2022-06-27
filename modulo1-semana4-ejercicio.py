# quiero declarar una variable, = numero de huevos
numHuevos = 12

# print("tengo" + numHuevos + "huevos")

#comoo solucionar el problema anteior? 

#opción 1
print("Tengo " + str(numHuevos) + " huevos")

#opción 2
print("Tengo %s huevos." %(numHuevos))
##################################################
#Calcular la superficie o área del cuadrado

lado = int (input("Ingrese la medida del lado del cuadrado : "))
superficie = lado * lado
print("La superficie del cuadrado es: " + str(superficie))

#ejercicio de la semana: hacer un formulario simple 
nombre = input("Instroduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
Edad = int(input("Introduce tu edad: "))
Correo = input("Introduce tu correo electrónico: ")
Telefono = input("Introduce tu teléfono: ")

print("Nombre: " + nombre)
print("Apellido: " + apellido)
print("Edad: " + str(Edad))
print("Correo: " + Correo)
print("Telefono: " + Telefono)






