from conexion import ModeloBase
"""   
    [ from conexion import ModeloBase ]

    ModeloBase :  
        Clase base para los modelos de la base de datos.
        Esta clase base es utilizada para definir los modelos que representan las tablas de la base de datos.
        Los modelos heredan de esta clase base y definen los atributos que corresponden a las columnas de las tablas.
        Permite utilizar SQLAlchemy de manera declarativa, facilitando la definicion de modelos y la interaccion con la base de datos.
"""
from sqlalchemy import Column, ForeignKey, Integer, String
"""
    [ from sqlalchemy import Column, ForeignKey, Integer, String ]
    todo estos datos son necesarios para definir los modelos de la base de datos. y son importadors de SQLAlchemy. desde conexion importan a ModeloBase.
    - Column: Permite definir una columna en la tabla de la base de datos.
    - ForeignKey: Permite definir una clave foranea que referencia a otra tabla.
    - Integer: Tipo de dato entero para las columnas.
    - String: Tipo de dato cadena de texto para las columnas.   
"""

class Departamento(ModeloBase):
    __tablename__ = "departamento"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False, unique=True)

    def __init__(self, nombre):
        self.nombre = nombre
"""
    [ class Departamento(ModeloBase) ]
    Modelo que representa la tabla "departamento" en la base de datos.
    Hereda de ModeloBase, que es la clase base para los modelos de la base de datos.
    Define los atributos que corresponden a las columnas de la tabla "departamento".
    - id: Identificador unico del departamento (clave primaria).
    - nombre: Nombre del departamento, no puede ser nulo y debe ser unico.
    El constructor inicializa el nombre del departamento.
"""

class Empleado(ModeloBase):
    
    __tablename__ = "empleado"
    """aqui asiganamos el nombre de la tabla empleado"""
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    documento = Column(String, nullable=False, unique=True)
    departamento_id = Column(Integer, ForeignKey('departamentos.id'))
    """
        [ class Empleado(ModeloBase) ]
        Modelo que representa la tabla "empleado" en la base de datos.
        Hereda de ModeloBase, que es la clase base para los modelos
        de la base de datos.
        Define los atributos que corresponden a las columnas de la tabla "empleado".
        - id: Identificador unico del empleado (clave primaria).
        - nombre: Nombre del empleado, no puede ser nulo.
        - apellido: Apellido del empleado, no puede ser nulo.
        - documento: Documento del empleado, no puede ser nulo y debe ser unico.
        - id_departamento: Identificador del departamento al que pertenece el empleado (clave foranea que referencia a la tabla "departamento").
    """

    def __init__(self, nombre, apellido, documento, id_departamento):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.id_departamento = id_departamento

    """    
    [ def __init__(self, nombre, apellido, documento, id_departamento) ]
        Constructor de la clase Empleado.
        Inicializa los atributos del empleado.
        - nombre: Nombre del empleado.
        - apellido: Apellido del empleado.
        - documento: Documento del empleado.
        - id_departamento: Identificador del departamento al que pertenece el empleado.
    """
