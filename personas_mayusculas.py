
def persona_mayuscula(nombre, apellido='', edad=0): #podemos poner valores por default o no
    print("Esta funcion regresa varios valores (tupla): ")
    return nombre.upper(), apellido.upper(), edad


#llamamos la funcion
nombre, apellido, edad = persona_mayuscula('Chris', 'Creey', 22)
print(f"Persona: nombre {nombre}, apellido: {apellido}, edad: {edad} ")
