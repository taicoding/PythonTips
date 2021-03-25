'''
@author Tai543
Conjuntos
Vamos a graficar el numero de elementos en 
comun entre dos conjuntos en un diagrama de Venn
'''
# Primero vamos a importar dos librerias
# 'matplotlib_venn' para generar los circulos del 
# diagrama de Venn 
from matplotlib_venn import venn2
# 'matplotlib.pyplot' para mostrar la grafica
import matplotlib.pyplot as plt
# En 'conjunto_a' definimos nuestro 
# primer conjunto usando solo {} <- llaves
conjunto_a={'P','O','L','Y','G','O','N','S'}
# En 'conjunto_b' definimos nuestro segundo conjunto 
# de otra forma 👩🏻‍🏫👩🏻‍💻 usando 'set()' y una lista
conjunto_b=set(['P','Y','T','H','O','N'])
# Con la funcion 'venn2' listamos los conjuntos 
# para graficar su interseccion 
venn2([conjunto_a, conjunto_b])
# Finalmente mostramos el grafico con 'plt.show()'
plt.show()