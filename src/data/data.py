class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """

    def invertir_lista(self, lista):
        izquierda = 0
        derecha = len(lista) - 1

        while izquierda < derecha:
            lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]
            izquierda += 1
            derecha -= 1

        return lista

    def buscar_elemento(self, lista, elemento):
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1  

    def eliminar_duplicados(self, lista):
        resultado = []
        vistos = set()

        for elemento in lista:
            if (elemento, type(elemento)) not in vistos:
                resultado.append(elemento)
                vistos.add((elemento, type(elemento))) 

        return resultado

    def merge_ordenado(self, lista1, lista2):
        i, j = 0, 0
        resultado = []

        while i < len(lista1) and j < len(lista2):
            if lista1[i] < lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1

        resultado.extend(lista1[i:])
        resultado.extend(lista2[j:])

        return resultado

    def rotar_lista(self, lista, k):
        if not lista:
            return lista
        k = k % len(lista)  
        return lista[-k:] + lista[:-k]

    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1  
        suma_total = n * (n + 1) // 2  
        suma_lista = sum(lista)  
        return suma_total - suma_lista

    def es_subconjunto(self, conjunto1, conjunto2):
        for elemento in conjunto1:
            if elemento not in conjunto2:
                return False
        return True

    def implementar_pila(self):
        pila = []

        def push(valor):
            pila.append(valor)

        def pop():
            return pila.pop() if pila else None

        def peek():
            return pila[-1] if pila else None

        def is_empty():
            return len(pila) == 0

        return {
            "push": push,
            "pop": pop,
            "peek": peek,
            "is_empty": is_empty
        }

    def implementar_cola(self):
        cola = []

        def enqueue(valor):
            cola.append(valor)

        def dequeue():
            return cola.pop(0) if cola else None

        def peek():
            return cola[0] if cola else None

        def is_empty():
            return len(cola) == 0

        return {
            "enqueue": enqueue,
            "dequeue": dequeue,
            "peek": peek,
            "is_empty": is_empty
        }

    def matriz_transpuesta(self, matriz):
        if not matriz:
            return []

        filas = len(matriz)
        columnas = len(matriz[0])

        transpuesta = [[matriz[j][i] for j in range(filas)] for i in range(columnas)]

        return transpuesta
