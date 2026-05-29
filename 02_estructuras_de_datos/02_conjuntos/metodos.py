"""
@author taicoding
Métodos de Conjuntos 🐍🍟
"""

# Definimos un conjunto de frutas
postres = {"🍰", "🍪"}
# 🧩 Agregar un elemento al conjunto
# Método: add(elemento)
postres.add("🍦")
print(postres)
# 🖨️ Resultado: {'🍪', '🍦', '🍰'}
# 🗑️ Remover un elemento del conjunto
# Método: discard(elemento)
postres.discard("🍪")
print(postres)
# 🖨️ Resultado: {'🍰', '🍦'}
# 🛒 Unir dos conjuntos
# Método: union(set)
helados = {"🍦", "🍨"}
union = postres.union(helados)
print(union)
# 🖨️ Resultado: {'🍰', '🍦', '🍨'}
# 💫 Encontrar la intersección entre
# dos conjuntos
# Método: intersection(set)
interseccion = postres.intersection(helados)
print(interseccion)
# 🖨️ Resultado: {'🍦'}
# 🔗 Encontrar la diferencia entre
# dos conjuntos
# Método: difference(set)
diferencia = postres.difference(helados)
print(diferencia)
# 🖨️ Resultado: {'🍰'}
# 🖇️ Verificar si dos conjuntos
# son disjuntos
# Método: isdisjoint(set)
disjuntos = postres.isdisjoint(helados)
print(disjuntos)
# 🖨️ Resultado: False
# 📚 Verificar si un conjunto es
# subconjunto de otro
# Método: issubset(set)
subconjunto = postres.issubset(union)
print(subconjunto)
# 🖨️ Resultado: True
# 🗂️ Verificar si un conjunto es
# superconjunto de otro
# Método: issuperset(set)
superconjunto = union.issuperset(helados)
print(superconjunto)
# 🖨️ Resultado: True
# 🧨 Eliminar todos los elementos de
# un conjunto
# Método: clear()
postres.clear()
print(postres)
# 🖨️ Resultado: set()
