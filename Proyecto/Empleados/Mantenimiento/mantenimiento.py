from Empleados.empleados import Empleados
from Empleados.Utils.roles import Rol

class Mantenimiento(Empleados):
    def __init__(self, nombre, apellidos, fecha_nacimiento, fecha_ingreso, rfc, curp, salario, horario):
        super().__init__(nombre, apellidos, fecha_nacimiento, fecha_ingreso, rfc, curp, salario, horario,  rol=Rol.MANTENIMIENTO)
        

    def realizar_mantenimiento(self):
        print(f"{self.nombre} está realizando mantenimiento.")

    """
    def reparar_zona(self):
        print(f"{self.nombre} está reparando la zona de {self.zona_responsable}")
    """