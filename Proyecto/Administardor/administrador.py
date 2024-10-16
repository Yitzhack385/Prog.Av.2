from Empleados.empleados import Empleados

class Mantenimiento(Empleados):
    def __init__(self, empleado, animal, proceso, fecha_proceso, observaciones=""):
        self.empleado = empleado
        self.animal = animal
        self.proceso = proceso  
        self.fecha_proceso = fecha_proceso
        self.observaciones = observaciones
    
    def mostrar_informacion_mantenimiento(self):
        print(f"Empleado a cargo: {self.empleado.nombre} {self.empleado.apellidos}")
        print(f"ID del animal: {self.animal.tipo_animal}")
        print(f"Proceso: {self.proceso}")
        print(f"Fecha del proceso: {self.fecha_proceso}")
        if self.observaciones:
            print(f"Observaciones: {self.observaciones}")