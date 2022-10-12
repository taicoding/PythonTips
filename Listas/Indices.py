"""
@author taicoding
¿Cómo funcionan los índices de las listas? 🐍
"""
# Definamos la lista 'python'
python = ["P", "Y", "T", "H", "O", "N"]
# Los indices de los elementos de la lista
# 'python' se pueden leer de las siguientes formas
"""
+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+           indices
| 0 | 1 | 2 | 3 | 4 | 5 | <<-- izquierda a derecha
+---+---+---+---+---+---+           indices
|-6 |-5 |-4 |-3 |-2 |-1 | <<-- derecha a izquierda
+---+---+---+---+---+---+
"""
# Mostremos el primer elemento de la lista 'python'
# usando ambos tipos de indices 😎👩🏻‍🏫👩🏻‍💻
print(python[0])
# Resultado: P
print(python[-6])
# Resultado: P

"""
@author taicoding
"""
from datetime import date

if str(date.today()) == "2022-09-13":
    print("¡Feliz día del programador!")
    print("¡Feliz día de la programadora!")
