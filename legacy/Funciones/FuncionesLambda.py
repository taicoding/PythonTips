'''
@author taicoding
Funciones Lambda
Es un tipo de funcion anonima que puede 
tomar varios argumentos y evaluarlos en 
una sola expresion. Se expresa como:
'lambda argumentos : expresion'
'''
# Vamos a expresar la funcion de una parabola
y = lambda x : x**2
print(y(5))
# Resultado: 25
# Vamos a usar dos argumentos para calcular 
# el IMC
imc = lambda peso , altura : peso/altura**2
print(imc(65,1.64))
# Resultado: 24.167162403331353
# Tambien podemos usar cadenas
uwu = lambda cadena : cadena + ' uwu'
print(uwu('Hola'))
# Resultado: Hola uwu