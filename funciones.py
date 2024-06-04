from modulo_funcion import saludar

print("Manejo de funciones")

#llamamos la funcion
argumento = input("ingrese un mensaje: ")
valor_devuelto = saludar(argumento)
print(f"valor devuelto: {valor_devuelto}" )
saludar(argumento)
#saludar('saludos')
#saludar('adios')

