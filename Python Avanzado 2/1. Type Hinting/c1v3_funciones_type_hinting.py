"""
type hinting  en funciones

    def calcular_perimetro_cuadrado(nombre_variable : tipo_variable) -> tipo_variable:
        return 4* lado

"""

def calular_perimetro_cuadrado(lado: int) -> int:
    return 4 * lado


print(calular_perimetro_cuadrado(lado="5"))
