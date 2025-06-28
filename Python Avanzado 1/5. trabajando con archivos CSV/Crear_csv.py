import csv
import os

"""ruta sin destino"""
ruta = "csv_vacio.csv"
 
"""ruta absoluta (no recomendable)"""
ruta_absoluta = "C:\\Users\\PC Acer\\Documents\\GitHub\\CursoPython\\Curso_Python_Avanzado\\5. trabajando con archivos CSV\\csv_vacio.csv" 

"""obtener la ruta actual mediante os"""
ruta_absoluta_os = os.path.join(os.getcwd(), "csv_vacio.csv")


archivo_abierto = open(ruta, "w")
writer = csv.writer(archivo_abierto, delimiter=",")
archivo_abierto.close()