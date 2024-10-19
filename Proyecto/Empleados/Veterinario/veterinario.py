from Empleados.empleados import Empleados
from Empleados.Utils.roles import Rol

class Veterinario(Empleados):
    def __init__(self, nombre, apellidos, fecha_nacimiento, fecha_ingreso, rfc, curp, salario, horario):
        super().__init__(nombre, apellidos, fecha_nacimiento, fecha_ingreso, rfc, curp, salario, horario, rol=Rol.VETERINARIO)
   
    def tratar_animal(self, animal):
        print(f"{self.nombre} está tratando a {animal} en la especialidad de {self.especialidad}")

    
    def mostrar_informacion(self):
        super().mostrar_informacion()  
        print(f"Especialidad: {self.especialidad}")

    