from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from materias.materia import Materia
from maestros.maestro import Maestro
from carrera.carrera import Carrera
from semestre.semestre import Semestre
from grupos.grupos import Grupo
from datetime import datetime

class Menu:
    escuela = escuela = Escuela()

    usuario_estudiante: str
    contrasenia_estudiante: str

    usuario_maestro: str
    contrasenia_maestro: str

    def login(self):
        intentos = 0

        while intentos < 5:

            print("\n*** BIENVENIDO ***")
            print("Inicia Seción para Continuar")

            nombre_usuario = input("Ingresa tu nombre de usuario")
            contrasenia_usuario = input("Ingrese tu contraseña")

            if nombre_usuario == self.usuario_estudiante:
                if contrasenia_usuario == self.contrasenia_estudiante:
                    self.mostrar_menu_estudiante()
                else:
                    intentos = self.mostrar_intento_sesion_fallido(intentos_usuario = intentos)

            elif nombre_usuario == self.usuario_maestro:
                if contrasenia_usuario == self.contrasenia_maestro:
                    self.mostrar_menu_maestro()
                else:
                    intentos = self.mostrar_intento_sesion_fallido(intentos_usuario = intentos)

            else:
                intentos = self.mostrar_intento_sesion_fallido(intentos_usuario = intentos)
        
        print("Maximos intentos alcanzados")

    def mostrar_intento_sesion_fallido(self, intentos_usuario):
        print("\nUsuario o Contraseña incorrectos. Intenta de nuevo")
        return intentos_usuario + 1

    def mostrar_menu_estudiante(self):
        opcion = 0
        while opcion != 3:
            print("\n** Mindbox **")
            print("1. Ver horrario")
            print("2. Ver grupo")
            print("3. Salir")

            opcion = int(input("Ingresa una opcion"))

            if opcion == 3:
                break

    def mostrar_menu_maestro(self):
        opcion = 0
        while opcion != 3:
            print("\n** Mindbox **")
            print("1. Ver horrarios")
            print("2. Ver grupos")
            print("3. Ver materias")
            print("4. Ver alumnos")
            print("5. Salir")

            opcion = int(input("Ingresa una opcion"))

            if opcion == 5:
                break


    def mostrar_menu(self):

        
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
            print("13 Registrar carrera")
            print("14 Registrar semestre")
            print("15 Mostrar carreras")
            print("16. Salir")

            opcion = input("Ingresa una opcion para continuar: ")

            if opcion == "1":
                print("Seleccionaste la opcion para registrar un estudiante")

                numero_control = self.escuela.generar_numero_control()


                nombre = input("Ingresa el nombre: " )
                apellido = input("Ingresa el apellido del estudiante: ")
                curp = input("Ingresar la curp del estudiante: ")
                ano = int(input("Ingresa el ano de nacimiento del estudiante: "))
                mes = int(input("Ingresa el mes de nacimiento del estudiante: "))
                dia = int(input("Ingresa el dia de nacimiento del estudiante: "))
                fecha_nacimiento = datetime(ano, mes, dia)

                estudiante = Estudiante( numero_control = numero_control, nombre = nombre, apellido = apellido, curp = curp, fecha_nacimiento = fecha_nacimiento)
                self.escuela.registrar_estudiante(estudiante) 

                print("\nEstudiante registrado correctamente")

            elif opcion == "2":
                print("Seleccionaste la opcion para registrar un maestro")


                nombre_maestro = input("Ingresa el nombre del maestro: " )
                apellido_maestro = input("Ingresa el apellido del maestro: ")
                rfc_maestro = input("Ingresar el rfc del maestro: ")
                sueldo_maestro = float(input("Ingresa el sueldo del maestro"))
                ano = int(input("Ingresa el ano de nacimiento del maestro: "))
                mes = int(input("Ingresa el mes de nacimiento del maestro: "))
                dia = int(input("Ingresa el dia de nacimiento del maestro: "))
                fecha_nacimiento = datetime(ano, mes, dia)

                numero_control_maestro = self.escuela.generar_numero_control_maestro
                nuevo_maestro = Maestro(numero_control = numero_control_maestro)
                self.escuela.registrar_maestro(nuevo_maestro)

                print(f"\nMaestro registrado correctamente")

            elif opcion == "3":
                print("Seleccionaste la opcion para registrar un materia")


                nombre_materia = input("Ingresa el nombre de la materia: " )
                descripcion_materia = input("Ingrese la descripción de la materia: ")
                semestre_materia = int(input("Ingrese el semestre de : "))
                creditos_materia = int(input("Ingrese los creditos de la materia: "))

                nueva_materia = Materia(nombre = nombre_materia, descripcion_materia = descripcion_materia)
                self.escuela.registrar_materia(nueva_materia)

                print("\nMateria registrada correctamente")

            elif opcion == "4":
                print("\nSeleccionaste la opcion de registrar un grupo")

                tipo = input("Ingresa el tipo de grupo (A/B)")
                id_semestre = input("Ingresa el ID del semestre al que : ")

                grupo = Grupo(tipo = tipo, id_semestre = id_semestre)
                self.escuela.registrar_grupo(grupo = grupo)

            elif opcion == "5":
                print("hla")
                for semestre in self.escuela.lista_carreras:
                    print(semestre.matricula)

            elif opcion == "6":
                self.escuela.listar_estudiantes()

            elif opcion == "7":
                self.escuela.listar_maestros()

            elif opcion == "8":
                self.escuela.listar_materias()

            elif opcion == "9":
                pass

            elif opcion == "10":
                print("\nSeleccionaste la opcion para eliminar un estudiante")

                numero_control = input("Ingrese el numero de control del estudiante")
                self.escuela.eliminar_estudiante(numero_control = numero_control)

            elif opcion == "11":
                print("\nSeleccionaste la opcion para eliminar un maestro")

                numero_control = input("Ingrese el numero de control del maestro")
                self.escuela.eliminar_maestro(numero_control = numero_control)

            elif opcion == "12":
                print("\nSeleccionaste la opcion para eliminar un materia")

                numero_control = input("Ingrese el numero de control del materia")
                self.escuela.eliminar_materia(numero_control = numero_control)

            elif opcion == "13":
                print("\nSeleccionaste la opcion para registrar una carrera")

                nombre = input("Ingresa el nombre de la carrera")
                carrera = Carrera(nombre = nombre)
                self.escuela.registrar_carrera(carrera = carrera)

            elif opcion == "14":
                print("\nSeleccionaste la opcion para registrar un semestre")

                numero = input("Ingresa el numero del semestre")
                id_carrera = input("Ingresa el ID de la carrera")

                semestre = Semestre(numero = numero, id_carrera = id_carrera)
                self.escuela.registrar_semestre(semestre = semestre)

            elif opcion == "15":
                pass

            elif opcion =="16":
                print("Hasta luego")
                break

