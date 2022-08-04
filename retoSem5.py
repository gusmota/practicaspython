añoActual = int(input('dime el año actual: '))
añoCualquiera = int(input('dime un año cualquiera: '))
añosPasados = ((añoActual - añoCualquiera))
if añosPasados >= 2:
    print('Han pasado' , añosPasados , 'años desde el año que has introducido')
elif añosPasados <= -2:
    print('Faltan' , abs(añosPasados) , 'años para llegar al año que has introducido')
elif añoCualquiera == 2021:
    print('Desde el año ', añoCualquiera , 'ha pasado ',abs(añosPasados),' año')
elif añoCualquiera == 2023:
    print('Para llegar a ', añoCualquiera,'hace falta ',abs(añosPasados),' año')
else:
    if añoActual==añoCualquiera:
        print('Has introducido el mismo año que el actual')


