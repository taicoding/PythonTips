"""
@author taicoding
Listas
Dividir una lista en 2
"""
# En 'emociones' vamos a definir una lista
emociones = list(
    [
        "u_u",
        "uwu",
        "u.u",
        "o_o",
        "owo",
        "o.o",
    ]
)
print(emociones)
# Resultado: ['u_u', 'uwu', 'u.u', 'o_o', 'owo', 'o.o']
# Es muy facil divir una lista
# Primero encontramos

# Con la funcion 'count()' vamos a contar el numero
# de veces que 'uwu' aparece en la lista 'emociones'
nro_uwus = emociones.count("uwu")
print(nro_uwus)
# Resultado: 2
# Con la funcion 'index()' vamos a obtener la posicion
# de 'uwu' en la lista 'emociones'
posicion_uwu = emociones.index("uwu")
print(posicion_uwu)
# Resultado: 1
# 🛑 Si te diste cuenta tenemos 2 'uwu' en la lista 🛑
# Si los elementos de una lista se repiten la funcion
# 'index()' solo nos devolvera la posicion de la
# primera aparicion del elemento 👩🏻‍🏫👩🏻‍💻


"""
@author taicoding
Funciones de Listas
Veamos funciones utiles para manejar listas
"""
# Vamos a definir la listas 'awa'
awa = ["awa", "de", "uwu"]
# En la lista 'emociones' vamos a copiar la lista
# 'awa' usando el operador '='
emociones = awa
print(emociones)
# Resultado: ['awa', 'de', 'uwu']
# Vamos a revertir la lista emociones con la funcion
# 'reverse()' y veremos que paso con la lista 'awa'
emociones.reverse()
print(emociones)
# Resultado: ['uwu', 'de', 'awa']
print(awa)
# Resultado: ['uwu', 'de', 'awa']
# 🛑🙀 Oh no! ambas listas fueron modificadas
# Cuando usamos el operador '=' las lista
# involucradas se convierten en un espejo de
# la otra 👩🏻‍🏫👩🏻‍💻🛑
