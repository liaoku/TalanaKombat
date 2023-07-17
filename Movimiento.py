

class Movimiento:
    nombre:str
    combinacion:str
    energia:int
    mensaje:str
    
    """ def __init__(self, nombre:str, combinacion:str, energia:int, mensaje:str):
        self.nombre = nombre
        self.combinacion = combinacion
        self.energia = energia
        self.mensaje = mensaje """
    
    def __str__(self): 
        return self.combinacion + " " + str(self.energia) + " " + self.mensaje