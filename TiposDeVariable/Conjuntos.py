'''
@author Tai543
Tipos de Variables: Conjuntos
Los conjuntos son estructuras de datos y un tipo 
de dato equivalentes a los conjuntos matematicos
'''
# En un conjunto podemos almacenar cadenas
meses = {'Enero','Febrero','Marzo','Abril'}
print(type(meses))
# Resultado: <class 'set'>
# Tambien podemos almacenar numeros enteros 
# y de punto flotante
edades = {15, 16, 17.7, 56, 26, 17, 20.5, 15}
print(type(edades))
# Resultado: <class 'set'>
# Incluso los anteriores tipos de datos en 
# una solo conjunto
mixto = {'Febrero', 29, 6.5}
print(type(mixto))
# Resultado: <class 'set'>
''' 👩🏻‍💻👩🏻‍🏫
Los elementos de un conjunto no estan ordenados
y pueden modificarse y añadirse mas elementos
'''
