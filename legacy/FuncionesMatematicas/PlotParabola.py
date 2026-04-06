'''
@author taicoding
Graficas de funciones trigonometricas: Parabola 👩🏻‍🏫👩🏻‍💻
'''
'''
Importamos 'matplotlib.pyplot' para generar graficas y 
'numpy' realizar operaciones matematicas de alto nivel
'''
import matplotlib.pyplot as plt
import numpy as np
# Vamos a definir las variables a utilizar
'''
En 'x' vamos a definir un vector con valores que van del
-100 a 100 con incremento de 1 utilizando la funcion 
'arange(inicio,fin,incremento)'
'''
x = np.arange(-100,100,1)
#En 'y' definimos ax**2+bx+c con a=1, b=1 y c=0
y = x**2 + x
# uwu vengase la parabola
'''
Agregamos el par de vectores ('x', 'y') al grafico
con la funcion plot 
'''
plt.plot(x,y)
# Con la funcion xlabel asignamos la descripcion al eje x
plt.xlabel('x de -100 a 100')
# Con la funcion ylabel asignamos la descripcion al eje y
plt.ylabel('f(x)=ax**2+bx+c')
# Con title establecemos el titulo de nuestro grafico
plt.title('Grafico de una parabola \n con a=1, b=1 y c=0 ')
# Desplegamos el grafico con la funcion 'show' de pyplot
plt.show()



