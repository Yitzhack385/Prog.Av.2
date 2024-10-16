

class Visitante:
    PRECIO_ADULTO = 100
    PRECIO_NIÑO = 50
    DESCUENTO = 0.20

    def __init__(self, guia, visitantes, fecha_visita):
        self.guia = guia
        self.visitantes = visitantes
        self.fecha_visita = fecha_visita
        self.cantidad_adultos = 0
        self.cantidad_ninos = 0
        self.costo_total = 0

        # Calcular la cantidad de adultos y niños al crear la visita
        self.calcular_cantidad_visitantes()
        # Calcular el costo total de la visita
        self.calcular_costo_total()

    def calcular_cantidad_visitantes(self):
        """Determina cuántos adultos y cuántos niños hay en la visita."""
        for visitante in self.visitantes:
            edad = visitante.calcular_edad()
            if edad >= 18:
                self.cantidad_adultos += 1
            else:
                self.cantidad_ninos += 1

    def calcular_costo_total(self):
        """Calcula el costo total de la visita, aplicando descuentos si es necesario."""
        costo = 0
        for visitante in self.visitantes:
            if visitante.calcular_edad() >= 18:
                precio = self.PRECIO_ADULTO
            else:
                precio = self.PRECIO_NIÑO
            
            # Aplicar descuento si corresponde
            if visitante.tiene_descuento():
                precio -= precio * self.DESCUENTO

            costo += precio
            visitante.incrementar_visita()

        self.costo_total = costo

    def mostrar_informacion(self):
        print(f"Guía: {self.guia.nombre}")
        print(f"Fecha de la visita: {self.fecha_visita}")
        print(f"Cantidad de adultos: {self.cantidad_adultos}")
        print(f"Cantidad de niños: {self.cantidad_ninos}")
        print(f"Costo total de la visita: ${self.costo_total:.2f}")
        print(f"Número de Visitas: {self.numero_visitas}")