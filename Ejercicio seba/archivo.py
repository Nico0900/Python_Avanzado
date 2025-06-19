def calcular_estado(n1, n2, n3, promedio):
    if 0.0 in (n1, n2, n3):
        return "EXAMEN"
    if promedio >= 4.0:
        return "APROBADO"
    elif 3.7 <= promedio <= 3.9:
        return "EXAMEN"
    else:
        return "REPROBADO"

def procesar_notas(nombre_archivo_entrada, nombre_archivo_salida):
    with open(nombre_archivo_entrada, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()

    nueva_data = []
    for linea in lineas:
        partes = linea.strip().split('--')
        if len(partes) < 5:
            continue  # línea malformada

        nombre = partes[0]
        nota1 = float(partes[1])
        nota2 = float(partes[2])
        nota3 = float(partes[3])
        
        nuevo_promedio = round((nota1 + nota2 + nota3) / 3, 1)
        estado = calcular_estado(nota1, nota2, nota3, nuevo_promedio)

        nueva_linea = f"{nombre}--{nota1}--{nota2}--{nota3}--{nuevo_promedio}--{estado}"
        nueva_data.append(nueva_linea)

    with open(nombre_archivo_salida, 'w', encoding='utf-8') as archivo_salida:
        for linea in nueva_data:
            archivo_salida.write(linea + '\n')

# Llamada principal
procesar_notas('archivo.txt', 'notas_resultado.txt')
