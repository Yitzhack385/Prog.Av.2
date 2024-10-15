from Empleados.empleados import Empleados
from Empleados.Utils.roles import Rol

class Administracion(Empleados):
    def __init__(self, nombre, apellidos, fecha_nacimiento, fecha_ingreso, rfc, curp, salario, horario, departamento):
        super().__init__(nombre, apellidos, fecha_nacimiento, fecha_ingreso, rfc, curp, salario, horario, "Administración")
        self.departamento = departamento

    def gestionar_departamento(self):
        print(f"{self.nombre} está gestionando el departamento de {self.departamento}")