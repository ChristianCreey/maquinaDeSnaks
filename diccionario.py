
diccionario = {'nombre':'Chris',
               'apellido':'creey',
               'edad':22}

print(diccionario)
print(f"nombre: {diccionario['nombre']}")
print(f"apellido: {diccionario['apellido']}")
print(f"edad: {diccionario.get('edad')}")

#agregar nuevo elemento
diccionario['telefono'] = 7121862303
print(diccionario)
print(f"telefono: {diccionario.get('telefono')}")

#obtener una lisa de llaves de diccionario
print(f"lista de llaves {diccionario.keys()}")
#lista de valores
print(f"valores {diccionario.values()}")
#elementos
print(f"elementos {diccionario.items()}")

llave = 'nombre'
if llave in diccionario:
    print("si existe")
else:
    print("no existe")

#actualizar un elemento
diccionario['edad'] = 23
print(diccionario)

#eliminar un elemento
diccionario.pop('telefono')
print(diccionario)

#recorrer llaves en dic
for llave in diccionario.keys():
    print(f" llave {llave}")

#recorrer valores en dic
for valor in diccionario.values():
    print(f" llave {valor}")

#recorrer llaves en dic
print()
for llave, valor in diccionario.items():
    print(f" llave {llave} valor {valor}")