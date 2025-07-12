from typing import Dict, List, Mapping, Tuple

"""
es cuando se declara junto a su valor el tipo de variable que junto a su libreria
    Ejemplo 
        nombre_variable : tipo_variable = Valor_variable

"""

nombre: str
nombre = "Ana"

edad: int = 25

pi: float  = 3.1416

# apellidos : list[str] = ["Botero", "Tafur", "Quiñonez"]
apellidos : List[str] = ["Botero", "Tafur", "Quiñonez"]

# lenguajes_programacion: tuple[str, str, str, str] = ("python", "java", "javascript", "golang")
lenguajes_programacion: Tuple[str, str, str] = ("python", "java", "javascript", "golang")

# lenguaje: dict = {"nombre": "python", "creador": "Guido Van Rossum"}
lenguaje: Dict[str, str] = {"nombre": "python", "creador": "Guido Van Rossum"}
