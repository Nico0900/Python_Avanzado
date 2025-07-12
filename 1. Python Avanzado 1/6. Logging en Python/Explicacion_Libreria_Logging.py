"""
esta libreria es un proceso que hacer 
refenencia a los registros del programa

la libreria que contiene python se llama "built-in"
"loggin"

contiene niveles de debe ser creado con niveles de seguridad 

existen 5 niveles de seguridad

DEBUG :     es una información detallada que usualmente 
            usa mientras se esta desarrollando en partes 
            del codigo que debemos revisar.

INFO :      es el reporte de eventos de los cuales se requiere
            información.

WARNING :   es un reporte de algo inesperado que ah sucedido
            o va a seceder en el codigo, sin embargo esto no
            genera ningun error.

ERROR :     es un reporte de algo que no se pudo ejecutar por
            que ocurrio algo en el codigo.

CRITICAL :  es un reporte de un error grave; puede indicar que
            que el programa se detendra por un error. por defecto
            la libreria logging genera warnings como el primer 
            nivel.

Nota : para usar DEBUG o INFO es necesario definirlo desde el codigo.


cada log contiene 3 partes y cada una esta separada en dos partes
(Nivel:logger:mensaje)

Nivel : severidad del log (debug, info, warning, error, critical)
Logger : por defecto es root
Mensaje : este es el mensaje que enviamos a la funcion como argumento

    Ejemplos 
        WARNING:root:log de advertencia
        ERROR:root:log de error
        CRITICAL:root:log de error critico
"""