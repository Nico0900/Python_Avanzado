# Importa Union del módulo typing para permitir múltiples tipos de datos en las anotaciones de tipo
from typing import Union

# Define una función que calcula el perímetro de un cuadrado.
# Recibe un parámetro 'lado' que puede ser int o float y retorna un valor del mismo tipo.
def calular_perimetro_cuadrado(lado: Union[int, float]) -> Union[int, float]:
    # Multiplica el valor del lado por 4 para obtener el perímetro
    return 4 * lado

# Llama a la función con el valor 5.1 y muestra el resultado en pantalla
print(calular_perimetro_cuadrado(lado=5.1))
