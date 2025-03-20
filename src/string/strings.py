import re

class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    """

    def es_palindromo(self, texto):
        """Verifica si una cadena es un palíndromo."""
        texto_limpio = ''.join(c.lower() for c in texto if c.isalnum())  # Quita espacios y signos
        return texto_limpio == texto_limpio[::-1]

    def invertir_cadena(self, texto):
        """Invierte una cadena de texto sin usar slicing ni reversed()."""
        invertida = ""
        for char in texto:
            invertida = char + invertida
        return invertida

    def contar_vocales(self, texto):
        """Cuenta el número de vocales en una cadena."""
        vocales = "aeiouAEIOU"
        return sum(1 for c in texto if c in vocales)

    def contar_consonantes(self, texto):
        """Cuenta el número de consonantes en una cadena."""
        consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        return sum(1 for c in texto if c in consonantes)

    def es_anagrama(self, texto1, texto2):
        """Verifica si dos cadenas son anagramas."""
        return sorted(texto1.replace(" ", "").lower()) == sorted(texto2.replace(" ", "").lower())

    def contar_palabras(self, texto):
        """Cuenta el número de palabras en una cadena."""
        return len(texto.split())

    def palabras_mayus(self, texto):
        """Pone en mayúscula la primera letra de cada palabra en una cadena sin eliminar espacios."""
        return ' '.join(word.capitalize() if word else "" for word in texto.split(" "))

    def eliminar_espacios_duplicados(self, texto):
        """Elimina espacios duplicados en una cadena sin eliminar espacios al inicio o final."""
        return re.sub(r'\s+', ' ', texto).strip()

    def es_numero_entero(self, texto):
        """Verifica si una cadena representa un número entero sin usar isdigit()."""
        if not texto:
            return False
        if texto[0] in ("-", "+"):
            texto = texto[1:]
        return texto.isdigit()

    def cifrar_cesar(self, texto, desplazamiento):
        """Aplica el cifrado César a una cadena de texto."""
        resultado = ""
        for c in texto:
            if 'a' <= c <= 'z':
                resultado += chr((ord(c) - ord('a') + desplazamiento) % 26 + ord('a'))
            elif 'A' <= c <= 'Z':
                resultado += chr((ord(c) - ord('A') + desplazamiento) % 26 + ord('A'))
            else:
                resultado += c
        return resultado

    def descifrar_cesar(self, texto, desplazamiento):
        """Descifra una cadena cifrada con el método César."""
        return self.cifrar_cesar(texto, -desplazamiento)

    def encontrar_subcadena(self, texto, subcadena):
        """Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index()."""
        posiciones = []
        longitud_subcadena = len(subcadena)
        for i in range(len(texto) - longitud_subcadena + 1):
            if texto[i:i + longitud_subcadena] == subcadena:
                posiciones.append(i)
        return posiciones
