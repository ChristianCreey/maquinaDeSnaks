#tupla
numeros = (1,2,3,4,5,6,7,8,9)

numero = int(input("Ingrese numero a buscar: "))
if numero in numeros:
    print(f"si existe {numero} en la tupla")
else:
    print(f"no existe {numero} en la tupla")

#set

conjunto = {'chris', 200, True, 'chris', 200, 'Ana'}
print(conjunto)
for i in conjunto:
    print(i, end=' ')

largo = len(conjunto)
print(f"tamaño de mi set {largo}")
conjunto.remove(200)
print(conjunto)
conjunto.add(500)
print(conjunto)


