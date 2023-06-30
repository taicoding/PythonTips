"""
@author taicoding
Métodos de Diccionarios 🐍
"""
# Diccionario inicial
persona = dict({"nombre": "taicoding"})
# ⭐️ Agregar elementos ⭐️
persona.update({"edad": 27})
print(persona)
# R: {'nombre': 'taicoding',
#     'edad': 27}
# ⭐️ Agregar elementos ⭐️
persona["alergias"] = ["almendras"]
print(persona)
# R: {'nombre': 'taicoding',
#     'edad': 27,
#     'alergias': ['almendras']}

# ⭐️ Remover un elemento especifico ⭐️
persona.pop("alergias")
print(persona)
# R: {'nombre': 'taicoding',
#     'edad': 27}

# ⭐️ Obtener el valor de una llave ⭐️
edad = persona["edad"]
print(edad)
# R: 27
edad = persona.get("edad")
print(edad)
# R: 27

# ⭐️ Obtener el valor de una llave ⭐️
# Si la llave no existe regresa
# un valor por defecto
alergia = persona.setdefault("alergias", "ninguna")
print(alergia)
# R: ninguna
# ⭐️ Obtener una lista de las llaves ⭐️
llaves = persona.keys()
print(llaves)
# R: dict_keys(['nombre', 'edad'])

# ⭐️ Obtener una lista de los valores ⭐️
valores = persona.values()
print(valores)
# R: dict_values(['taicoding', 27])

# ⭐️ Actualizar el valor de una llave ⭐️
persona["edad"] = 29
print(persona)
# R: {'nombre': 'taicoding',
#     'edad': 29}
persona.update({"edad": 30})
print(persona)
# R: {'nombre': 'taicoding',
#     'edad': 30}

# ⭐️ Eliminar todos los elementos ⭐️
persona.clear()
print(persona)
# R: {}

# ⭐️ Crear un diccionario desde una tupla
# de llaves y valores por defecto⭐️
llaves = ("nombre", "edad")
valor = "vació"
persona = dict.fromkeys(llaves, valor)
print(persona)
# R: {'nombre': 'vació', 'edad': 'vació'}
