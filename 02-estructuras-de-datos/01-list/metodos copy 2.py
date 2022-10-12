"""
@author taicoding
Metodos de Listas 🐍
"""
# Lista inicial
emociones = ["uwu"]
# ⭐️ Agregar un elemento ⭐️
# append(elemento)
emociones.append("owo")
print(emociones)
# R: ['uwu', 'owo']
# ⭐️ Tip: append es la forma mas rapida
"""
@author taicoding
Metodos de Listas 🐍
"""
# Lista inicial
emociones = ["uwu", "owo"]
# ⭐️ Agregar un elemento ⭐️
# insert(indice,elemento)
emociones.insert(1, "e_e")
print(emociones)
# R: ['uwu', 'e_e', 'owo']
"""
@author taicoding
Metodos de Listas 🐍
"""
# Lista inicial
emociones = ["uwu", "e_e", "owo"]
# concatenacion de listas
emociones = emociones + ["o_o"]
print(emociones)
# R: ['uwu', 'e_e', 'owo', 'o_o']
"""
@author taicoding
Metodos de Listas 🐍
"""
# Lista inicial
emociones = ["uwu", "o_o", "e_e", "owo"]
# ⭐️ Remueve un elemento ⭐️
# remove(elemento)
emociones.remove("o_o")
print(emociones)
# R: ['uwu', 'e_e', 'owo']
"""
@author taicoding
Metodos de Listas 🐍
"""
# Lista inicial
emociones = ["uwu", "e_e", "owo"]
# ⭐️ Revertir la Lista ⭐️
emociones.reverse()
print(emociones)
# R: ['owo', 'e_e', 'uwu']
"""
@author taicoding
Metodos de Listas 🐍
"""
# Lista inicial
emociones = ["owo", "e_e", "uwu"]
# ⭐️ Ordenar la Lista ⭐️
emociones.sort()
print(emociones)
# R: ['e_e', 'owo', 'uwu']
"""
@author taicoding
Metodos de Listas 🐍
"""
# Lista inicial
emociones = ["e_e", "owo", "uwu"]
# ⭐️ Indice de un elemento ⭐️
# index(elemento)
i = emociones.index("owo")
print(i)
# R: 1
