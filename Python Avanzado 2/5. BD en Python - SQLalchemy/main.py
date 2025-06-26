from modelos import Departamento, Empleado
"""importamos los modelos Departamento y Empleado desde el archivo modelos.py"""
from conexion import engine, ModeloBase, session
"""importamos el motor de la base de datos, la clase base para los modelos y la sesion desde el archivo conexion.py"""


"""creamos la funcion guardar_datos que se encarga de insertar datos en la base de datos"""
def guardar_datos():
    contabilidad = Departamento("Contabilidad")
    """creamos un objeto Departamento con el nombre 'Contabilidad'"""
    session.add(contabilidad)
    """agregamos el departamento de contabilidad a la sesion"""
    tecnologia = Departamento("Tecnología")
    """creamos un objeto Departamento con el nombre 'Tecnología'"""
    session.add(tecnologia)
    """agregamos el departamento de tecnologia a la sesion"""
    session.commit()
    """guardamos los cambios en la base de datos"""

    emilio = Empleado("Emilio", "Tafur", "123", contabilidad.id)
    session.add(emilio)
    javier = Empleado("Javier", "Quiñonez", "1234", tecnologia.id)
    """creamos un objeto Empleado con el nombre 'Emilio', apellido 'Tafur', documento '123' y el id del departamento de contabilidad"""
    session.add(javier)
    """agregamos el empleado Emilio a la sesion"""
    session.commit()
    """guardamos los cambios en la base de datos"""

    print(contabilidad.id)
    """imprimimos el id del departamento de contabilidad"""


def hacer_consultas():
    departamento_1 = session.get(Departamento, 1)
    """obtenemos el departamento con id 1"""
    print(departamento_1)

    cantidad_departamentos = session.query(Departamento).count()
    """obtenemos la cantidad de departamentos en la base de datos"""
    print("Cantidad de departamentos:", cantidad_departamentos)
    """imprimimos la cantidad de departamentos"""
    print(cantidad_departamentos)

    empleados_contabilidad = session.query(Empleado).filter_by(
        id_departamento=departamento_1.id
    ).first()
    """obtenemos el primer empleado del departamento de contabilidad"""
    """filtramos los empleados por el id del departamento de contabilidad"""
    print(empleados_contabilidad)
    """imprimimos el empleado de contabilidad"""
    for empleado in empleados_contabilidad:
        print(empleado)
    """iteramos sobre los empleados de contabilidad e imprimimos cada empleado"""


if __name__ == "__main__":
    """este bloque se ejecuta si el script se ejecuta directamente"""
    ModeloBase.metadata.create_all(engine)
    """creamos las tablas en la base de datos"""
    # guardar_datos()
    # hacer_consultas()
    """llamamos a las funciones guardar_datos() y hacer_consultas()
    para insertar datos y realizar consultas en la base de datos """

"""
    [ if  __name__ == "__main__": ]

Este bloque se ejecuta si el script se ejecuta directamente, creando las tablas en la base de datos y llamando a las funciones guardar_datos() y hacer_consultas()
"""