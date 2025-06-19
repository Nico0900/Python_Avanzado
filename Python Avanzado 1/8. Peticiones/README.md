# ¿Qué es una Petición HTTP?

Una **petición HTTP** es un mensaje que se envía desde un cliente a un servidor para iniciar una acción y obtener o enviar información. HTTP (HyperText Transfer Protocol) es el protocolo que hace posible esta comunicación entre servicios, basado en un modelo **cliente-servidor**.

---

## Características del Protocolo HTTP

- 📦 **Simple**: fácil de interpretar y usar.
- 🔧 **Extensible**: se puede ampliar para agregar nuevas funcionalidades.
- 🚫 **Sin estado** (*stateless*): no guarda datos entre múltiples peticiones, aunque permite gestionar sesiones.

---

## Componentes de una Petición HTTP

Una petición HTTP consta de tres partes principales:

1. **Línea de inicio**:
   - **Método**: Acción que se desea realizar (`GET`, `POST`, `PUT`, `DELETE`, etc.).
   - **Objetivo**: URL o recurso al que se accede.
   - **Versión**: Especifica el protocolo HTTP utilizado.

2. **Cabeceras (Headers)**:
   - Metadatos que proporcionan información adicional sobre la petición, como tipo de contenido, autenticación, etc.

3. **Cuerpo (Body)**:
   - Datos enviados al servidor, generalmente en peticiones `POST`, `PUT`, etc.

---

## Métodos HTTP Comunes

| Método  | Descripción                                         |
|---------|-----------------------------------------------------|
| `GET`   | Solicita datos del servidor.                        |
| `POST`  | Envía nuevos datos al servidor (crear recursos).   |
| `PUT`   | Modifica datos existentes en el servidor.           |
| `DELETE`| Elimina recursos del servidor.                     |

---

## Estructura de una Respuesta HTTP

1. **Línea de estado**:
   - Protocolo, código de estado (por ejemplo, `200 OK`) y descripción textual.

2. **Cabeceras (Headers)**:
   - Información adicional sobre la respuesta.

3. **Cuerpo (Body)**:
   - Contenido de la respuesta, como datos solicitados o mensajes de error.

---

## Códigos de Estado HTTP

| Código | Categoría              | Significado Principal                          |
|--------|------------------------|-----------------------------------------------|
| 1xx    | Informativos           | Proceso en curso.                             |
| 2xx    | Éxito                  | La petición fue procesada correctamente.      |
| 200    | OK                     | Petición exitosa.                             |
| 201    | Created                | Recurso creado con éxito (usado con `POST`).  |
| 3xx    | Redirección            | Se requiere acción adicional.                 |
| 4xx    | Error del cliente      | Problema en la solicitud del cliente.         |
| 400    | Bad Request            | Solicitud mal formada.                        |
| 401    | Unauthorized           | Autenticación requerida.                      |
| 403    | Forbidden              | No tiene permisos para acceder.               |
| 5xx    | Error del servidor     | Fallo interno en el servidor.                 |
| 500    | Internal Server Error  | Error general en el servidor.                 |

---

## HTTP vs HTTPS

- **HTTP**: Protocolo sin cifrado.
- **HTTPS**: Protocolo seguro, con una capa adicional de seguridad (SSL/TLS).

---

## ¿Qué es una API?

Una **API** (*Application Programming Interface*) es un conjunto de reglas y funciones que permiten que diferentes servicios o programas se comuniquen entre sí. Las API modernas suelen utilizar HTTP como medio de comunicación, usando los métodos mencionados.

### Endpoints

Un **endpoint** es una URL específica asociada a una función dentro de una API. Cada endpoint tiene asignado un **método HTTP** que define su comportamiento.

> 📌 Ejemplo de endpoint:
> `GET https://api.ejemplo.com/usuarios`

---

## Resumen

- Las **peticiones HTTP** permiten la comunicación entre servicios cliente-servidor.
- Cada petición tiene una estructura clara: método, headers, cuerpo.
- Las **respuestas HTTP** indican el resultado de la petición mediante códigos de estado.
- Las **APIs** utilizan peticiones HTTP para intercambiar datos mediante **endpoints**.

