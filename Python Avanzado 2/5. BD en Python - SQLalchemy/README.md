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

```sql
SELECT * FROM usuarios WHERE activo = 1;
