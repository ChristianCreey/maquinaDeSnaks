print("listas y diccionario")

personas = [
            {'nombre':'Regina','apellido':'Flores','edad':22},
            {'nombre':'Juan','apellido':'Perez','edad':23}
]

print(personas[0].get('nombre'))
print(personas[1].get('edad'))

#
for contador, persona in enumerate(personas):
    print(f"persona {contador}: {persona.get('nombre')}")