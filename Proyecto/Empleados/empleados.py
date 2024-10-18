from time import strftime
from Empleados.Utils.roles import Rol
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
        self.fecha_ingreso_como_trabajador = fecha_ingreso_como_trabajador
        self.fecha_nacimiento = fecha_nacimiento
        self.curp = curp
        self.rfc = rfc
        self.salario = salario
        self.horario = horario
        self.rol = rol

    def mostrar_informacion(self):
        nombre_completo = f"{self.nombre} {self.apellidos}"
        info = f"\n - Nombre completo: {nombre_completo}, Fecha de Nacimiento: {self.fecha_nacimiento.strftime("%d/%m/%Y")}, Fecha de Ingreso: {self.fecha_ingreso.strftime("%d/%m/%Y")}, RFC: {self.rfc}, CURP: {self.curp}, Salario: {self.salario}, Horario: {self.horario},Rol: {self.rol}"
        return info
    
        