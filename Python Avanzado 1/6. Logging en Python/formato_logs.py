import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s ",
    # datefmt="%H:%M:%S" #parametro para la configuracion que muestre solo la hora.
)

"""ejemplo de logs con ingreso de variables"""
nombre="Paco"
logging.error(f"{nombre} creó el error")

"""logs por defecto"""
logging.warning("log de advertencia")
logging.error("log de error")
logging.critical("log de error critico")

"""ejemplos de logs de error en try"""
try:
    division = 2 % 0
except: 
    logging.error("division por cero")