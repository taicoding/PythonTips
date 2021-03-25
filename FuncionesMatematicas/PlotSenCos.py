'''
@author Tai543
Graficas de funciones trigonometricas: 
Funciones Seno y Coseno
'''
'''
Importamos 'matplotlib.pyplot' para generar graficas y 
'numpy' realizar operaciones matematicas de alto nivel
'''
import matplotlib.pyplot as plt
import numpy as np
# Vamos a definir las variables a utilizar
'''
En la varible 'x' vamos a definir un vector con valores 
que van del 0 a 4π y se incrementan en 0.1 utilizando la
funcion 'arange(inicio,fin,incremento)'
'''
x = np.arange(0,4*np.pi,0.1)
'''
En 'y_sen' evaluamos el vector 'x' con la funcion 'sin' 
y en 'y_cos' evaluamos el vector 'x' con la funcion 'cos' 
'''
y_sen = np.sin(x)
y_cos = np.cos(x)
# Vamos a mostrar ambas funciones en un solo grafico uwu
'''
Agregamos primero los pares para la funcion seno 'x' y 
'y_sen' y los pares para la funcion coseno 'x' y 'y_cos' 
'''
plt.plot(x,y_sen,x,y_cos)
# Con la funcion xlabel asignamos la descripcion al eje x
plt.xlabel('Eje x con valores de 0 a 4pi')
# Con la funcion ylabel asignamos la descripcion al eje y
plt.ylabel('sen(x) y cos(x)')
# Con title establecemos el titulo de nuestro grafico
plt.title('Grafico del seno y coseno de 0 a 4pi')
# Con legend vamos a asignar las leyendas a los graficos 
# en el orden que pusimos los pares en la funcion 'plot'
# es decir que el primer par corresponde a la funcion seno 
# y el segundo par a la funcion coseno 
plt.legend(['sen(x)','cos(x)'])
# Desplegamos el grafico con la funcion 'show' de pyplot
plt.show()


