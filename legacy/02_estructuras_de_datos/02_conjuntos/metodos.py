"""
@author taicoding
Métodos de Conjuntos 🐍🍟
"""

# Definimos un conjunto de frutas
frutas = {"🍓", "🍉"}
# 🧩 Agregar un elemento al conjunto
# Método: add(elemento)
frutas.add("🍋")
print(frutas)
# 🖨️ Resultado: {'🍋', '🍓', '🍉'}
# 🗑️ Remover un elemento al conjunto
# Método: discard(elemento)
frutas.discard("🍋")
print(frutas)
# 🖨️ Resultado: {'🍓', '🍉'}
# 🔗 Encontrar la diferencia entre dos conjuntos
# Método: difference(set)
bayas = {"🍓", "🍒"}
print(bayas.difference(frutas))
# 🖨️ Resultado: {"🍒"}
# 🔘 Unir dos conjuntos
# Método: union(set)
frutas = frutas.union(bayas)
print(frutas)
# 🖨️ Resultado: {'🍒', '🍓', '🍉'}
