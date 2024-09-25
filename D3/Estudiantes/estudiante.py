from datetime import datetime

class Estudiante:
    numero_control: int
    nombre: str
    apellido: str
    curp: str
    fecha_nacimiento: datetime

    def __init__(self, nombre: str, apellido: str, curp: str, fecha_nacimiento: str):
        self.numero_control = "C21120576"
        self.nombre = nombre
        self.apellido = apellido
        self.curp = curp
        self.fecha_nacimiento = fecha_nacimiento
        

    def mostrar_info_estudiantes(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"Numero de control: {self.numero_control}, Nombre completo {nombre_completo}, Curp: {self.curp}, Fecha de nacimiento: {self.fecha_nacimiento}"
        return info
    