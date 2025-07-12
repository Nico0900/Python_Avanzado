import unittest  # Importa el módulo unittest para definir y ejecutar pruebas unitarias.


# Función que calcula el promedio usando un bloque try-except para manejar errores
def calcular_promedio_try_except(lista):
    try:
        promedio = sum(lista) / len(lista)  # Calcula la suma de los elementos dividida por el total de elementos
        return promedio  # Retorna el promedio
    except Exception as e:
        return None  # Si ocurre un error (por ejemplo, lista vacía -> división por cero), retorna None


# Función que calcula el promedio sin manejo de errores explícito
def calcular_promedio(lista):
    promedio = sum(lista) / len(lista)  # Calcula el promedio
    return promedio  # Retorna el promedio


# Clase de pruebas unitarias
class Test(unittest.TestCase):

    def test_promedio_exitoso_try_except(self):
        # Prueba que calcular_promedio_try_except funcione correctamente con una lista válida
        lista = [2, 3, 4]
        promedio_esperado = 3
        promedio_obtenido = calcular_promedio_try_except(lista)
        self.assertEqual(promedio_esperado, promedio_obtenido)  # Comprobamos que el promedio calculado sea el esperado

    def test_promedio_none_try_except(self):
        # Prueba que calcular_promedio_try_except retorne None al recibir una lista vacía (porque no se puede dividir por cero)
        lista_vacia = []
        promedio_obtenido = calcular_promedio_try_except(lista_vacia)
        self.assertIsNone(promedio_obtenido)  # Comprobamos que el resultado sea None

    def test_promedio_exitoso(self):
        # Prueba que calcular_promedio funcione correctamente con una lista válida
        lista = [2, 3, 4]
        promedio_esperado = 3
        promedio_obtenido = calcular_promedio(lista)
        self.assertEqual(promedio_esperado, promedio_obtenido)  # Comprobamos que el promedio calculado sea el esperado

    def test_promedio_falla(self):
        # Prueba que calcular_promedio lance una excepción al recibir una lista vacía
        with self.assertRaises(Exception):
            lista_vacia = []
            calcular_promedio(lista_vacia)  # Aquí se espera que falle con ZeroDivisionError


# Este bloque se ejecuta solo si el script se llama directamente
if __name__ == '__main__':
    unittest.main()  # Ejecuta todas las pruebas definidas en la clase Test
