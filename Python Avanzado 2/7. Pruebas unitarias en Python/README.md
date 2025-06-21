# Pruebas Unitarias en Python

## ¿Qué son las Pruebas Unitarias?

Las **pruebas unitarias** son una técnica de desarrollo utilizada para **detectar y evitar errores** en el código. Se enfocan en probar de forma aislada cada unidad funcional del programa, como funciones, métodos o clases, asegurando que funcionen correctamente de manera individual.

---

## ¿Por qué son importantes?

- ✅ **Garantizan la calidad del código.**
- ✅ **Verifican que el código se comporta como se espera.**
- ✅ **Previenen errores semánticos y lógicos.**
- ✅ **Facilitan el mantenimiento y la refactorización.**
- ✅ **Permiten detectar errores antes de que lleguen a producción.**

---

## ¿Qué se debe probar?

Cuando escribimos pruebas unitarias, debemos cubrir:

- **Todas las unidades del código:** funciones, métodos, clases.
- **Todas las posibilidades:** condiciones verdaderas y falsas, entradas válidas e inválidas.
- **Casos extremos y errores esperados.**

```python
def es_par(n):
    return n % 2 == 0

# Casos de prueba:
# - n = 2  → True
# - n = 3  → False
# - n = 0  → True
