# conexion.py
from sqlalchemy import create_engine 
"""
    [ from sqlalchemy import create_engine ]

    craete_engine : 
        Crea una conexion a la base de datos SQLite utilizando SQLAlchemy.
        Utiliza el motor de SQLAlchemy para conectarse a la base de datos y crear una sesion.
"""

from sqlalchemy.ext.declarative import declarative_base
"""
    [ from sqlalchemy.ext.declarative import declarative_base ]

    declarative_base : 
        Crea una clase base para los modelos de la base de datos.
        Esta clase base es utilizada para definir los modelos que representan las tablas de la base de datos.
        Los modelos heredan de esta clase base y definen los atributos que corresponden a las columnas de las tablas, Permite utilizar SQLAlchemy de manera declarativa, facilitando la definicion de modelos y la interaccion con la base de datos.
"""


from sqlalchemy.orm import sessionmaker
"""
    [ from sqlalchemy.orm import sessionmaker ]

    sessionmaker :
        Crea una sesion de SQLAlchemy para interactuar con la base de datos.
        La sesion es utilizada para realizar consultas, insertar, actualizar y eliminar datos en la base de datos.
"""

database_name = "empleados.sqlite" 
"""
    [ database_name = "empleados.sqlite"  ]

    Este es el nombre del archivo de la base de datos SQLite que vamos a utilizar.
"""

engine = create_engine(f"sqlite:///{database_name}")
"""
    [ engine = create_engine(f"sqlite:///{database_name}") ]

    creamos el motor de la base de datos utilizando SQLAlchemy
    El motor es el encargado de conectarse a la base de datos y ejecutar las consultas. En este caso, estamos utilizando SQLite como base de datos.
"""

Session = sessionmaker(bind=engine)
session = Session()
"""
    [ Session = sessionmaker(bind=engine) ]
    Crea una clase de sesion que se conecta al motor de la base de datos.
"""


ModeloBase = declarative_base()
"""
    [ ModeloBase = declarative_base() ]
    
    Crea una clase base para los modelos de la base de datos.
    Esta clase base es utilizada para definir los modelos que representan las tablas de la base de datos.
    Los modelos heredan de esta clase base y definen los atributos que corresponden a las columnas de las tablas.
    Permite utilizar SQLAlchemy de manera declarativa, facilitando la definicion de modelos y la interaccion con la base de datos.
"""