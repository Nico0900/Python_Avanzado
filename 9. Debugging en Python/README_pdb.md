# Depuración en Python con `pdb`

Este proyecto explora el uso de la biblioteca de depuración integrada de Python, `pdb`, a través de ejemplos prácticos como el cálculo del área de un cuadrado. Aquí aprenderás a utilizar `pdb` para inspeccionar variables, establecer puntos de interrupción (*breakpoints*), y controlar el flujo de ejecución del código paso a paso.

---

## 📄 Creando el primer archivo con `pdb`

Para iniciar con la librería de depuración `pdb`, usaremos un archivo llamado `area_cuadrado.py`, que contiene una función para calcular el área de un cuadrado a partir del valor de uno de sus lados. Luego, iteramos sobre una lista de tres lados para generar una lista con sus respectivas áreas.

Cuando ejecutamos este archivo con:

```bash
python area_cuadrado.py
```

no veremos salida alguna, ya que no se utiliza `print`.

Para depurarlo, usamos:

```bash
python -m pdb area_cuadrado.py
```

Esto abrirá la consola de depuración `pdb`, donde veremos el código detenido. Desde allí podremos inspeccionar el flujo del programa línea a línea con comandos como:

- `l` (list): lista las líneas alrededor de donde está detenido el código.
- `q` (quit): salir de la depuración.

---

## ⛔ Uso de *breakpoints* con `pdb`

Los *breakpoints* permiten pausar la ejecución del código en líneas específicas. Para establecer un *breakpoint*, usamos el comando:

```bash
break 8
```

Esto detendrá la ejecución en la línea 8. Podemos comprobarlo con:

```bash
l
```

La línea 8 mostrará una `B` indicando que tiene un *breakpoint*.

Para continuar con la ejecución hasta el siguiente *breakpoint*, usamos:

```bash
continue
```

Otros comandos útiles:

- `next`: ejecuta la siguiente línea sin necesidad de *breakpoints* adicionales.
- `continue`: sigue la ejecución hasta el próximo *breakpoint* o finaliza si no hay más.

---

## 🔍 Inspección de variables y funciones

`pdb` permite inspeccionar variables sin necesidad de `print`, usando el comando `display`.

Ejemplo:

```bash
display lado_cuadrados
```

Si aún no ha sido declarada, mostrará un error. Tras avanzar con:

```bash
continue
```

la variable será visible una vez ejecutada la línea correspondiente.

También podemos inspeccionar variables del ciclo `for`, como:

```bash
display lado
```

Para dejar de mostrar una variable:

```bash
undisplay lado
```

Finalmente, para reiniciar el proceso de depuración sin perder los *breakpoints*:

```bash
restart
```

---

## 📚 Recursos adicionales

Para más comandos y funcionalidades, consulta la [documentación oficial de `pdb`](https://docs.python.org/3/library/pdb.html).

---

## 🛠 Requisitos

- Python 3.x

---

## 🚀 Ejecución rápida

```bash
python -m pdb area_cuadrado.py
```

¡Explora, depura y entiende mejor cómo funciona tu código Python paso a paso!