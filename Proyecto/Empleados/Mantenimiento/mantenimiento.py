from Empleados.empleados import Empleados

class Mantenimiento(Empleados):
    def __init__(self, nombre, apellidos, fecha_nacimiento, fecha_ingreso, rfc, curp, salario, horario, zona_responsable):
        super().__init__(nombre, apellidos, fecha_nacimiento, fecha_ingreso, rfc, curp, salario, horario, "Mantenimiento")
        self.zona_responsable = zona_responsable

    def reparar_zona(self):
        print(f"{self.nombre} está reparando la zona de {self.zona_responsable}")
    