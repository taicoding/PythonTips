'''
@author Tai543
Graficas de funciones trigonometricas: 
Funcion Coseno
'''
# Vamos a importar las extensiones necesarias para 
# este ejemplo
'''
Importamos 'matplotlib', especificamos el 
modulo 'pyplot' y le daremos el alias 'plt'. 
Esta biblioteca nos permite generar graficas. 
'''
import matplotlib.pyplot as plt
'''
Importamos 'numpy' le daremos el alias 'np'. 
Esta biblioteca nos permite realizar operaciones 
matematicas de alto nivel con vectores y matrices.
'''
import numpy as np
# Vamos a definir las variables que vamos a usar 
# para la grafica
'''
En la varible 'x' usando la funcion 
'arange(inicio,fin,incremento)' de numpy 
vamos a definir un vector con valores que van 
del 0 a 4π y se incrementan en 0.1
'''
x = np.arange(0,4*np.pi,0.1)
'''
En la variable 'y' evaluamos el vector 'x' con la 
funcion 'cos' de numpy
'''
y = np.cos(x)

# Ahora si vamos a graficar la funcion y haremos que 
# se vea muy cool uwu
# Asignamos los valores del eje 'x' y 'y' al grafico con 
# la funcion 'plot' de pyplot  
plt.plot(x,y)
# La funcion xlabel nos permite asignar una descripcion al 
# eje x
plt.xlabel('Eje x con valores de 0 a 4pi')
# La funcion ylabel nos permite asignar una descripcion al 
# eje y
plt.ylabel('cos(x)')
# La funcion title nos permite asignar el titulo de 
# nuestro grafico
plt.title('Grafico del coseno de 0 a 4pi')
# La funcion legend nos permite asignar la decripcion de
# los pares graficados
plt.legend(['cos(x)'])
# Desplegamos el grafico con la funcion 'show' de pyplot
plt.show()

