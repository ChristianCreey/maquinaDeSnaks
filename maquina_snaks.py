
snacks = [
    {'id':0, 'nombre':'Papas', 'precio':20},
    {'id':1, 'nombre':'Pan', 'precio':10},
    {'id':2, 'nombre':'Torta', 'precio':30},
    {'id':3, 'nombre':'Paleta', 'precio':5},
    {'id':4, 'nombre':'Galletas', 'precio':25}
]

#lista de productos
productos = []

print(" *** maquina snaks *** ")
print("snaks disponibles")
for snack in snacks:
    print(f'''\tId: {snack['id']} -> {snack['nombre']} - {snack['precio']} ''')

def maquina_snack(snacks, productos):
    salir = False
    while not salir:
        print(f'''Menu:
        1. comprar snack
        2. Mostrar ticket
        3. salir''')
        opcion = int(input('Elije una opcion: '))
        if opcion == 1:
            comprar_producto(snacks, productos)
        elif opcion == 2:
            mostrar_ticket(productos)
        elif opcion == 3:
            print("Regresa pronto")
            salir =True
        else:
            print("opcion invalida, selecciona otra opcion ...")

def comprar_producto(snacks, productos):
    id_snack = int(input("Seleccione el id del snack: "))
    productos.append(snacks[id_snack])
    print(f"Snack agregao {snacks[id_snack]}")

def mostrar_ticket(productos):
    ticket = f'\t*** Ticket de venta ***'
    total = 0
    for producto in productos:
        ticket += f"\n\t - {producto['nombre']} - ${producto['precio']}"
        total += producto['precio']
    ticket += f"\n\tTotal -> ${total}"
    print(ticket)

maquina_snack(snacks, productos)