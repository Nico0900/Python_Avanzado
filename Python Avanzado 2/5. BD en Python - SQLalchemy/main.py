from modelos import Departamento, Empleado
from conexion import engine, ModeloBase, session


def guardar_datos():
    contabilidad = Departamento("Contabilidad")
    session.add(contabilidad)
    tecnologia = Departamento("Tecnología")
    session.add(tecnologia)
    session.commit()

    emilio = Empleado("Emilio", "Tafur", "123", contabilidad.id)
    session.add(emilio)
    javier = Empleado("Javier", "Quiñonez", "1234", tecnologia.id)
    session.add(javier)
    session.commit()

    print(contabilidad.id)

if __name__ == "__main__":
    ModeloBase.metadata.create_all(engine)
    guardar_datos()
