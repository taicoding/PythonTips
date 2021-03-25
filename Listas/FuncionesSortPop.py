'''
@author Tai543
Funciones de Listas
Veamos funciones utiles para manejar listas
'''
# En 'emociones' vamos a definir una lista vacia 
# con la clase 'list' esta es otra forma de 
# definir listas uwu
emociones = list()
print(emociones)
# Resultado: []
# Con la funcion 'append()' vamos a agregar tres 
# elementos a la lista 'emociones'
emociones.append('uwu')
emociones.append('ewe')
emociones.append('owo')
print(emociones)
# Resultado: ['uwu', 'ewe', 'owo']
# Con la funcion 'remove()' vamos a eleminar 
# el elementos 'ewe' de la lista 'emociones'
emociones.remove('ewe')
print(emociones)
# Resultado: ['uwu', 'owo']
# En 'numeros' vamos a definir una lista de 
# numeros
numeros = [1,5,3,6,9,4,25,8,19,2]
print(numeros)
# Resultado: [1, 5, 3, 6, 9, 4, 25, 8, 19, 2] 
# Con la funcion 'sort()' ordenamos la lista 
# 'numeros' de forma ascendente
numeros.sort()
print(numeros)
# Resultado: [1, 2, 3, 4, 5, 6, 8, 9, 19, 25]
# Con la funcion 'pop()' sacamos el ultimo 
# elemento de la lista 'numeros' y lo 
# almacenaremos en la variable 'elemento'
elemento = numeros.pop()
print(numeros)
# Resultado: [1, 2, 3, 4, 5, 6, 8, 9, 19]
print(elemento)
# Resultado: 25

