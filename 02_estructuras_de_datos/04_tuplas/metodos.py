"""
@author taicoding
Métodos de Tuplas 🐍🧮
"""

# Definimos una tupla de calificaciones
calificaciones = (51, 70, 80, 51, 65)
# 🔢 Contar las apariciones de un elemento
# Método: count(elemento)
contador = calificaciones.count(51)
print(contador)
# 🖨️ Resultado: 2

# 🔍 Obtener el indice de un elemento
# Método: index(elemento)
indice = calificaciones.index(70)
print(indice)
# 🖨️ Resultado: 1

# 📍 Obtener el indice de un elemento
# en un intervalo específico 🔛
# Método:  index(elemento, inicio, fin)
indice = calificaciones.index(51, 2, 5)
print(indice)
# 🖨️ Resultado: 3
