
'''
@author taicoding
Graficar multiples funciones 👩🏻‍🏫👩🏻‍💻
'''
'''
Importamos 'matplotlib.pyplot' para generar 
graficas, 'numpy' para realizar operaciones 
matematicas de alto nivel, 'matplotlib' para 
configurar algunos aspectos del grafico
'''
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
# Modificamos el tamaño de fuente usada 
# en todo nuestro grafico asignando el valor 
# '5.0' al atributo 'font.size'del diccionario 
# 'rcParams' de matplotlib
matplotlib.rcParams['font.size'] = 5.0
# Vamos a definir una funcion que nos sera muy util
def config_sub_grafico(x, y, axs, f, c, title,funcion):
    """ Establece la configuracion del sub grafico
    Parametros:
    x -- vector de valores para el eje x
    y -- vector de valores para el eje y
    axs -- matriz de ejes de los sub graficos
    f -- fila de la matriz de ejes 
    c -- columna de la matriz de ejes
    title -- titulo del sub grafico
    funcion -- formula de la funcion
    """
    # Establecemos la ubicacion del sub grafico 
    # en la matriz de ejes
    axs[f, c].plot(x, y)
    # Asignamos el titulo y subtitulo del sub grafico 
    # agregando entre ambas varibles un salto de 
    # linea '\n'
    axs[f, c].set_title(title+'\n'+funcion)
    
# En 'fig' almacenamos los elementos de todo el
# grafico, en 'axs' definimos nuestra matiz de ejes 
# Con la funcion 'subplots' establecemos las 
# dimensiones de nuestra matriz de ejes, en este 
# caso de 3x3, asignamos en 'figsize' las dimensiones 
# de los sub graficos con un alto y ancho de 10 pulgadas
fig, axs = plt.subplots(3, 3, figsize=(10,10))
# Para el eje 'x' establecemos la etiqueta del eje
# en la posicion (2,1) de la matriz de ejes 'axs', 
# con la funcion 'set_xlabel' y con el parametro 
# 'fontsize' establecemos el tamaño de la fuente en 12
axs[2,1].set_xlabel('x de -10 a 10',fontsize=12)
# Para el eje 'y' establecemos la etiqueta del eje 
# en la posicion (1,0) de la matriz de ejes 'axs',
# con la funcion 'set_ylabel'
axs[1,0].set_ylabel('f(x)',fontsize=12)

# Vamos a definir las variables a utilizar
# En 'x1' definimos un vector con valores negativos y 
# positivos de -10 a 10
x1 = np.arange(-10,10,0.1)
# En 'x2' definimos un vector solo con valores positivos 
# de 1 a 10
x2 = np.arange(1,10,0.1)
# En 'x3' definimos un vector con valores de 0 a 2π
x3 = np.arange(0,2*np.pi,0.1)
# Vamos a definir los elementos del sub grafico de la 
# funcion: Linea Recta
# En 'title_recta' definimos el titulo del sub grafico
title_recta= 'Linea Recta'
# En 'fun_recta' definimos la descripcion de la funcion
fun_recta='f(x) = ax +b'
# En 'recta' definimos ax+b con a=1, b=0 y evaluamos 
# los valores positivos y negativos almacenados en 'x1'
recta = x1
# Vamos a configurar la ubicacion de este sub grafico en 
# la posicion (0,0) de 'axs' y enviamos todos estos 
# elementos a la funcion 'config_sub_grafico'
config_sub_grafico(x1,recta,axs,0,0,title_recta,fun_recta)

# Vamos a definir los elementos del sub grafico de la 
# funcion: Parabola
title_parabola= 'Parabola'
fun_parabola='f(x) = ax**2 + bx + c'
# En 'parabola' definimos ax**2 + bx + c con a=1, b=1, c=0 
# y evaluamos valores positivos y negativos almacenados en 'x1'
parabola = (x1**2) + x1
# Vamos a configurar la ubicacion de este grafico en 
# la posicion (0,1) en 'axs' 
config_sub_grafico(x1,parabola,axs,0,1,title_parabola,fun_parabola)
# Vamos a definir los elementos del sub grafico de la 
# funcion: Polinomica
title_polinom= 'Polinomica'
fun_polinom='f(x) = ax**4 + bx**3 + cx**2 + dx + e'
# En 'polinom' definimos la ax**4 + bx**3 + cx**2 + dx + e
# con a=1, b=1, c=1, d=1, e=0 y evaluamos valores positivos 
# y negativos almacenados en 'x1'
polinom = (x1**4) + (x1**3) + (x1**2) + x1
# Vamos a configurar la ubicacion de este sub grafico en 
# la posicion (0,2) en 'axs' 
config_sub_grafico(x1,polinom,axs,0,2,title_polinom,fun_polinom)

# Vamos a definir los elementos del sub grafico de la 
# funcion: Exponencial
title_exp= 'Exponencial'
fun_exp='f(x) = exp(x)'
# En 'exp' evaluamos valores positivos almacenados en 'x2'
exp = np.exp(x2)
# Vamos a configurar la ubicacion de este sub grafico en 
# la posicion (1,0) en 'axs' 
config_sub_grafico(x2,exp,axs,1,0,title_exp,fun_exp)
# Vamos a definir los elementos del sub grafico de la 
# funcion: Logaritmica
title_log= 'Logaritmica'
fun_log='f(x) = log(x)'
# En 'log' evaluamos valores positivos almacenados en 'x2'
log = np.log(x2)
# Vamos a configurar la ubicacion de este sub grafico en 
# la posicion (1,1) en 'axs' 
config_sub_grafico(x2,log,axs,1,1,title_log,fun_log)

# Vamos a definir los elementos del sub grafico de la 
# funcion: Irracional
title_sqrt= 'Irracional'
fun_sqrt='f(x) = sqrt(x)'
# En 'sqrt' evaluamos valores positivos almacenados en 'x2'
sqrt = np.sqrt(x2)
# Vamos a configurar la ubicacion de este sub grafico en 
# la posicion (1,2) en 'axs' 
config_sub_grafico(x2,sqrt,axs,1,2,title_sqrt,fun_sqrt)
# Vamos a definir los elementos del sub grafico de la 
# funcion: Seno
title_sin= 'Seno'
fun_sin='f(x) = sen(x)'
# En 'seno' evaluamos valores de 0 a 2π almacenados 
# en 'x3'
seno = np.sin(x3)
# Vamos a configurar la ubicacion de este sub grafico en 
# la posicion (2,0) en 'axs'
config_sub_grafico(x3,seno,axs,2,0,title_sin,fun_sin)

# Vamos a definir los elementos del sub grafico de la 
# funcion: Coseno
title_cos= 'Coseno'
fun_cos='f(x) = cos(x)'
# En 'coseno' evaluamos valores de 0 a 2π almacenados 
# en 'x3'
coseno = np.cos(x3)
# Vamos a configurar la ubicacion de este sub grafico en 
# la posicion (2,1) en 'axs' 
config_sub_grafico(x3,coseno,axs,2,1,title_cos,fun_cos)
# Vamos a definir los elementos del sub grafico de la 
# funcion: Tangente
title_tan= 'Tangente'
fun_tan='f(x) = tan(x)'
# En 'tan' evaluamos valores de 0 a 2π almacenados 
# en 'x3'
tan = np.tan(x3)
# Vamos a configurar la ubicacion de este sub grafico en 
# la posicion (2,2) en 'axs' 
config_sub_grafico(x3,tan,axs,2,2,title_tan,fun_tan)
# Desplegamos el grafico con la funcion 'show' de pyplot
plt.show()