

class Maestro:
    Numero_control: int
    Nombre: str
    Apellido: str
    RFC: str
    Sueldo: float

    def __init__(self, Nombre: str, Apellido: str, RFC: str, Sueldo: float):
        self.Numero_control = ""
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.RFC = RFC
        self.Sueldo = Sueldo