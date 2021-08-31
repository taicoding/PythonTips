'''
@author taicoding
Listas: Segmentacion
La segmentacion es una propiedad muy cool de las 
listas en python 😎👩🏻‍🏫👩🏻‍💻 para usarla solo tenemos 
que seguir la siguiente notacion '[inicio:fin]' 
'inicio' --  indice donde inicia el segmento
'fin' -- indice donde finiliza el segmento + 1
'''    
# Vamos a definir la lista 'python'  
python = ['P','Y','T','H','O','N']
print(python)
# Resultado: ['P', 'Y', 'T', 'H', 'O', 'N']
# Vamos a mostrar solo los dos primeros elementos 
# de la lista 'python' para esto el indice de 
# 'inicio' sera 0 y indice de 'fin' sera 2 '[0:2]'
print(python[0:2])
# Resultado: ['P', 'Y']
# Como el indice de 'inicio' es 0 tambien podemos 
# mostrar los elementos de la siguiente forma '[:2]'
print(python[:2])
# Resultado: ['P', 'Y']
