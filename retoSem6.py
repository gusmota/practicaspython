"""" 
1. Solicitar una contraseña que inicie con un número
2. que pida ingresar nuevamente la contraseña y verificar que coincida con la primera ingresada
3. si se cometen 3 errores al ingresar la contraseña, que despliegue un mensaje de aviso y cierre el programa       

cont =1
usuario = str(input('escribe la contraseña iniciando con un número: '))  # Solicitar una contraseña que inicie con un número
while usuario[0] not in ['1','2','3','4','5','6','7','8','9','0']:
   usuario = str(input('escribe la contraseña iniciando con un número: '))
   
usu1 = str(input('ingresa nuevamente la contraseña (máx 3 intentos): ')) # que pida ingresar nuevamente la contraseña y verificar que coincida con la primera ingresada
while usuario != usu1:
        usu1 = str(input('ingresa nuevamente la contraseña (sólo 3 intentos): '))
        cont = cont+1
        while usuario ==usu1 and cont <=3:
            print('la contraseña es correcta')
        else:
            print('se han hecho 3 intentos, se cierra el programa') # si se cometen 3 errores al ingresar la contraseña, que despliegue un mensaje de aviso y cierre el programa
            break


            """
def saludo():
    print('hola amiga')
    return
saludo()


