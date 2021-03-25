'''
@author Tai543
Bucles: for
'''
'''
Tenemos la variable 'lista' y nos gustaria saber 
el tipo de variable de cada uno de sus elementos
¿Como podemos hacerlo?
'''
lista = ['Febrero', [28,29] , 29, 6.5]
# La estructura del bucle 'for' nos permite 
# recorrer uno a uno los elementos de una lista 
# de inicio a fin
for elemento in lista:
# Cada elemento de la lista sera almacenado en 
# la variable 'elemento', para cada elemento vamos 
# a imprimir el valor de la variable 'elemento' y su tipo de variable
    print(str(elemento) + ' ' + str(type(elemento)))
# Resultado: 
# Febrero <class 'str'>
# [28, 29] <class 'list'>
# 29 <class 'int'>
# 6.5 <class 'float'>