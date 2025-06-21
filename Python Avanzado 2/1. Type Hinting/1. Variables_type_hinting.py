from typing import List, Tuple, Dict

"""
es cuando se declara junto a su valor el tipo de variable que junto a su libreria
    Ejemplo 
        nombre_variable : tipo_variable = Valor_variable

"""

nombre: str = "Nicolas"

edad : int ="25"

pi : float = 3.1416

apellidos : list = ["Botero", "tafur", "Quinonez"]
apellidos : List[str] = ["Botero", "tafur", "Quinonez"]

lenguaje_progamacion : tuple = ("python", "java", "javascripts", "golang")
lenguaje_progamacion : Tuple[str, str, str, str] = ("python", "java", "javascripts", "golang")

lenguaje : dict = {"nombre":"Python", "creador":"Guido VAn Rossum"}
lenguaje : Dict [str, str] = {"nombre":"Python", "creador":"Guido VAn Rossum"}