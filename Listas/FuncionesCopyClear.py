'''
@author Tai543
Funciones de Listas
Veamos funciones utiles para manejar listas
'''
# Vamos a definir la listas 'uwu'
uwu = ['uwu','sin','ewe']
# En la lista 'emociones' vamos a copiar la lista 
# 'uwu' usando el la funcion 'copy()'
emociones = uwu.copy()
print(emociones)
# Resultado: ['uwu', 'sin', 'ewe']
# Vamos a vaciar la lista emociones con la funcion 
# 'clear()' y veremos que paso con la lista 'uwu'
emociones.clear()
print(emociones)
# Resultado: []
print(uwu)
# Resultado: ['uwu', 'sin', 'ewe']
# 🛑👩🏻‍🏫 Al usar la funcion 'copy()' ambas listas 
# son independientes lo que quiere decir que 
# cualquier cambio que sufra una no afecta a 
# la otra 👩🏻‍💻🛑
