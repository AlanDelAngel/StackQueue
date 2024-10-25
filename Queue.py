#Creamos La claes cola que tendra todas las funciones
class Queue:
    def __init__(self): # Fixed typo: _init __ should be __init__
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("La cola esta vacía")
        return self.items.pop(0) # Elimina y devuelve el primer elemento

    def is_empty(self):
        return len(self.items) == 0 # Verifica si La cola está vacía

    def peek(self, index):
        if index < 0 or index >= len(self.items):
            raise IndexError("Indice fuera de rango")
        return self.items[index] # Devuelve el elemento en La posicion especificada

# Ejemplo de como se usan Las funciones de colas
#Ponemos estas dos Líneas de código para separar La definición de La clase
# y sus métodos del código que escribiremos para implementar Las funciones
if __name__ == "__main__": # Fixed typo: _name __ and _main __ should be __name__ and __main__
    cola = Queue()

# Enqueue
    cola.enqueue(123)
    cola.enqueue(321)
    cola.enqueue(9398)
    cola.enqueue(8)
    print("Cola después de enqueue:", cola.items)

    # IsEmpty
    print("¿La cola está vacía?", cola.is_empty())

    # Peek
    print("Elemento en la posición 1:", cola.peek(1))

    # Dequeue
    print("Elemento dequeue:", cola.dequeue()) # 100
    [321, 9398]

    print("Cola en estado actual:", cola.items)

    cola.clear()
    print("Cola despues de clear:", cola.items) # []