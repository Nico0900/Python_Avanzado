# Programación Orientada a Objetos (POO) en Python

La **programación orientada a objetos (POO)** es un paradigma muy utilizado en el desarrollo de software.  
En este enfoque, **todos los datos y elementos** con los cuales trabajamos están representados por **objetos**.

## ¿Qué es un Objeto?

Un **objeto** es una representación de algo del mundo real. Usar objetos nos permite **modelar y abstraer problemas reales**, lo cual se conoce como **abstracción**.

En programación, los objetos se crean a partir de **clases**, que actúan como modelos o planos.

---

## Conceptos Clave

- **Clase**: Modelo o plantilla desde la cual se crean los objetos.
- **Objeto**: Instancia de una clase. Cada objeto tiene características y comportamientos.
- **Atributos**: Representan las **características** de un objeto.
- **Métodos**: Representan los **comportamientos** o acciones que puede realizar el objeto.

---

## Ejemplo en Python

```python
class Empleado:
    def __init__(self, nombre, apellido, horas_trabajadas):
        self.nombre = nombre
        self.apellido = apellido
        self.horas_trabajadas = horas_trabajadas

    def trabajar(self, horas):
        self.horas_trabajadas += horas
