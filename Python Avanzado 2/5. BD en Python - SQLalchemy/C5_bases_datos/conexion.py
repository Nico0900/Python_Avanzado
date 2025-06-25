"""
Las Bases de datos 
    permiten almacenar, consultar, modificar y eliminar datos de manera eficiente.
    En Python, una de las librerias mas utilizadas para trabajar con bases de datos es SQLAlchemy.
    SQLAlchemy es un ORM (Object Relational Mapper) que permite interactuar con bases de datos de manera sencilla y eficiente.
    En este ejemplo, vamos a crear una conexion a una base de datos SQLite utilizando SQLAlchemy.

Existen las bases de datos relacionales y no relacionales.
# Relacionales
    Las bases de datos relacionales utilizan tablas para almacenar los datos y permiten realizar consultas complejas utilizando SQL (Structured Query Language). Estas bases de datos son ideales para aplicaciones que requieren integridad referencial y transacciones. 

# No Relacionales
    Por otro lado, las bases de datos no relacionales (NoSQL) son más flexibles y permiten almacenar datos en formatos no estructurados, como documentos o grafos.

En Python, existen varias librerias para trabajar con bases de datos, como SQLite, PostgreSQL, MySQL y MongoDB.
Cada una de estas bases de datos tiene sus propias características y
ventajas, y la elección de una u otra dependerá de las necesidades del proyecto.

Existen lo tipos de bases de datos mas comunes:

    - SQLite: es una base de datos ligera y embebida, ideal para aplicaciones   pequeñas y desarrollo local. No requiere un servidor separado y almacena los datos en un solo archivo.

    - PostgreSQL: es una base de datos relacional de código abierto, conocida por su robust ez y características avanzadas. Es adecuada para aplicaciones de producción y escalables.

    - MySQL: es otra base de datos relacional de código abierto, ampliamente utilizada en aplicacionesweb y sistemas de gestión de contenido. Ofrece un buen rendimiento y es fácil de usar.

    - MongoDB: es una base de datos NoSQL orientada a documentos, ideal para aplicaciones que requieren flexibilidad en el esquema de datos. Almacena datos en formato JSON y es adecuada para aplicaciones que manejan grandes volúmenes de datos no estructurados.  

Existen las ORM (Object Relational Mapper) Librerias especializadas para la manipulacion de bases de datos.
Usualmente una tabla de la base de datos es representada por una clase de Python, y cada fila de la tabla es representada por un objeto de esa clase o modelo. Tambien cada columna de la tabla es representada por un atributo de la clase. donde se define el tipo de dato de cada atributo, y se pueden definir relaciones entre tablas utilizando atributos de tipo ForeignKey o primary key. (llave foranea o llave primaria).

Cuando damos uso a una ORM, no necesitamos escribir consultas SQL directamente, sino que utilizamos métodos y atributos de las clases para realizar operaciones en la base de datos. Esto nos permite trabajar con bases de datos de manera más intuitiva y orientada a objetos.

Existen varias ORM populares en Python que facilitan la interacción con bases de datos relacionales:

    - SQLAlchemy: es una de las librerias mas populares para trabajar con bases de datos en Python. Proporciona una interfaz de alto nivel para interactuar con bases de datos relacionales y permite definir modelos de datos utilizando clases de Python.

    - Django ORM: es el ORM integrado en el framework Django, que permite interactuar con bases de datos de manera sencilla y eficiente. Proporciona una interfaz de alto nivel para definir modelos de datos y realizar consultas utilizando una sintaxis similar a SQL.

    - Peewee: es una ORM ligera y fácil de usar para Python. Permite definir modelos de datos utilizando clases de Python y realizar consultas de manera sencilla. Es ideal para aplicaciones pequeñas y medianas que no requieren características avanzadas de bases de datos.

    - Tortoise-ORM: es una ORM asíncrona para Python, que permite interactuar con bases de datos de manera eficiente en aplicaciones asíncronas. Proporciona una interfaz de alto nivel para definir modelos de datos y realizar consultas utilizando una sintaxis similar a SQL.

    - Pony ORM: es una ORM que permite definir modelos de datos utilizando una sintaxis similar to Python, lo que facilita la escritura de consultas complejas. Proporciona una interfaz de altonivel para interactuar con bases de datos relacionales y permite realizar consultas utilizando una sintaxis similar a SQL.

    SQLObject: es una ORM que permite interactuar con bases de datos relacionales utilizando una sintaxis similar a SQL. Proporciona una interfaz de alto nivel para definir modelos de datos y realizar consultas utilizando una sintaxis similar a SQL.

SQLAlchemy es una de las librerias mas populares para trabajar con bases de datos en Python y es ampliamente utilizada en aplicaciones web y sistemas de gestión de contenido.
SQLAlchemy permite definir modelos de datos utilizando clases de Python y proporciona una interfaz de alto nivel para interactuar con bases de datos relacionales.

En este ejemplo, vamos a crear una conexion a una base de datos SQLite utilizando SQLAlchemy.
"""



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
