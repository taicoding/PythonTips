'''
@author Tai543
Sentencias condicionales: if
'''
'''
Vamos a crear un pequeño algoritmo que imprima el 
mensaje 'Si existe' cuando encuentre el valor de la 
variable subcadena dentro del valor de la variable 
cadena, en el caso contrario debe imprimir 'No existe'
'''
#Definimos nuestras variables
sub_cadena ='uwu'
cadena ='hola soy una uwu cadena'
#Almacenamos la busqueda de la subcadena
hay_uwu = cadena.find(sub_cadena)
#Definimos la condicional
if hay_uwu > -1:
    print('Si existe')
else:
    print('No existe')
#Resultado: Si existe
