import os

def procesar_notas(nombre_archivo_entrada, nombre_archivo_salida):
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_entrada = os.path.join(directorio_actual, nombre_archivo_entrada)
    ruta_salida = os.path.join(directorio_actual, nombre_archivo_salida)

    with open(ruta_entrada, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()

    nueva_data = []
    for linea in lineas:
        partes = linea.strip().split('--')
        if len(partes) < 5:
            continue

        nombre = partes[0]
        nota1 = float(partes[1])
        nota2 = float(partes[2])
        nota3 = float(partes[3])

        nuevo_promedio = round((nota1 + nota2 + nota3) / 3, 1)
        estado = calcular_estado(nota1, nota2, nota3, nuevo_promedio)

        nueva_linea = f"{nombre}--{nota1}--{nota2}--{nota3}--{nuevo_promedio}--{estado}"
        nueva_data.append(nueva_linea)

    with open(ruta_salida, 'w', encoding='utf-8') as archivo_salida:
        for linea in nueva_data:
            archivo_salida.write(linea + '\n')


procesar_notas('archivo.txt', 'notas_resultado.txt')
