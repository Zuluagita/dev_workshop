import math

class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números primos, números perfectos, triángulo de Pascal, etc.
    """

    def fibonacci(self, n):
        """Calcula el n-ésimo número de la secuencia de Fibonacci."""
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def secuencia_fibonacci(self, n):
        """Genera los primeros n números de la secuencia de Fibonacci."""
        secuencia = [0, 1]
        for i in range(2, n):
            secuencia.append(secuencia[-1] + secuencia[-2])
        return secuencia[:n]

    def es_primo(self, n):
        """Verifica si un número es primo."""
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def generar_primos(self, n):
        """Genera una lista de números primos hasta n."""
        return [i for i in range(2, n + 1) if self.es_primo(i)]

    def es_numero_perfecto(self, n):
        """Verifica si un número es perfecto."""
        return n > 0 and sum(i for i in range(1, n) if n % i == 0) == n

    def triangulo_pascal(self, filas):
        """Genera las primeras n filas del triángulo de Pascal."""
        triangulo = [[1]]
        for i in range(1, filas):
            fila = [1]
            for j in range(1, i):
                fila.append(triangulo[i - 1][j - 1] + triangulo[i - 1][j])
            fila.append(1)
            triangulo.append(fila)
        return triangulo

    def factorial(self, n):
        """Calcula el factorial de un número."""
        return 1 if n == 0 else n * self.factorial(n - 1)

    def mcd(self, a, b):
        """Calcula el máximo común divisor (MCD) de dos números."""
        while b:
            a, b = b, a % b
        return a

    def mcm(self, a, b):
        """Calcula el mínimo común múltiplo (MCM) de dos números."""
        return abs(a * b) // self.mcd(a, b) if a and b else 0

    def suma_digitos(self, n):
        """Calcula la suma de los dígitos de un número."""
        return sum(int(d) for d in str(abs(n)))

    def es_numero_armstrong(self, n):
        """Verifica si un número es de Armstrong."""
        digitos = [int(d) for d in str(n)]
        return sum(d ** len(digitos) for d in digitos) == n

    def es_cuadrado_magico(self, matriz):
        """Verifica si una matriz es un cuadrado mágico."""
        n = len(matriz)
        suma_objetivo = sum(matriz[0])
        
        for fila in matriz:
            if sum(fila) != suma_objetivo:
                return False

        for col in zip(*matriz):
            if sum(col) != suma_objetivo:
                return False

        if sum(matriz[i][i] for i in range(n)) != suma_objetivo:
            return False

        if sum(matriz[i][n - 1 - i] for i in range(n)) != suma_objetivo:
            return False

        return True
