'''
@author Tai543
Tipos de Variables: Listas
Las listas son estructuras de datos y 
un tipo de dato muy util en Python
'''
# En una lista podemos almacenar cadenas
meses = ['Enero','Febrero','Marzo','Abril']
print(type(meses))
# Resultado: <class 'list'>
# Tambien podemos almacenar numeros enteros 
# y de punto flotante
edades = [15, 16, 17.7, 56, 26, 17, 20.5, 15]
print(type(edades))
# Resultado: <class 'list'>
# Al igual que otras listas
pares = [[0,0] , [10,15] , [17,23] , [25,40]]
print(type(pares))
# Resultado: <class 'list'>
# Incluso los anteriores tipos de datos en 
# una sola lista
lista = ['Febrero', [28,29] , 29, 6.5]
print(type(lista))