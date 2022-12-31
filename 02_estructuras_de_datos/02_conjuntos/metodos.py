"""
@author taicoding
Métodos de Sets 🐍
"""
# Conjunto inicial
frutas = {"fresa", "sandia"}
# ⭐️ Agregar un elemento ⭐️
# add(elemento)
frutas.add("uva")
print(frutas)
# R: {'sandia', 'fresa', 'uva'}
# ⭐️ Remover un elemento especifico ⭐️
# discard(elemento)
frutas.discard("uva")
print(frutas)
# R: {'sandia', 'fresa'}
# ⭐️ Diferencia entre dos conjuntos ⭐️
# set.difference(set)
bayas = {"fresa", "mora"}
print(bayas.difference(frutas))
# R: {'mora'}
