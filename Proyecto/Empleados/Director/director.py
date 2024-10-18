from Empleados.empleados import Empleados
from Empleados.Utils.roles import Rol
from datetime import datetime

class Director(Empleados):
    def __init__(self, nombre: str, apellidos: str, fecha_ingreso_como_trabajador: datetime, fecha_nacimiento: datetime, curp: str, rfc: str, horario: int, salario: float, usuario: str, contrasenia: str):
        super().__init__(nombre, apellidos, fecha_ingreso_como_trabajador, fecha_nacimiento, curp, rfc, horario, salario, rol=Rol.DIRECTOR)
        self.usuario = usuario
        self.contrasenia = contrasenia

    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        return f"{info}, Usuario: {self.usuario}"