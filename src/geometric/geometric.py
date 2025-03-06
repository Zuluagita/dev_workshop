import math

class Geometria:
    """
    Clase con ejercicios geométricos.
    Incluye operaciones básicas y avanzadas en 2D y 3D.
    """

    def area_rectangulo(self, base, altura):
        "Calcula el área de un rectángulo."
        return base * altura

    def perimetro_rectangulo(self, base, altura):
        "Calcula el perímetro de un rectángulo."
        return 2 * (base + altura)

    def area_circulo(self, radio):
        "Calcula el área de un círculo."
        return math.pi * radio ** 2

    def perimetro_circulo(self, radio):
        "Calcula el perímetro (circunferencia) de un círculo."
        return 2 * math.pi * radio

    def area_triangulo(self, base, altura):
        "Calcula el área de un triángulo."
        return (base * altura) / 2

    def perimetro_triangulo(self, lado1, lado2, lado3):
        "Calcula el perímetro de un triángulo."
        return lado1 + lado2 + lado3

    def es_triangulo_valido(self, lado1, lado2, lado3):
        """
        Verifica si tres longitudes pueden formar un triángulo válido.
        Un triángulo es válido si la suma de las longitudes de dos lados
        es mayor que la longitud del tercer lado, para todos los lados."""
        return (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)

    def area_trapecio(self, base_mayor, base_menor, altura):
        "Calcula el área de un trapecio."
        return ((base_mayor + base_menor) * altura) / 2

    def area_rombo(self, diagonal_mayor, diagonal_menor):
        "Calcula el área de un rombo usando sus diagonales."
        return (diagonal_mayor * diagonal_menor) / 2

    def area_pentagono_regular(self, lado, apotema):
        "Calcula el área de un pentágono regular."
        return (5 * lado * apotema) / 2

    def perimetro_pentagono_regular(self, lado):
        "Calcula el perímetro de un pentágono regular."
        return 5 * lado

    def area_hexagono_regular(self, lado, apotema):
        "Calcula el área de un hexágono regular."
        return (6 * lado * apotema) / 2

    def perimetro_hexagono_regular(self, lado):
        "Calcula el perímetro de un hexágono regular."
        return 6 * lado

    def volumen_cubo(self, lado):
        "Calcula el volumen de un cubo."
        return lado ** 3

    def area_superficie_cubo(self, lado):
        "Calcula el área de la superficie de un cubo."
        return 6 * (lado ** 2)

    def volumen_esfera(self, radio):
        "Calcula el área del volumen de una esfera."
        return (4 / 3) * math.pi * radio ** 3

    def area_superficie_esfera(self, radio):
        "Calcula el área de la superficie de una esfera."
        return 4 * math.pi * radio ** 2

    def volumen_cilindro(self, radio, altura):
        "Calcula el volumen de un cilindro."
        return math.pi * radio ** 2 * altura

    def area_superficie_cilindro(self, radio, altura):
        "Calcula el área de la superficie de un cilindro."
        return 2 * math.pi * radio * (radio + altura)

    def distancia_entre_puntos(self, x1, y1, x2, y2):
        "Calcula la distancia euclidiana entre dos puntos en un plano 2D."
        return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)

    def punto_medio(self, x1, y1, x2, y2):
        "Calcula el punto medio entre dos puntos en un plano 2D."
        return ((x1 + x2) / 2, (y1 + y2) / 2)

    def pendiente_recta(self, x1, y1, x2, y2):
        "Calcula la pendiente de una recta que pasa por dos puntos."
        if x1 == x2:
            raise ZeroDivisionError("La pendiente es indefinida para líneas verticales.")
        return (y2 - y1) / (x2 - x1)

    def ecuacion_recta(self, x1, y1, x2, y2):
        "Obtiene los coeficientes de la ecuación de una recta en la forma Ax + By + C = 0."
        if x1 == x2:
            return (1, 0, -x1) 
        A = y2 - y1
        B = x1 - x2
        C = (x2 * y1) - (x1 * y2)
        return (A, B, C)

    def area_poligono_regular(self, num_lados, lado, apotema):
        "Calcula el área de un polígono regular."
        return (num_lados * lado * apotema) / 2

    def perimetro_poligono_regular(self, num_lados, lado):
        "Calcula el perímetro de un polígono regular."
        return num_lados * lado

