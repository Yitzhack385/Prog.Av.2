class Animal:
    def __init__(self, tipo_animal, fecha_nacimiento, fecha_llegada, peso, enfermedades, frecuencia_alimentacion, tipo_alimentacion, vacunas):
        self.tipo_animal = tipo_animal
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_llegada = fecha_llegada
        self.peso = peso
        self.enfermedades = enfermedades if enfermedades else []
        self.frecuencia_alimentacion = frecuencia_alimentacion
        self.tipo_alimentacion = tipo_alimentacion
        self.vacunas = vacunas

    def agregar_enfermedad(self, enfermedad):
        """Agrega una enfermedad a la lista."""
        self.enfermedades.append(enfermedad)

    def mostrar_informacion(self):
        print(f"Tipo de animal: {self.tipo_animal}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
        print(f"Fecha de llegada al zoológico: {self.fecha_llegada}")
        print(f"Peso: {self.peso} kg")
        print(f"Enfermedades: {', '.join(self.enfermedades) if self.enfermedades else 'Ninguna'}")
        print(f"Frecuencia de alimentación: {self.frecuencia_alimentacion}")
        print(f"Tipo de alimentación: {self.tipo_alimentacion}")
        print(f"Vacunas: {'Sí' if self.vacunas else 'No'}")