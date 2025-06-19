# ¿Qué es el Debugging y Para Qué Sirve?

## 🐞 ¿Qué es un "bug"?

En informática, un **bug** es un **error o falla** en el funcionamiento de un sistema, programa o aplicación. El término proviene de la palabra inglesa *bug* (bicho) y fue popularizado por **Grace Murray Hopper**, quien documentó que una falla en el hardware fue causada literalmente por un insecto dentro de un componente del computador.

---

## 🛠 ¿Qué es el Debugging?

**Debugging** (en español, *depuración*) es el proceso de:

1. **Identificar errores o fallas** en un programa.
2. **Analizar el comportamiento** del código paso a paso.
3. **Corregir los errores** para asegurar que el programa funcione correctamente.

Es una actividad esencial en el ciclo de desarrollo de software, y suele realizarse de manera **manual y controlada**, especialmente en entornos de desarrollo y pruebas.

---

## 🧪 Debugging en Python

Python incluye herramientas nativas para hacer debugging, sin necesidad de instalar librerías externas. Una de las principales es:

### 📦 `pdb` - Python Debugger

La librería **`pdb`** (Python Debugger) permite:

- Ejecutar el código **paso a paso**.
- **Inspeccionar variables** en tiempo real.
- Detener la ejecución en **puntos de interrupción**.
- **Analizar el flujo del programa** desde la consola.

### Ejemplo básico con `pdb`:

```python
import pdb

def suma(a, b):
    pdb.set_trace()  # Punto de interrupción
    resultado = a + b
    return resultado

print(suma(2, 3))
