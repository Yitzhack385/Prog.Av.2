from .Utils.roles import Rol
from datetime import datetime

class Empleados:
    nombre: str
    apellidos: str
    fecha_ingreso_como_trabajador: datetime
    fecha_nacimiento: datetime
    curp: str
    rfc: str
    salario: float
    horario: int
    rol: Rol

    def __init__(self, nombre: str, apellidos: str, fecha_ingreso_como_trabajador: datetime, fecha_nacimiento: datetime, curp: str, rfc: str, horario: int, salario: float, rol: Rol):
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_ingreso_como_trabajador = datetime()
        self.fecha_nacimiento = datetime()
        self.curp = curp
        self.rfc = rfc
        self.salario = salario
        self.horario = horario
        self.rol = rol

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, 
        Apellidos: {self.apellidos}, 
        Fecha de ingreso como trabajador: {self.fecha_ingreso_como_trabajador},
        Fecha de nacimiento: {self.fecha_nacimiento},
        CURP: {self.curp},
        RFC: {self.rfc},
        Salario: {self.salario},
        Horario: {self.horario},
        Rol: {self.rol}
        )
        return info