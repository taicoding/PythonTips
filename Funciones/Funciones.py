'''
@author Tai543
Funciones
¿Que es un Funcion?
Una funcion es un bloque de codigo que se ejecuta
una vez que la funcion es llamada
'''
# Para definir una funcion utilizamos la palabra reservada 
# 'def' y le ponemos un nombre a la funcion en este caso 
# 'soy_una_funcion'
def soy_una_funcion():
    # Este es el bloque de codigo que se ejecutara cuando 
    # llamemos a la funcion   
    print('Hola soy una funcion')
# Para ejecutar la funcion solo citamos su nombre 
soy_una_funcion()
# Rasultado: Hola soy una funcion
# Las funciones tambien puede recibir parametros
def imprime_mensaje(mensaje):
    print(mensaje)
# Definimos un cadena con nuestro mensaje
cadena='Python es muy cool :)'
# Enviamos nuestra 'cadena' como parametro a 
# la funcion 'imprime_mensaje'
imprime_mensaje(cadena)
# Rasultado: Python es muy cool :)
