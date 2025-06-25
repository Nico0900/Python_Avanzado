# conexion.py
from sqlalchemy import create_engine 
"""
    [ from sqlalchemy import create_engine ]

    craete_engine : 
        Crea una conexion a la base de datos SQLite utilizando SQLAlchemy.
        Utiliza el motor de SQLAlchemy para conectarse a la base de datos y crear una sesion.
"""

from sqlalchemy.ext.declarative import declarative_base


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

ModeloBase = declarative_base()
