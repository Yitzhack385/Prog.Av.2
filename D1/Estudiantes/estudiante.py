from datetime import datetime

class Estudiante:
    Numero_control: int
    Nombre: str
    Apellido: str
    Curp: str
    Fecha_nacimiento: datetime

    def __init__(self, Nombre: str, Apellido: str, Curp: str, Fecha_nacimiento: str):
        self.Numero_control = "C21120576"
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Curp = Curp
        self.Fecha_nacimiento = Fecha_nacimiento
        

