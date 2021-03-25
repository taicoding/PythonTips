"""
@author Tai543
Ambientes virtuales
Supongamos que tenemos una carpeta 'proyecto' y 
ejecutamos los siguientes comandos
"""
# Instalar virtualenv 
> pip install virtualenv
# Verificar instalacion 
> virtualenv --version
# Creamos un ambiente virtual llamado 'env'
> virtualenv env
'''
Como resultado tendremos la siguiente estructura 
de carpetas:
proyecto/
└──env
'''
# Activamos el ambiente virtual en Windows
> env\Scripts\activate
# Activamos el ambiente virtual en Linux / Mac OS
$ source env/bin/activate
# Crear ambientes virtuales nos permite aislar las 
# dependencias de cada proyecto 👩🏻‍🏫👩🏻‍💻