import unittest  # Importa el módulo unittest, que permite escribir y ejecutar pruebas unitarias.


# Definición de la función es_numero_primo que recibe un número como argumento
def es_numero_primo(numero):

    if numero <= 1:
        # Si el número es menor o igual a 1, no es primo
        return False

    # Itera desde 2 hasta numero-1 para verificar si tiene algún divisor
    for i in range(2, numero):
        if numero % i == 0:
            # Si el número es divisible por i, no es primo
            return False

    # Si no se encontraron divisores, es primo
    return True


# Definición de la clase Test que hereda de unittest.TestCase.
# Aquí se colocan los métodos de prueba.
class Test(unittest.TestCase):

    def test_numero_menor_1(self):
        # Prueba con número menor o igual a 1 (en este caso, 1), debería retornar False.
        numero = 1
        resultado = es_numero_primo(numero)
        self.assertFalse(resultado)  # Comprobamos que el resultado sea False.

    def test_numero_primo_false(self):
        # Prueba con número que no es primo (en este caso, 4), debería retornar False.
        numero = 4
        resultado = es_numero_primo(numero)
        self.assertEqual(False, resultado)  # Comprobamos que el resultado sea exactamente False.

    def test_numero_primo_true(self):
        # Prueba con número primo (en este caso, 3), debería retornar True.
        numero = 3
        resultado = es_numero_primo(numero)
        self.assertTrue(resultado)  # Comprobamos que el resultado sea True.


# Este bloque se ejecuta solo si el script se ejecuta directamente.
if __name__ == '__main__':
    unittest.main()  # Llama al método main de unittest para ejecutar las pruebas definidas arriba.
