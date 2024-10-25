#pila:
pila = []

print("La pila esta vacia?:", len(pila)== 0)

#agrega valores a pila
while True:
    try:
        quantity = int(input("\nCuantos valores desas agregar a la pila?: "))
        break
    except ValueError:
        print("\nIngresa un numero!")

print()

for a in range(quantity):
    b = a+1
    valor = input(f"Ingresa el valor #{b} a agregar:")
    a -= 1
    pila.append(valor)

print("\nEstado actual de la pila: ", pila)

print("\nSize de la pila: ", len(pila))

print("\nPila despues de limpiar: ", pila.clear())

pila.extend([20, 30, 45, 30])
print("\nPila nueva con .extend: ", pila)

pila_copia = pila[:]
print("\nPila original:", pila)
print("\nPila copia:", pila_copia)

pila_copia.reverse()
print("\nPila copia después de invertir:", pila_copia)

print("\nÍndice del elemento 45 en la pila copia:", pila_copia.index(45))

print("\nNúmero de veces que aparece el 30 en la pila copia:", pila_copia.count(30))