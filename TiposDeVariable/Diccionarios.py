'''
@author Tai543
Tipos de Variables: Diccionarios
Los diccionarios son estructuras de datos y un tipo de 
dato que nos permite almacenar cualquier tipo de dato
'''
# Para definir los elementos de un diccionario utilizamos 
# el formato 'llave:valor' donde cada 'llave' es unica
instagram = {'nombre':'Tai543','edad':'27'
            ,'progreso':0.5
            , 'seguidores':['uwu'
                            ,'sin'
                            ,'ewe']}
print(type(instagram))
# Resultado: <class 'dict'>
# Vamos a acceder al valor de la llave 'nombre'
# de nuestro diccionario
print(instagram['nombre']) 
# Resultado: Tai543
# Ahora vamos a acceder al valor de la llave 'seguidores'
print(instagram['seguidores']) 
# Resultado: ['uwu', 'sin', 'ewe']