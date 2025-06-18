def funcion_kwargs(**kwargs):
    ##solo muestra lo que contenga kwargs
    print(kwargs)

    #El cilo for muestra en pantalla todo lo que exista dentro de Kwargs
    for llave, valor in kwargs.items():
        print(f"llave : {llave}, valor : {valor}")
    
    #imprime el valor del nombre segun sea llamado
    print(kwargs["nombre"], kwargs["apellido"])
    print(kwargs["nombre"])
    print(kwargs["apellido"])

funcion_kwargs(
    nombre = "Paco",
    apellido = "Botero",
    )