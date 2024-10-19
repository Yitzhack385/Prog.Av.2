
import bcrypt

from ZOO.zoo import Zoo

class Menu:

    def __init__(self, zoo: Zoo):
        self.zoo = zoo
        self.intentos_fallidos = 0
        self.bloqueado_hasta = None

    def verificar_contrasenia(self, contrasenia, hash_contrasenia):
        return bcrypt.checkpw(contrasenia.encode('utf-8'), hash_contrasenia)
    
    def login(self):
        intentos = 0
        while intentos < 5:
            print("*** BIENVENIDO ***")
            print("Inicia Sesión para continuar")
            usuario = input("Ingresa tu nombre de usuario: ")
            contrasenia = input("Ingresa tu contraseña: ")

            # Verificar director
           
            if usuario == self.zoo.director.usuario and self.verificar_contrasenia(contrasenia, self.zoo.director.contrasenia):
                print("Inicio de sesión exitoso como Director.")
                self.menu_director()  # Redirigir al menú del director
                return

            # Verificar administrador

            for administrador in self.zoo.lista_administradores:
                if administrador.usuario == usuario and self.verificar_contrasenia(contrasenia, administrador.contrasenia):
                    print("Inicio de sesión exitoso como Administrador.")
                    self.menu_administrador()  # Redirigir al menú del administrador
                    return
            
            intentos += 1
            print(f"Usuario o contraseña incorrectos. Te quedan {5 - intentos} intento(s).")
        
        print("Has excedido el número de intentos permitidos. Intente más tarde.")


    def menu_director(self):
        while True:
            print("Menú del Director:")
            print("1. Registrar Administrador")
            print("2. Eliminar Administrador")
            print("3. Consultar Administradores")
            print("4. Ir al Menú")
            print("5. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                print("\nSeleccionaste Registrar un Administrador \n")
                self.zoo.registrar_administrador()
            elif opcion == '2':
                print("\nSeleccionaste Eliminar un Administrador \n")
                curp = input("Ingrese el CURP del administrador a eliminar: ")
                self.zoo.eliminar_administrador(curp)
            elif opcion == '3':
                print("\nSeleccionaste Consultar Administradores \n")
                self.zoo.consultar_administradores()
            elif opcion == '4':
                self.menu() 
            elif opcion == '5':
                print("Saliendo del menú del director...")
                break

    """
    def menu_director(self):
        print("Menú del Director:")
        self.menu()
    """
    def menu_administrador(self):
        print("Menú del Administrador:")
        self.menu()
    
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
            print("9. Modificar Empleados")
            print("10. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                print("\nSeleccionaste Registrar un Empleado \n")
                self.zoo.registrar_empleado()
            elif opcion == '2':
                print("\nSeleccionaste Registrar un Animal \n")
                self.zoo.registrar_animal()
            elif opcion == '3':
                print("\nSeleccionaste Registrar una Visita \n")
                self.zoo.registrar_visita()
            elif opcion == '4':
                print("\nSeleccionaste Eliminar un Empleado \n")
                curp = input("Ingrese el CURP del empleado a eliminar: ")
                self.zoo.eliminar_empleado(curp)
            elif opcion == '5':
                print("\nSeleccionaste Eliminar un Animal \n")
                self.zoo.eliminar_animal()
            elif opcion == '6':
                print("\nSeleccionaste Consultar los Empleados \n")
                self.zoo.consultar_empleado()
            elif opcion == '7':
                print("\nSeleccionaste Consultar las Animales \n")
                self.zoo.consultar_animales()
            elif opcion == '8':
                print("\nSeleccionaste Consultar las Visitas \n")
                self.zoo.consultar_visitas()
            elif opcion == '9':
                print("\nSeleccionaste Modificar un Empleado \n")
                self.zoo.modificar_empleado()
            elif opcion == '10':
                print("Saliendo...")
                break
            else:
                print("Opción no válida, intenta de nuevo.")

            
           

    

   