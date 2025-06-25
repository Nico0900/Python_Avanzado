class Persona:# CLASES SON PLANOS O PLANTILLAS DONDE SE CONSTRUYEN LOS OBSJETOS #

    tipo = "Humano" # ATRIBUTO : VALOR #

    """Constructor de la clase Persona dunder method (__init__)""" 
    def __init__(self, nombre, apellido, edad):
        """ self : inicializa la instancia de la clase. """
        """ nombre, apellido, edad : son los atributos de la clase """
        """ self.tipo : es un atributo de la clase que se comparte entre todas las instancias  """
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.documento_identidad = None

        """metodo constructor que se ejecuta al crear una instancia de la clase""" 
    def agregar_documento_identidad(self, numero_documento):
        """Metodo para agregar un documento de identidad a la instancia"""
        """ numero_documento : es el numero de documento que se le asigna a la instancia """
        """ self.documento_identidad : es el atributo de la clase que almacena el numero de documento """
        self.documento_identidad = numero_documento
        print("Documento guardado")

## EJEMPLO DE CLASE ##
## CREANDO UNA INSTANCIA DE LA CLASE PERSONA ## 
paco = Persona("Paco", "Botero", 27)
print(paco.tipo)
print("nombre : ", paco.nombre)
print("apellido : ", paco.apellido)
print("edad : ", paco.edad)
# AGREGANDO UN DOCUMENTO DE IDENTIDAD A LA INSTANCIA PACO #
paco.agregar_documento_identidad(1234)
