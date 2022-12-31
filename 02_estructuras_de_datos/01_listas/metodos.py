"""
@author taicoding
Métodos de Listas 🐍
"""
# Lista inicial
emociones = ["uwu"]
# ⭐️ Agregar un elemento ⭐️
# append(elemento)
emociones.append("owo")
print(emociones)
# R: ['uwu', 'owo']
# ⭐️ Tip: append es la forma mas rápida

# ⭐️ Agregar un elemento ⭐️
# insert(indice,elemento)
emociones.insert(1, "e_e")
print(emociones)
# R: ['uwu', 'e_e', 'owo']

# concatenación de listas
emociones = emociones + ["o_o"]
print(emociones)
# R: ['uwu', 'e_e', 'owo', 'o_o']

# ⭐️ Remueve un elemento ⭐️
# remove(elemento)
emociones.remove("o_o")
print(emociones)
# R: ['uwu', 'e_e', 'owo']

# ⭐️ Revertir la Lista ⭐️
emociones.reverse()
print(emociones)
# R: ['owo', 'e_e', 'uwu']

# ⭐️ Ordenar la Lista ⭐️
emociones.sort()
print(emociones)
# R: ['e_e', 'owo', 'uwu']

# ⭐️ Indice de un elemento ⭐️
# index(elemento)
i = emociones.index("owo")
print(i)
# R: 1
