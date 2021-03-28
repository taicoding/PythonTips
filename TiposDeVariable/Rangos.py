'''
@author Tai543
Tipos de Variables: Rangos
Los rangos son tipos de datos que nos permiten representar 
secuencias de numeros inmutables
'''   
# Existen dos notaciones para definir rangos 
# 'range(fin)' y 'range(inicio,fin,salto)'
# 'inicio' -- numero inicial del segmento 👩🏻‍🏫
# 'fin' -- numero final del segmento - 1 👩🏻‍💻
# 'salto' -- incremento entre numeros (opcional)
# Si usamos la primera notacion el inicio por defecto es 0
numeros = range(11) 
print(numeros , list(numeros))
# Resultado: range(0, 11) [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Ahora generemos otra secuencia que vaya del 1 al 10
numeros = range(1,11)
print(numeros , list(numeros))
# Resultado: range(1, 11) [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Para terminar generemos solo multiplos de 3 
numeros = range(3,11,3)
print(numeros , list(numeros))
# Resultado: range(3, 11, 3) [3, 6, 9]