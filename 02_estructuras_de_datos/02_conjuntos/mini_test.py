"""
@author taicoding
Tema: Sets 🐍🍟
¿Cuál es el resultado? 👩🏻‍🏫👩🏻‍💻🐍
"""

fibonacci = {0, 1, 1, 2, 3}
impares = {1, 3, 5, 7}
pares = {2, 4, 6, 8}
interseccion = fibonacci.intersection(pares)
resultado = impares.difference(interseccion)
print(resultado)
