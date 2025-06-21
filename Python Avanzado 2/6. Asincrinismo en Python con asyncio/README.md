# Programación Asíncrona en Python

## Introducción

La programación asíncrona es una técnica que permite ejecutar múltiples tareas al mismo tiempo, mejorando la eficiencia y reduciendo el tiempo de espera, especialmente cuando se manejan tareas de entrada/salida como llamadas a APIs, lectura de archivos o consultas a bases de datos.

Antes de entender cómo funciona, es importante diferenciarla de la programación tradicional:

---

## Programación Síncrona

En la **programación síncrona**, el código se ejecuta de forma **secuencial**.  
Cada instrucción debe esperar a que la anterior finalice para comenzar su ejecución.

```python
print("Inicio")
respuesta = obtener_datos()
print("Fin")  # Esto no se ejecuta hasta que obtener_datos() finalice
