"""
@author taicoding
Listas: Segmentacion III
"""
# En 'emociones' vamos a definir una lista
emociones = list(["u_u", "uwu", "o_o", "uwu"])
print(emociones)
# Resultado: ['u_u', 'uwu', 'o_o', 'uwu']
# Ahora vamos a dividir esta lista en dos
# Encontramos la cantidad de elementos de la lista
longitud = len(emociones)
# Con una division entera encontramos la mitad de la
# 'longitud'
medio = longitud // 2
# Utilizando la sergmentacion delimitamos
# las dos mitades de nuesta lista
una_mitad = emociones[:medio]
otra_mitad = emociones[medio:]
print(una_mitad)
# Resultado: ['u_u', 'uwu']
print(otra_mitad)
# Resultado: ['o_o', 'uwu']
