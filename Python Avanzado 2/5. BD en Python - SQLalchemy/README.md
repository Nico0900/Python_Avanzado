# Bases de Datos y ORMs en Python

## Introducción

Una **base de datos** es una herramienta que permite almacenar, organizar y gestionar información estructurada. Es esencial en el desarrollo de aplicaciones, ya que posibilita guardar datos de forma persistente a lo largo del tiempo.

Las bases de datos pueden ser:

- **Relacionales (SQL):** Organizan los datos en tablas (estructura tabular).
- **No relacionales (NoSQL):** Usan estructuras como documentos, grafos, pares clave-valor, etc.

---

## Bases de Datos Relacionales y SQL

Las **bases de datos relacionales** utilizan **SQL (Structured Query Language)**, un lenguaje especializado que permite:

- Insertar datos
- Eliminar registros
- Actualizar información
- Consultar datos

# Tipos de Bases de Datos
- Existen los tipos de bases de datos más comunes:

## SQLite 
- Base de datos ligera y embebida, ideal para aplicaciones pequeñas y desarrollo local. No requiere un servidor separado y almacena los datos en un solo archivo.

## PostgreSQL
- Base de datos relacional de código abierto, conocida por su robustez y características avanzadas. Es adecuada para aplicaciones de producción y escalables.

## MySQL 
- Otra base de datos relacional de código abierto, ampliamente utilizada en aplicaciones web y sistemas de gestión de contenido. Ofrece buen rendimiento y es fácil de usar.

## MongoDB
- Base de datos NoSQL orientada a documentos. Almacena datos en formato JSON y es adecuada para aplicaciones que manejan grandes volúmenes de datos no estructurados.

---

# Relacionales vs No Relacionales

## Relacionales
- Las bases de datos relacionales utilizan tablas para almacenar los datos y permiten realizar consultas complejas utilizando SQL. Estas bases de datos son ideales para aplicaciones que requieren integridad referencial y transacciones.

## No Relacionales
- Las bases de datos no relacionales (NoSQL) son más flexibles y permiten almacenar datos en formatos no estructurados, como documentos o grafos.

## Librerías en Python para Bases de Datos
# En Python, existen varias librerías para trabajar con bases de datos como:
- SQLite
- PostgreSQL
- MySQL
- MongoDB

Cada una tiene sus propias características y ventajas. La elección dependerá de las necesidades específicas del proyecto.

ORMs en Python (Object Relational Mappers)
Una ORM es una librería que permite la manipulación de bases de datos de forma orientada a objetos.

Usualmente, una tabla de la base de datos es representada por una clase de Python, y cada fila de la tabla por un objeto de esa clase. Cada columna se define como un atributo, donde también se especifica el tipo de dato y relaciones como claves primarias (PrimaryKey) o claves foráneas (ForeignKey).

Al usar una ORM, no es necesario escribir consultas SQL directamente; en cambio, se usan métodos y atributos de las clases.

ORMs Populares en Python
SQLAlchemy: Una de las más populares. Proporciona una interfaz de alto nivel para interactuar con bases de datos relacionales y definir modelos con clases de Python.

Django ORM: Integrada en el framework Django. Muy eficiente y sencilla de usar, con sintaxis similar a SQL.

Peewee: Ligera y fácil de usar. Ideal para aplicaciones pequeñas o medianas.

Tortoise ORM: Asíncrona, ideal para apps basadas en async/await.

Pony ORM: Permite definir modelos y realizar consultas con sintaxis muy similar a Python.

SQLObject: También proporciona una interfaz de alto nivel para definir modelos y ejecutar consultas similares a SQL.

```sql
SELECT * FROM usuarios WHERE activo = 1;


