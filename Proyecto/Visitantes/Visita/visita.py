class Visita:
    def __init__(self, guia, visitantes, costo_total, fecha_visita, num_ninos, num_adultos):
        self.guia = guia
        self.visitantes = visitantes
        self.costo_total = costo_total
        self.fecha_visita = fecha_visita
        self.num_ninos = num_ninos
        self.num_adultos = num_adultos

    def mostrar_informacion(self):
        print(f"Guía a cargo: {self.guia}")
        print(f"Visitantes: {[visitante.nombre + ' ' + visitante.apellidos for visitante in self.visitantes]}")
        print(f"Costo total de la visita: {self.costo_total}")
        print(f"Fecha de la visita: {self.fecha_visita}")
        print(f"Cantidad de niños: {self.num_ninos}")
        print(f"Cantidad de adultos: {self.num_adultos}")
        print("-" * 40)