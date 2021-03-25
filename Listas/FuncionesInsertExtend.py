'''
@author Tai543
Funciones de Listas
Veamos funciones utiles para manejar listas
'''
# Vamos a definir dos listas de numeros
pares = [2,6,8,10]
numeros = list([1,3,5,7,9])
# Vamos a agregar un 4 despues del 2 es decir 
# en la posicion 1 en la lista 'pares' usando 
# la funcion 'insert(posicion, elemento)' 
# 👩🏻‍🏫👩🏻‍💻🛑 Las listas empiezan en la posicion 0
pares.insert(1,4)
print(pares)
# Resultado: [2, 4, 6, 8, 10]
# Ahora que los pares estan completos agregaremos 
# todos los elementos de la lista 'pares' a la 
# lista 'numeros' con la funcion 'extend()'
numeros.extend(pares)
print(numeros)
# Resultado: [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
# Ordenemos la lista para que se vea mas cool 😎
numeros.sort()
print(numeros)
# Resultado: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]