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

    def front(self):
        if self.is_empty():
            raise IndexError("La cola esta vacía")
        return self.items[0] # Devuelve el primer elemento sin eliminarlo

    def rear(self):
        if self.is_empty():
            raise IndexError("La cola esta vacía")
        return self.items[-1] # Devuelve el ultimo elemento sin eliminarlo

    def is_empty(self):
        return len(self.items) == 0 # Verifica si La cola está vacía

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()

    def peek(self, index):
        if index < 0 or index >= len(self.items):
            raise IndexError("Indice fuera de rango")
        return self.items[index] # Devuelve el elemento en La posicion especificada

    def contains(self, item):
        return item in self.items # Verifica si un elemento esta en La cola

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

    # Front
    print("Elemento del frente:", cola.front())

    # Rear
    print("Último elemento:", cola.rear())

    # IsEmpty
    print("¿La cola está vacía?", cola.is_empty())

    # Size
    print("Tamaño de la cola:", cola.size()) 

    # Peek
    print("Elemento en la posición 1:", cola.peek(1))

    # Contains
    print("¿La cola contiene el num 200?", cola.contains(200))
    # True

    # Dequeue
    print("Elemento dequeue:", cola.dequeue()) # 100
    [321, 9398]

    print("Cola en estado actual:", cola.items)

    cola.clear()
    print("Cola despues de clear:", cola.items) # []