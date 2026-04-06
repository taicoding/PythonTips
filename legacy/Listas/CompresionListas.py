'''
@author taicoding
Listas: Comprension 
'''
'''
¿Como recorrer una lista en una sola linea 
y aplicar alguna operacion a sus elementos?
👩🏻‍🏫👩🏻‍💻 Podemos hacerlo aplicando compresion 
de listas con la siguiente estructura 👩🏻‍🏫👩🏻‍💻
[<operacion> for <elemento> in <lista>]
'''
# Definamos una lista de numeros
numeros = list([1,3,5,7,9,11])
# Vamos a elevar todos los valores de la 
# lista al cuadrado
al_cuadrado = [n**2 for n in numeros]
# Esto genera una nueva lista
print(al_cuadrado)
# Resultado: [1, 9, 25, 49, 81, 121]

