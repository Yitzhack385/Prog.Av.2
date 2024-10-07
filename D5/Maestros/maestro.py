#numero_control nombre apellido rfc sueldo

class Maestro:
    numero_control: int
    nombre: str
    apellido: str
    rfc: str
    sueldo: float

    def __init__(self, numero_control: int, nombre: str, apellido: str, rfc: str, sueldo: float):
        self.numero_control = numero_control
        self.nombre = nombre
        self.apellido = apellido
        self.rfc = rfc
        self.sueldo = sueldo