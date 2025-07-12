import unittest


def es_numero_primo(numero):

    if numero <= 1:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True


class Test(unittest.TestCase):

    def test_numero_menor_1(self):
        numero = 1 # caso de prueba para un numero menor o igual a 1"
        resultado = es_numero_primo(numero)
        self.assertTrue(resultado)

    def test_numero_primo_false(self):
        numero = 4
        resultado = es_numero_primo(numero)
        self.assertEqual(False, resultado)

    def test_numero_primo_true(self):
        numero = "2" # esto es un muestra de un error causado por un String donde deberia ser un entero, para poder visualizar el error
        resultado = es_numero_primo(numero)
        self.assertTrue(resultado)


if __name__ == '__main__':
    unittest.main()
