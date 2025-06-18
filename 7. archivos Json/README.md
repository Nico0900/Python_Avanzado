# ¿Qué es JSON?

**JSON** (JavaScript Object Notation) es un formato de texto ligero utilizado para el **intercambio de datos entre servicios y aplicaciones**. A pesar de su nombre, no está limitado al lenguaje JavaScript y puede ser usado con prácticamente cualquier lenguaje de programación.

---

## Características de JSON

- ✅ **Sencillo** y fácil de leer.
- ✅ **Legible** tanto por humanos como por máquinas.
- ✅ No necesita codificación especial para enviarse o recibirse.
- ✅ Representa uno o varios objetos con una estructura clara.
- ✅ Muy utilizado en comunicación entre aplicaciones, APIs, y servicios web.

---

## Tipos de Datos Soportados

JSON puede manejar los siguientes tipos de datos:

| Tipo           | Ejemplo                        | Notas                                                |
|----------------|--------------------------------|------------------------------------------------------|
| String (cadena)| `"texto"`                      | Siempre entre comillas dobles.                       |
| Número         | `123`, `3.14`                  | Decimales usan punto como separador.                 |
| Booleano       | `true`, `false`                | En inglés, en minúscula y sin comillas.              |
| Nulo           | `null`                         | Representa ausencia de valor.                        |
| Lista (Array)  | `[1, "hola", true]`            | Entre corchetes `[]`, puede contener varios tipos.   |
| Objeto         | `{"clave": "valor"}`           | Entre llaves `{}`, con pares clave-valor.            |

---

## Estructura de un Objeto JSON

Dependiendo del lenguaje en el que se vaya a usar, se puede usar camelCase. Vamos a definir la llave string con camelCase, que quiere decir que, para identificar cada palabra de la llave, separo por la primera letra de la siguiente palabra en mayúscula. También se pueden escribir en snake case, que quiere decir que cada palabra se separa por un guion bajo de la siguiente. 

```json
{
  "nombre": "Juan",
  "edad": 30,
  "activo": true,
  "direccion": null,
  "hobbies": ["fútbol", "lectura", "cine"]
}
