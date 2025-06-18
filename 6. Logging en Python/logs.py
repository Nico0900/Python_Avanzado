import logging

"""
basicConfig(level=logging.DEBUG)
con esta funcion podemos cambiar la manera en que se muestran
o se gardan los logs definiendo su formato.

filename="ejemplo_logs.log" :   con esta parametro creamos un 
                                archivo.log que permire visualizar 
                                los logs.

filemode="w" :  con este parametro sobreescribirmos el archivo.log
                para que no se vuelvan a repetir los logging en el
                documento.                               
"""

logging.basicConfig(level=logging.DEBUG, filename="ejemplo-CAP6-logs.log", filemode="w")

logging.debug("log de debugging")
logging.info("log informativo")
logging.warning("log de advertencia")
logging.error("log de error")
logging.critical("log de error critico")