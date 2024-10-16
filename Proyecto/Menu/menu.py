from typing import List
from Animales import animales
from Empleados import empleados
from Empleados.empleados import Empleados
from Empleados.Guia.guia import Guia
from Empleados.Mantenimiento.mantenimiento import Mantenimiento
from Empleados.Veterinario.veterinario import Veterinario
from Animales.animales import Animal
from datetime import datetime
from getpass import getpass

from Visitantes import visitantes
from Visitantes.descuento import Visitante
from ZOO.zoo import Zoo

class Menu:

    zoo: Zoo = Zoo()
    
    def login(self):
        intentos = 0
        while intentos < 5:
            print("*** BIENVENIDO ***")
            print("Inicia Sesión para continuar")
            usuario = input("Ingresa tu nombre de usuario: ")
            contrasenia = getpass("Ingresa tu contraseña: ")

            for administrador in self.zoo.lista_administradores:
                if administrador.usuario == usuario and administrador.contraseña == contrasenia:
                    print("Inicio de sesión exitoso.")
                    self.menu()
                    return
            intentos += 1
            print(f"Usuario o contraseña incorrectos. Te quedan {5 - intentos} intento(s).")
        
        print("Has excedido el número de intentos permitidos. Intente más tarde.")
    
    def menu(self):
        
        
        while True:
            print("\n** Menú **")
            print("1. Registrar Empleados")
            print("2. Registrar Animales")
            print("3. Registrar Visitas")
            print("4. Eliminar Empleados")
            print("5. Eliminar Animales")
            print("6. Consultar Empleados registrados")
            print("7. Consultar Animales registrados")
            print("8. Consultar Visitas registradas")
            print("9. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                self.registrar_empleado()
            elif opcion == '2':
                self.registrar_animal()
            elif opcion == '3':
                self.registrar_visita()
            elif opcion == '4':
                self.eliminar_empleado()
            elif opcion == '5':
                self.eliminar_animal()
            elif opcion == '6':
                self.consultar_empleados()
            elif opcion == '7':
                self.consultar_animales()
            elif opcion == '8':
                self.consultar_visitas()
            elif opcion == '9':
                print("Saliendo...")
                break
            else:
                print("Opción no válida, intenta de nuevo.")


            """   while True:
            print("\n** Menú **")
            print("1. Registrar Empleados")
            print("2. Registrar Visitas")
            print("3. Registrar Animales")
            print("4. Eliminar Empleados")
            print("5. Eliminar Animales")
            print("6. Consultar Empleados registrados")
            print("7. Consultar Animales registrados")
            print("8. Consultar Visitas registradas")
            print("9. Salir")

            opcion = input("Selecciona una opción: ")
            
            if opcion == "1":
                print("\nSeleccionaste Registrar un empleado \n")

                nombre = input("Ingresa el nombre del empleado: ")
                apellidos = input("Ingresa el apellidos del empleado: ")
                curp = input("Ingresa la curp del empleado: ")
                fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
                fecha_ingreso_como_trabajador = input("Fecha de ingreso (YYYY-MM-DD): ")
                rfc = input("RFC: ")
                curp = input("CURP: ")
                salario = float(input("Salario: "))
                horario = input("Horario: ")
                rol = input("Rol (Veterinario, Guía, Mantenimiento, Administración): ")
                #contrasenia = input("Ingresa la contraseña del empleado: ")

                empleado = Empleados(nombre, apellidos, fecha_nacimiento, fecha_ingreso_como_trabajador, rfc, curp, salario, horario, rol)
                empleados.append(empleado)
                print("Empleado registrado exitosamente.")

                #empleado = Empleados(nombre, apellido, curp, fecha_nacimiento, contrasenia)
                #self.empleados.append(empleado)
                #print("Empleado agregado correctamente")

            elif opcion == "2":
                print("\nSeleccionaste registrar una visita \n")
                
                nombre = input("Nombre: ")
                apellidos = input("Apellidos: ")
                fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
                curp = input("CURP: ")
                fecha_registro = input("Fecha de registro (YYYY-MM-DD): ")
                self.num_visitas = 0 
                
                visitante = Visitante(nombre, apellidos, fecha_nacimiento, curp, fecha_registro)
                visitantes.append(visitante)
                print("Visitante registrado exitosamente.")

            elif opcion == "3":#registrar animal
                print("\nSeleccionaste registrar un Animal \n")

                def registrar_animal():
                    tipo = input("Tipo de animal: ")
                    fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
                    fecha_llegada = input("Fecha de llegada al zoológico (YYYY-MM-DD): ")
                    frecuencia_alimentacion = input("Frecuencia de alimentación: ")
                    enfermedades = input("Enfermedades (separadas por comas): ").split(",")
                    tipo_alimentacion = input("Tipo de alimentación: ")
                    vacunas = input("¿Cuenta con vacunas? (Si/No): ").lower() == "si"
                    peso = float(input("Peso (kg): "))

                    animal = Animal(tipo, fecha_nacimiento, fecha_llegada, frecuencia_alimentacion, enfermedades, tipo_alimentacion, vacunas, peso)
                    animales.append(animal)
                    print("Animal registrado exitosamente.")

                #nombre = input("Ingresa el nombre del empleado que realizó el mantenimiento: ")
                #apellido = input("Ingresa el apellido del empleado que realizó el mantenimiento: ")
                #curp = input("Ingresa la curp del empleado que realizó el mantenimiento: ")
                #ano = int(input("Ingresa el año de nacimiento del empleado que realizó el mantenimiento: "))
                #mes = int(input("Ingresa el mes de nacimiento del empleado que realizó el mantenimiento: "))
                #dia = int(input("Ingresa el dia de nacimiento del empleado que realizó el mantenimiento: "))
                #fecha_nacimiento = datetime(ano, mes, dia)
                #contrasenia = input("Ingresa la contraseña del empleado que realizó el mantenimiento: ")
                #empleado_mantenimiento = Empleados(nombre, apellido, curp, fecha_nacimiento, contrasenia)

            elif opcion == "4":#elminar empleados
                print("\nSeleccionaste eliminar un empleado \n")


                curp = input("Ingresa la curp del empleado que deseas modificar: ")
                for empleado in self.empleados:
                    if empleado.curp == curp:
                        nombre = input("Ingresa el nuevo nombre del empleado: ")
                        apellido = input("Ingresa el nuevo apellido del empleado: ")
                        empleado.nombre = nombre
                        empleado.apellido = apellido
                        print("Empleado modificado correctamente")
                        return
                print("Empleado no encontrado")

            elif opcion == "5":#eliminar animal
                print("\nSeleccionaste eliminar un empleado \n")
                curp = input("Ingresa la curp del empleado que deseas eliminar: ")
                for empleado in self.empleados:
                    if empleado.curp == curp:
                        self.empleados.remove(empleado)
                        print("Empleado eliminado correctamente")
                        return
                print("Empleado no encontrado")

            elif opcion == "6":#consultar empleados
                print("\nSeleccionaste consultar las visitas \n")
                for visita in self.visitas:
                    print(f"Nombre: {visita.nombre} Apellido: {visita.apellido} CURP: {visita.curp} Fecha de nacimiento: {visita.fecha_nacimiento}")
                    print(f"Número de visitas: {self.num_visitas}")
                    self.num_visitas += 1
                    print("Visitas consultadas correctamente")
                    return

            elif opcion == "7":#consultar animales
                print("\nSeleccionaste consultar los empleados \n")
                for empleado in self.empleados:
                    print(f"Nombre: {empleado.nombre} Apellido: {empleado.apellido} CURP: {empleado.curp} Fecha de nacimiento: {empleado.fecha_nacimiento} Rol: {empleado.rol}")
                    print("Empleados consultados correctamente")
                    return
                
            elif opcion == "8":#consultar visitas
                print("\nSeleccionaste consultar los mantenimientos \n")
                for mantenimiento in self.mantenimientos:
                    print(f"Nombre: {mantenimiento.nombre} Apellido: {mantenimiento.apellido} CURP: {mantenimiento.curp} Fecha de nacimiento: {mantenimiento.fecha_nacimiento}")
                    print("Mantenimientos consultados correctamente")
                    return

            elif opcion == "9":#salir
                print("\nSaliendo del menú...")
                return

            else:
                print("\nOpción no válida. Intente de nuevo")
                break """

            

    

   