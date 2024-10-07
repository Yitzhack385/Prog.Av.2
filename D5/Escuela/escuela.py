from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime
from random import randint
from carrera.carrera import Carrera
from semestre.semestre import Semestre

class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_maestros: List[Maestro] = []
    lista_grupos: List[Grupo] = []
    lista_materias: List[Materia] = []
    lista_carreras: List[Carrera] = []
    lista_semestre: List[Semestre] = []


    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)

    def registrar_maestro(self, maestro: Maestro):
        self.lista.maestros.append(maestro)

    def registrar_materia(self, materia: Materia):
        self.lista_materias.append(materia)

    def listar_estudiantes(self):
        print("*** Estudiantes ***")

        for estudiante in self.lista_estudiantes:
            print(estudiante.mostrar_info_estudiante)

    def eliminar_estudiante(self, numero_control: str):
        for estudiante in self.estudiantes:
            if estudiante.numero_control == numero_control:
                self.lista_estudiantes.remove(estudiante)
                print("Estudiante eliminido")
                return
            
        print("\nNose encontro el estudiante con numero de control: {numero_control}")

    def listar_maestros(self):
        print("*** Maestros ***")

        for maestro in self.lista_maestros:
            print(maestro.mostrar_info_maestro)
    
    def eliminar_maestro(self, numero_control: str):
        for maestro in self.maestros:
            if maestro.numero_control == numero_control:
                self.lista_maestros.remove(maestro)
                print("Maestro eliminido")
                return
            
        print("\nNo se encontro el maestro con numero de control: {numero_control}")

    def listar_materias(self):
        print("*** Materias ***")

        for materia in self.lista_materias:
            print(materia.mostrar_info_materia) 

    def eliminar_materia(self, numero_control: str):
        for materia in self.materias:
            if materia.numero_control == numero_control:
                self.lista_materias.remove(materia)
                print("Materia eliminido")
                return
            
        print("\nNo se encontro el materia con numero de control: {numero_control}")       
    


    def generar_numero_control(self):
        ano = datetime.now().year
        mes = datetime.now().month
        longitud_mas_uno = len(self.lista_estudiantes) + 1
        aleatorio = randint(0,10000)

        numero_control = f"{ano}{mes}{longitud_mas_uno}{aleatorio}"

        return numero_control
    
    def generar_numero_control_maestro(self, rfc: str) -> str:
        ano = datetime.now().year
        dia_actual = datetime.now().day
        longitud_mas_uno = len(self.lista_maestros) + 1
        ultimas_letras_rfc = rfc[-2:]
        aleatorio = randint(500, 5000)
        numero_control_maestro = f"{ano}{dia_actual}{longitud_mas_uno}{ultimas_letras_rfc}{aleatorio}"
        
        return numero_control_maestro
    


