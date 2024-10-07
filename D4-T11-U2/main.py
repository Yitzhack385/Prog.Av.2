"""
- Estudiantes
- Maestros
- Horarios
- Grupos

"""

from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from materias.materia import Materia
from maestros.maestro import Maestro
from carrera.carrera import Carrera
from semestre.semestre import Semestre
from grupos.grupos import Grupos

from datetime import datetime

escuela = Escuela()

while True:
    print("\n Mindbox")
    print("1. Registrar estudiante")
    print("2. Registrar maestro")
    print("3. Registrar materia")
    print("4. Registrar grupo")
    print("5. Registrar horario")
    print("6 Mostrar estudiantes")
    print("7 Mostrar maestros")
    print("8 Mostrar materias")
    print("9 Mostrar grupos")
    print("10 Eliminar estudiante")
    print("11 Eliminar maestros")
    print("12 Eliminar materia")
    print("13. Salir")

    opcion = input("Ingresa una opcion para continuar: ")

    if opcion == "1":
        print("Seleccionaste la opcion para registrar un estudiante")

        numero_control = escuela.generar_numero_control()


        nombre = input("Ingresa el nombre: " )
        apellido = input("Ingresa el apellido del estudiante: ")
        curp = input("Ingresar la curp del estudiante: ")
        ano = int(input("Ingresa el ano de nacimiento del estudiante: "))
        mes = int(input("Ingresa el mes de nacimiento del estudiante: "))
        dia = int(input("Ingresa el dia de nacimiento del estudiante: "))
        fecha_nacimiento = datetime(ano, mes, dia)

        estudiante = Estudiante( numero_control = numero_control, nombre = nombre, apellido = apellido, curp = curp, fecha_nacimiento = fecha_nacimiento)
        escuela.registrar_estudiante(estudiante) 

        print("\nEstudiante registrado correctamente")

    elif opcion == "2":
        print("Seleccionaste la opcion para registrar un maestro")

        numero_control = escuela.generar_numero_control()

        print(numero_control)

        nombre = input("Ingresa el nombre: " )
        apellido = input("Ingresa el apellido del maestro: ")
        curp = input("Ingresar la curp del maestro: ")
        ano = int(input("Ingresa el ano de nacimiento del maestro: "))
        mes = int(input("Ingresa el mes de nacimiento del maestro: "))
        dia = int(input("Ingresa el dia de nacimiento del maestro: "))
        fecha_nacimiento = datetime(ano, mes, dia)

    elif opcion == "3":
        pass

    elif opcion == "4":
        pass

    elif opcion == "5":
        pass

    elif opcion == "6":
        escuela.listar_estudiantes()

    elif opcion == "7":
        escuela.listar_maestros()

    elif opcion == "8":
        escuela.listar_materias()

    elif opcion == "9":
        pass

    elif opcion == "10":
        print("Seleccionaste la opcion para eliminar un estudiante")

        numero_control = input("Ingrese el numero de control del estudiante")
        escuela.eliminar_estudiante(numero_control = numero_control)

    elif opcion == "11":
        print("Seleccionaste la opcion para eliminar un maestro")

        numero_control = input("Ingrese el numero de control del maestro")
        escuela.eliminar_maestro(numero_control = numero_control)

    elif opcion == "12":
        print("Seleccionaste la opcion para eliminar un materia")

        numero_control = input("Ingrese el numero de control del materia")
        escuela.eliminar_materia(numero_control = numero_control)

    elif opcion =="13":
        print("Hasta luego")
        break

