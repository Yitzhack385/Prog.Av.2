from Empleados.empleados import Empleados
from Empleados.Utils.roles import Rol

class Guia(Empleados):
    def __init__(self, nombre, apellidos, fecha_nacimiento, fecha_ingreso, rfc, curp, salario, horario, area):
        super().__init__(nombre, apellidos, fecha_nacimiento, fecha_ingreso, rfc, curp, salario, horario, rol=Rol.GUIA)
        self.area = area
        self.visitas_realizadas = 0

    def guiar_tour(self):
        print(f"{self.nombre} está guiando un tour en el área de {self.area}")

    def registrar_visita(self):
        self.visitas_realizadas += 1
        print(f"El guía {self.nombre} ha registrado {self.visitas_realizadas} visita(s).")
