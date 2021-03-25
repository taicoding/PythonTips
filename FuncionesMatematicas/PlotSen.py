'''
@author Tai543
Graficas de funciones trigonometricas: Funcion Seno
'''
# Vamos a importar las extensiones necesarias para este ejemplo
'''
Importamos 'matplotlib', especificamos el modulo 'pyplot' 
y le daremos el alias 'plt'. Esta biblioteca nos permite generar graficas. 
'''
import matplotlib.pyplot as plt
'''
Importamos 'numpy' le daremos el alias 'np'. Esta biblioteca nos permite 
realizar operaciones matematicas de alto nivel con vectores y matrices.
'''
import numpy as np
#Vamos a definir las variables que vamos a usar para la grafica
'''
En la varible 'x' usando la funcion 'range(inicio,fin,incremento)' de numpy 
vamos a definir un vector con valores que van del 0 a 4π y se incrementan en 0.1
'''
x = np.arange(0,4*np.pi,0.1)
'''
En la variable 'y' evaluamos el vector 'x' con la funcion 'sin' de numpy
'''
y = np.sin(x)

#Ahora si vamos a graficar los valores de ambas variables uwu
'''
Asignamos los valores del eje 'x' y 'y' al grafico con la funcion 'plot' de pyplot  
'''
plt.plot(x,y)
'''
Desplegamos el grafico con la funcion 'show' de pyplot
'''
plt.show()