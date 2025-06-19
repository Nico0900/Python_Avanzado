class Persona:
    def __init__(self, nombre:str, poscion:int) -> None:
        self.nombre = nombre
        self.posicion = poscion

    def caminar(self, distancia_km : int) -> int:
        self.posicion += distancia_km
        return self.posicion
    
paco = Persona(nombre="Paco", poscion=0)
posicion_paco = paco.caminar(distancia_km=6)
        