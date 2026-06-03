"""
@author taicoding
Diferencias entre
Estructuras de Datos en Python 🐍👩🏻‍🏫👩🏻‍💻
"""

# 🔒 Tuplas: almacenan datos que no cambian tras crearse
tupla = ("indexada", "inmutable", "ordenada")
print(type(tupla))
# 🖨️ Resultado: <class 'tuple'>
# 📝 Listas: almacenan datos que se pueden modificar
lista = ["indexada", "mutable", "ordenada"]
print(type(lista))
# 🖨️ Resultado: <class 'list'>
# 🔵 Conjuntos: almacenan datos únicos
# sin orden específico y no permiten duplicados
conjunto = {"no indexada", "mutable", "no ordenada"}
print(type(conjunto))
# 🖨️ Resultado: <class 'set'>
# 🗂️ Diccionarios: almacenan datos en pares clave-valor
diccionario = {"indexada": "✅", "mutable": "✅", "ordenada": "✅"}
print(type(diccionario))
# 🖨️ Resultado: <class 'dict'>
