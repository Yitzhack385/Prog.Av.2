from datetime import date
from typing import List
from Empleados.empleados import Empleados
from Empleados.Admin.admin import Administrador
from Empleados.Guia.guia import Guia
from Empleados.Mantenimiento.mantenimiento import Mantenimiento
from Empleados.Veterinario.veterinario import Veterinario
from Animales.animales import Animal 
from Visitantes.Visita.visita import Visita
from Visitantes.visitantes import Visitante


class Zoo:

    def __init__(self):
        self.lista_empleados: List[Empleados] = []
        self.lista_guias: List[Guia] = []
        self.lista_mantenimiento: List[Mantenimiento] = []
        self.lista_veterinarios: List[Veterinario] = []
        self.lista_administrador: List[Administrador] = []
        self.lista_animales: List[Animal] = []
        self.lista_visitantes: List[Visitante] = [] 
        self.lista_visitas: List[Visita] = []
        #self.lista_enfermedades_animales: List[] = []
    
 # Empleados
    def registrar_empleado(self, empleado: Empleados):
        if isinstance(empleado, Guia):
            self.lista_guias.append(empleado)
        elif isinstance(empleado, Mantenimiento):
            self.lista_mantenimiento.append(empleado)
        elif isinstance(empleado, Veterinario):
            self.lista_veterinarios.append(empleado)
        self.lista_empleados.append(empleado)
        print(f"Empleado {empleado.nombre} {empleado.apellidos} registrado con éxito en el rol {empleado.rol}")

    def eliminar_empleado(self, curp: str):
        for lista in [self.lista_guias, self.lista_mantenimiento, self.lista_veterinarios]:
            for empleado in lista:
                if empleado.curp == curp:
                    lista.remove(empleado)
                    self.lista_empleados.remove(empleado)
                    print(f"Empleado con CURP {curp} eliminado con éxito.")
                    return
        print(f"Empleado con CURP {curp} no encontrado.")

    def consultar_empleado(self, curp: str):
        for empleado in self.lista_empleados:
            if empleado.curp == curp:
                return empleado.mostrar_informacion()
        return f"Empleado con CURP {curp} no encontrado."

    def consultar_empleados_por_rol(self, rol: str):
        if rol.lower() == 'guia':
            return [empleado.mostrar_informacion() for empleado in self.lista_guias]
        elif rol.lower() == 'mantenimiento':
            return [empleado.mostrar_informacion() for empleado in self.lista_mantenimiento]
        elif rol.lower() == 'veterinario':
            return [empleado.mostrar_informacion() for empleado in self.lista_veterinarios]
        else:
            return f"No hay empleados registrados con el rol {rol}."
        
    def modificar_empleado(self, curp: str, nuevos_datos: dict):
        for empleado in self.lista_empleados:
            if empleado.curp == curp:
                for clave, valor in nuevos_datos.items():
                    setattr(empleado, clave, valor)       #clave = atributo, valor = nuevo valor --- salario: 6500
                print(f"Empleado {empleado.nombre} {empleado.apellidos} actualizado.")
                return
        print(f"No se encontró al empleado con CURP {curp}.")  

#---------------------------------------------------------

    #Animales
    
    def registrar_animal(self):
        tipo = input("Tipo de animal: ")
        fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
        fecha_llegada = input("Fecha de llegada al zoológico (YYYY-MM-DD): ")
        frecuencia_alimentacion = input("Frecuencia de alimentación: ")
        enfermedades = input("Enfermedades (separadas por comas): ").split(",")
        tipo_alimentacion = input("Tipo de alimentación: ")
        vacunas = input("¿Cuenta con vacunas? (Sí/No): ").lower() == "sí"
        peso = float(input("Peso (kg): "))

        animal = Animal(tipo, fecha_nacimiento, fecha_llegada, frecuencia_alimentacion, enfermedades, tipo_alimentacion, vacunas, peso)
        self.zoo.lista_animales.append(animal)
        print("Animal registrado exitosamente.")

    def eliminar_animal(self):
        index = int(input("Índice del animal a eliminar: "))
        if 0 <= index < len(self.zoo.lista_animales):
            self.zoo.lista_animales.pop(index)
            print("Animal eliminado exitosamente.")
        else:
            print("Índice no válido.")

    def consultar_animales(self):
        for animal in self.zoo.lista_animales:
            print(vars(animal))

#---------------------------------------------------------------------

    #Visitantes
    def registrar_visita(self):
        guia = input("Nombre del guía a cargo: ")
        curps_visitantes = input("CURPs de los visitantes (separados por comas): ").split(",")
        fecha_visita = input("Fecha de la visita (YYYY-MM-DD): ")
        
        visitantes_involucrados = [visitante for visitante in self.lista_visitantes if visitante.curp in curps_visitantes]
        
        num_ninos = sum(1 for visitante in visitantes_involucrados if (date.today().year - visitante.fecha_nacimiento.year) < 12)
        num_adultos = len(visitantes_involucrados) - num_ninos
        
        costo_total = sum(visitante.obtener_precio(es_adulto=(date.today().year - visitante.fecha_nacimiento.year) >= 12) for visitante in visitantes_involucrados)
        
        for visitante in visitantes_involucrados:
            visitante.incrementar_visitas()

        visita = Visita( guia, visitantes_involucrados, costo_total, fecha_visita, num_ninos, num_adultos)
        self.lista_visitas.append(visita)
        print("Visita registrada exitosamente.")

    def consultar_visitas(self):
        for visita in self.lista_visitas:
            visita.mostrar_informacion()
    
#------------------------------------------------------------------------------

"""
    
    
    
    def registrar_mantenimiento(self, mantenimiento):
        self.mantenimientos.append(mantenimiento)
        print(f"Mantenimiento registrado para el animal con ID {mantenimiento.animal_id}.")

    def registrar_animal(self, animal):
        self.animales.append(animal)
        print(f"Animal {animal.tipo_animal} registrado con éxito.")

    def eliminar_animal(self, id_animal):
        for animal in self.animales:
            if animal.id == id_animal:
                self.animales.remove(animal)
                print(f"Animal {animal.tipo_animal} eliminado.")
                return
        print(f"No se encontró el animal con ID {id_animal}.")
    
    def consultar_animales(self):
        for animal in self.animales:
            animal.mostrar_informacion()

    def modificar_animal(self, id_animal, nuevos_datos):
        for animal in self.animales:
            if animal.id == id_animal:
                animal.actualizar_datos(nuevos_datos)
                print(f"Animal {animal.tipo_animal} actualizado.")
                return
        print(f"No se encontró el animal con ID {id_animal}.")
    
    def consultar_visitantes(self):
        for visitante in self.visitantes:
            visitante.mostrar_informacion()
    
    def consultar_visitas(self):
        for visita in self.visitas:
            visita.mostrar_informacion()
    
    def consultar_mantenimientos(self):
        for mantenimiento in self.mantenimientos:
            mantenimiento.mostrar_proceso()

    def consultar_enfermedades_animales(self):
        for animal in self.animales:
            for enfermedad in animal.enfermedades:
                print(f"Enfermedad: {enfermedad.descripcion}, animal: {animal.tipo_animal}, fecha de inicio: {enfermedad.fecha_inicio}, fecha de culminación: {enfermedad.fecha_culminacion}")
"""
    

    
    
