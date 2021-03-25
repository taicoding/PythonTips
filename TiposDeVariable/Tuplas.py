'''
@author Tai543
Tipos de Variables: Tuplas
Las tuplas son tipos de dato parecidos a las listas.
Podemos almacenar en ellas cualquier tipo de dato
'''
# Podemos almacenar cadenas
cadenas = ('Hola','soy','una','tupla')
print(type(cadenas))
# Resultado: <class 'tuple'>
# Podemos almacenar numero enteros o de . flotante
numeros = (2, 2.5, 2.8, 3, 1000, 580)
print(type(numeros))
# Resultado: <class 'tuple'>
# Podemos almacenar listas 
listas = (['soy','estatica'] , [1,1])
print(type(listas))
# Resultado: <class 'tuple'>
'''
🛑🛑🛑 Las tuplas son estaticas, esto quiere decir 
que NO podemos agregar, ni modificar elementos 
despues de definirlas 🛑🛑🛑
'''