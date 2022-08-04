"""
Hacer un diccionario con colores de arcoíris (rojo, naranja, amarillo, verde, azul, violeta), en dos idiomas diferentes
Indicar cuales son los dos idiomas a los que se puede traducir el programa
El usuario debe elegir a cual de los idiomas quiere traducir
Al ingresar la frase en español que incluya un color, debe desplegar en la pantalla como se dice en el idioma seleccionado
"""
diccionario = {'red' : 'rojo' ,'orange' : 'naranja' ,'yellow' : 'amarillo' ,'green' : 'verde' ,'blue' : 'azul' ,\
    'violet' : 'violeta' ,'rojo' : 'red' ,'naranja' : 'orange' ,'amarillo' : 'yellow' ,'verde' : 'green' ,\
        'azul' : 'blue' ,'violeta' : 'violet', 'red' : 'roja','yellow' : 'amarilla'}

print('El programa puede traducir inglés-español o viceversa')
idioma = input('selecciona el idioma (ingles = i o español = e): ')
traduc = input('escribe la frase incluyendo un color del arcoiris: ')
palabras = traduc.split()

respuesta = ' '
for palabra in palabras:
    if palabra in diccionario:
        respuesta = diccionario[palabra]

print('la traducción es: ' + respuesta)