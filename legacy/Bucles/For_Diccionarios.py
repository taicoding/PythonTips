'''
@author taicoding
Tipos de Variables: Diccionarios II
Tenemos nuestro diccionario 'instagram' vamos a mostrar 
todos los valores de las llaves linea por linea
'''
instagram = {'nombre':'taicoding','edad':'27'
            ,'progreso':0.5
            , 'seguidores':['uwu'
                            ,'sin'
                            ,'ewe']}
# Con ayuda de un 'for' vamos a recorrer cada uno de 
# los valores del diccionario utilizando un par de 
# variables: 'llave' y 'valor'
for llave,valor in instagram.items():
# En la primera variable tendremos el nombre de la 
# llave y en la segunda variable tendremos el valor 
# correspondiente a la llave
    print(str(llave)+':'+str(valor))
# Resultado:
# nombre:taicoding
# edad:27
# progreso:0.5
# seguidores:['uwu', 'sin', 'ewe']