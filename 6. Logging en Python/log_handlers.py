import logging

"""
Formato de muestra del logs

%(asctime)s 
    % = inicio de la connotacion especial.
    (asctime) = nombre del atributo a utilizar.
    s = indica que es String.

asctime : tiempo (%H:%M:%S).
name : nombre del atributo.
levelname : nivel de severidad.
message : mensaje a mostrar.

"""

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#controlador uno para formato del logs
handler_consola = logging.StreamHandler() #controlador
formato_logs = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s") #formato controlador
datefmt="%H:%M:%S" #formato hora - minutos - segundo
handler_consola.setFormatter(formato_logs) #añade el formato creado al controlador
logger.addHandler(handler_consola) #define a que logger pertenece el controlador que creamos

#controlador dos para escribir los logs en un archivo 
handler_archivo = logging.FileHandler("archivo-CAP6-logging.log") #Crea y nombra el archivo que almacena los logs
handler_archivo.setLevel(logging.ERROR) #nivel de severidad que se guardara en el archivo
handler_archivo.setFormatter(formato_logs) #mantiene el mismo formato
logger.addHandler(handler_archivo) #añadimos el handler al loger.

logger.error("registro informativo")
