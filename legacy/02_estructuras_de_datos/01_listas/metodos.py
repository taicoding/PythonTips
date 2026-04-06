"""
@author taicoding
Métodos para agregar elementos a una Lista 🐍📜
"""

# Declaramos una lista de emociones
emociones = ["😊"]
# 📂 Agregar una nueva emoción al final de la lista
# Método: append(elemento)
emociones.append("😢")
print(emociones)
# 🖨️ Resultado: ['😊', '😢']
# 📂 Agregar una nueva emoción en una posición
# especifica de la lista
# Método: insert(posición,elemento)
emociones.insert(1, "😵")
print(emociones)
# 🖨️ Resultado: ['😊', '😵', '😢']
# 🧩 Agregar emociones utilizando otro iterable
# Un iterable puede ser una lista, tupla, cadena, etc.
# Método: extend(lista)
emociones.extend({"😄", "😍"})
print(emociones)
# 🖨️ Resultado: ['😊', '😵', '😢', '😍', '😄']
# 🧩 Agregar una emoción concatenando dos listas
emociones = emociones + ["😢"]
print(emociones)
# 🖨️ Resultado: ['😊', '😵', '😢', '😍', '😄', '😢']
# ⭐️ Tip: El método append es el mas rápido

# Declaramos una lista de emociones
emociones = ["😊", "😵", "😍", "😄", "😢"]
# 🗑️ Remover un elemento de la Lista
# Método: remove(elemento)
emociones.remove("😢")
print(emociones)
# 🖨️ Resultado: ['😊', '😵', '😍', '😄']
# 🔄 Revertir los elementos de la Lista
# Método: reverse()
emociones.reverse()
print(emociones)
# 🖨️ Resultado: ['😄', '😍', '😵', '😊']
# 📊 Ordenar los elementos de la Lista
# Método: sort()
emociones.sort()
print(emociones)
# 🖨️ Resultado: ['😄', '😊', '😍', '😵']
# 🔍 Obtener el indice de un elemento
# Método: index(elemento)
indice = emociones.index("😍")
print(indice)
# 🖨️ Resultado: 2
