from datetime import date

class Visitante:
    def __init__(self, nombre, apellidos, fecha_nacimiento, curp, fecha_registro=None):
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.curp = curp
        self.numero_visitas = 0
        self.fecha_registro = fecha_registro if fecha_registro else date.today()


    def incrementar_visitas(self):
        self.numero_visitas += 1

    def aplicar_descuento(self, precio_base):
        if self.numero_visitas > 0 and self.numero_visitas % 5 == 0:
            return precio_base * 0.8  # 20% de descuento
        return precio_base

    def obtener_precio(self):
        if self.tipo == "adulto":
            precio_base = 100
        else:
            precio_base = 50
        return self.aplicar_descuento(precio_base)

    def mostrar_informacion(self):
        """Muestra la información completa del visitante."""
        print(f"Nombre: {self.nombre} {self.apellidos}")
        print(f"Fecha de Nacimiento: {self.fecha_nacimiento}")
        print(f"CURP: {self.curp}")
        print(f"Número de Visitas: {self.numero_visitas}")
        print(f"Fecha de Registro: {self.fecha_registro}")
