# Uso de la Librería `logging` en Python

Esta librería permite registrar eventos que ocurren durante la ejecución de un programa, ayudando en el proceso de depuración, monitoreo y análisis de errores.

## ¿Qué es `logging`?

`logging` es una librería **built-in** (incluida por defecto en Python) que permite crear registros del comportamiento de una aplicación en diferentes niveles de severidad.

## Niveles de Severidad

La librería maneja **cinco niveles de severidad** para los logs, los cuales permiten clasificar los mensajes según su importancia:

| Nivel     | Descripción |
|-----------|-------------|
| `DEBUG`   | Información detallada, útil durante el desarrollo     para depurar partes específicas del código. |
| `INFO`    | Información relevante sobre eventos que ocurren en el programa. |
| `WARNING` | Reporta algo inesperado o que podría causar problemas, pero que no detiene la ejecución. Este es el nivel por defecto. |
| `ERROR`   | Reporta errores que han impedido que una parte del código se ejecute correctamente. |
| `CRITICAL`| Reporta errores graves que pueden causar la detención completa del programa. |

> **Nota:** Para que se muestren logs con nivel `DEBUG` o `INFO`, es necesario configurarlo explícitamente en el código.

## Formato del Log

Cada mensaje de log contiene tres componentes, separados por dos puntos:

