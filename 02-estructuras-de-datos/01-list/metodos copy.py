"""
@author taicoding
Metodos de Listas 🐍 Parte II
"""
# Lista inicial
emociones = ["uwu", "o_o", "e_e", "owo"]
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
