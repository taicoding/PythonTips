"""
@author taicoding
Métodos de Tuplas 🐍
"""
# Tupla inicial
calificaciones = (2, 7, 8, 2, 5, 4, 2)
# ⭐️ Contar las apariciones de un elemento ⭐️
# count(elemento)
contador = calificaciones.count(2)
print(contador)
# R: 3
"""
@author taicoding
Métodos de Tuplas 🐍
"""
# ⭐️ Obtener el indice de un elemento ⭐️
# index(elemento)
indice = calificaciones.index(7)
print(indice)
# R: 1
"""
@author taicoding
Métodos de Tuplas 🐍
"""
# ⭐️ Obtener el indice de un elemento
# en un intervalo ⭐️
# index(elemento, inicio, fin)
indice = calificaciones.index(2, 2, 5)
print(indice)
# R: 3
