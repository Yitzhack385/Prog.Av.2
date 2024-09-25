from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime
from random import randint

class Escuela:
    lista_estudiantes: List [Estudiante] = []
    lista_maestros: List [Maestro] = []
    lista_grupos: List [Grupo] = []
    lista_materias: List [Materia] = []

    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)

    def registrar_maestro(self, maestro: Maestro):
        self.lista.maestros.append(maestro)

    def registrar_materia(self, materia: Materia):
        self.lista_materias.append(materia)

    def lista_estudiantes(self):
        print("*** Estudiantes ***")

        for estudiante in self.lista_estudiantes:
            print(estudiante.mostrar_info_estudiante)

    def eliminar_estudiante(self, numero_control: str):
        for estudiante in self.estudiantes:
            if estudiante.numero_control == numero_control:
                self.lista_estudiantes.remove(estudiante)
                print("Estudiante eliminido")
                return
            
        print("Nose encontro el estudiante con numero de control: {numero_control}")


    def generar_numero_control(self):
        ano = datetime.now().year
        mes = datetime.now().month
        longitud_mas_uno = len(self.lista_estudiantes) + 1
        aleatorio = randint(0,10000)

        numero_control = f"{ano}{mes}{longitud_mas_uno}"

