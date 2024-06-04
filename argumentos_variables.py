#Argumentos variables

# *args = arguments = tupla
# *kwargs = keyword arguments = diccionario
def superheroe_superpoderes(nombre, *args, **kwargs): #argumentos variables o tupla
    print(f"Superheroe: {nombre} - {args} - Mas info {kwargs}")
    for poder in args:
        print(f"superpoder {poder}")

superheroe_superpoderes('Superman', 'Volar', 'Rayos laser', 'Superfuerza', edad=25, empresa='DC')

superheroe_superpoderes('yo', personalidad='Buena onda')