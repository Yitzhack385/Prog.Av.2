from datetime import datetime

# Clase ProcesoAnimal
class ProcesoAnimal:
    def __init__(self, empleado, animal_id, tipo_proceso, fecha_proceso, observaciones=None):
        self.empleado = empleado  
        self.animal_id = animal_id
        self.tipo_proceso = tipo_proceso
        self.fecha_proceso = fecha_proceso
        self.observaciones = observaciones

    def mostrar_proceso(self):
        print(f"Empleado a cargo: {self.empleado.nombre} (Mantenimiento)")
        print(f"ID del animal: {self.animal_id}")
        print(f"Tipo de proceso: {self.tipo_proceso}")
        print(f"Fecha del proceso: {self.fecha_proceso}")
        if self.observaciones:
            print(f"Observaciones: {self.observaciones}")