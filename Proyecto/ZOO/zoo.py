from typing import List
from Empleados.empleados import Empleados
from Empleados.Guia.guia import Guia
from Empleados.Mantenimiento.mantenimiento import Mantenimiento
from Empleados.Veterinario.veterinario import Veterinario
from Animales.animales import Animales


class Zoo:
    lista_empleados: List[Empleados] = []
    lista_guias: List[Guia] = []
    lista_mantenimiento: List[Mantenimiento] = []
    lista_Veterinarios: List[Veterinario] = []
    lista_Animales: List[Animales] = []
    #lista_enfermedades_animales: List[] = []

    def __init__(self):
        
