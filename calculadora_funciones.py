#calculadora con funciones

def menu():
    print(f'''Menu
        1. Suma
        2. Resta
        3. Multiplicacion
        4. Division
        5. Salir''')
    opcion = int(input("Dijite una opcion: "))
    return opcion

def valores():
    numero1 = int(input("Dijita el numero 1: "))
    numero2 = int(input("Dijita el numero 2: "))
    return numero1, numero2

def operacion(opcion, salir):
    if 1 <= opcion <= 4:
        num1, num2 = valores()

    if opcion == 1: #suma
        resultado = num1 + num2
        print(resultado)
    elif opcion == 2: # resta
        resultado = num1 - num2
        print(resultado)
    elif opcion == 3: #multiplicacion
        resultado = num1 * num2
        print(resultado)
    elif opcion == 4: #division
        resultado = num1 / num2
        print(resultado)
    elif opcion == 5:
        print("Saliendo ...")
        salir = True
    else:
        print("opcion invalida, selecciona otra opcion ...")
    return salir


salir = False
while not salir:
    opcion = menu()
    salir = operacion(opcion, salir)