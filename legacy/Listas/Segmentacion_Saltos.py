'''
@author taicoding
Listas: Segmentacion y saltos
'''    
# Vamos a definir la lista 'numeros'  
numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros)
# Resultado: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Ahora seleccionaremos los numero pares de esta lista
# usando la siguiente notacion '[inicio,fin,salto]'
# 'inicio' -- indice donde inicia el segmento   👩🏻‍🏫
# 'fin' -- indice donde finiliza el segmento + 1👩🏻‍💻
# 'salto' -- incremento del indice en el recorrido 
print(numeros[1:11:2])
# Resultado: [2, 4, 6, 8, 10]
# Tambien podemos mostrar estos elementos de la
# siguiente forma '[1::2]'
print(numeros[1::2])
# Resultado: [8, 9, 10]

