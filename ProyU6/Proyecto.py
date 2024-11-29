
import tkinter as tk
from tkinter import messagebox
import pymysql
from tkinter import ttk


def conectar_db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="biblioteca"
    )


def menu_acceso():
    global ventana
    ventana = tk.Tk()
    ventana.geometry("380x300")
    ventana.title("Login")
    ventana.iconbitmap("Logo3.ico")

    image = tk.PhotoImage(file="Logoe2.gif")
    image = image.subsample(2, 2)
    label = tk.Label(ventana, image=image)
    label.image = image  # Guardar referencia para evitar recolección de basura
    label.pack()

    tk.Label(text="Acceso al Sistema", bg="midnight blue", fg="white", height="3", font=("Calibri", 15)).pack()
    tk.Label(text="").pack()  # Salto de línea

    tk.Button(text="Iniciar Sesión",height="3",width="30",command=inicio_sesion).pack()
    tk.Label(text="").pack()  # Salto de línea

    tk.Button(text="Registrar",height="3",width="30",command=registrar).pack()

    ventana.mainloop()


def inicio_sesion():
    global ventana1
    ventana1 = tk.Toplevel(ventana)
    ventana1.geometry("400x250")
    ventana1.title("Inicia Sesión")
    ventana1.iconbitmap("Logo3.ico")

    tk.Label(ventana1, text="Ingrese Usuario y Contraseña").pack()
    tk.Label(ventana1, text="").pack()  # Salto de línea

    global nombreusuario_verify, contrasenausuario_verify
    nombreusuario_verify = tk.StringVar()
    contrasenausuario_verify = tk.StringVar()

    tk.Label(ventana1, text="Usuario").pack()
    nombre_usuario_entry = tk.Entry(ventana1, textvariable=nombreusuario_verify)
    nombre_usuario_entry.pack()
    tk.Label(ventana1).pack()

    tk.Label(ventana1, text="Contraseña").pack()
    contrasena_usuario_entry = tk.Entry(ventana1, textvariable=contrasenausuario_verify, show="*")
    contrasena_usuario_entry.pack()
    tk.Label(ventana1).pack()

    def verificar_login():
        conexion = conectar_db()
        cursor = conexion.cursor()
        usuario = nombreusuario_verify.get()
        contrasena = contrasenausuario_verify.get()

        sql = "SELECT * FROM usuarios WHERE Usuario=%s AND Contrasena=%s"
        cursor.execute(sql, (usuario, contrasena))
        resultado = cursor.fetchone()
        conexion.close()

        if resultado:
            ventana1.destroy()
            if resultado[5] == 'administrador':
                ventana_admin()
            else:
                ventana_empleado()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    tk.Button(ventana1, text="Iniciar Sesión", command=verificar_login).pack()


def registrar():
    ventana2 = tk.Toplevel(ventana)
    ventana2.geometry("400x300")
    ventana2.title("Registro")
    ventana2.iconbitmap("Logo3.ico")

    nombre_entry = tk.StringVar()
    apellido_entry = tk.StringVar()
    usuario_entry = tk.StringVar()
    contrasena_entry = tk.StringVar()
    rol_entry = tk.StringVar()

    tk.Label(ventana2, text="Ingrese los datos del nuevo usuario").pack()
    tk.Label(ventana2, text="").pack()  # Salto de línea

    tk.Label(ventana2, text="Nombre").pack()
    nombre_entry_widget = tk.Entry(ventana2, textvariable=nombre_entry)
    nombre_entry_widget.pack()

    tk.Label(ventana2, text="Apellido").pack()
    apellido_entry_widget = tk.Entry(ventana2, textvariable=apellido_entry)
    apellido_entry_widget.pack()

    tk.Label(ventana2, text="Usuario").pack()
    usuario_entry_widget = tk.Entry(ventana2, textvariable=usuario_entry)
    usuario_entry_widget.pack()

    tk.Label(ventana2, text="Contraseña").pack()
    contrasena_entry_widget = tk.Entry(ventana2, textvariable=contrasena_entry, show="*")
    contrasena_entry_widget.pack()

    tk.Label(ventana2, text="Rol (administrador/empleado)").pack()
    rol_entry_widget = tk.Entry(ventana2, textvariable=rol_entry)
    rol_entry_widget.pack()

    def insertar_datos():
        conexion = conectar_db()
        cursor = conexion.cursor()

        sql = "INSERT INTO Usuarios (Nombre, Apellido, Usuario, Contrasena, Rol) VALUES (%s, %s, %s, %s, %s)"
        valores = (
            nombre_entry.get(),
            apellido_entry.get(),
            usuario_entry.get(),
            contrasena_entry.get(),
            rol_entry.get()
        )

        try:
            cursor.execute(sql, valores)
            conexion.commit()
            messagebox.showinfo("Éxito", "Usuario registrado con éxito")
            ventana2.destroy()
        except Exception as e:
            conexion.rollback()
            messagebox.showerror("Error", str(e))
        finally:
            conexion.close()

    tk.Button(ventana2, text="Registrar", command=insertar_datos).pack()

#----------------------------------------------------------------Admin

def ventana_admin():
    admin = tk.Toplevel(ventana)
    admin.geometry("1200x800")
    admin.title("Administrador")
    admin.iconbitmap("Logo3.ico")

    tk.Label(admin, text="Bienvenido Administrador").pack()

    columns = ("id", "nombre", "apellido", "usuario", "contrasena", "rol")
    tree = ttk.Treeview(admin, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col.capitalize())
    tree.pack(fill=tk.BOTH, expand=True)

    def leer_usuarios():
        conn = conectar_db()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM Usuarios")
            rows = cursor.fetchall()
            for item in tree.get_children():
                tree.delete(item)
            for row in rows:
                tree.insert("", tk.END, values=row)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer los usuarios: {e}")
        finally:
            conn.close()

    leer_usuarios()

    # Función para eliminar un usuario
    def eliminar_usuario():
        selected_item = tree.selection()
        if selected_item:
            user_id = tree.item(selected_item)["values"][0]
            conexion = conectar_db()
            cursor = conexion.cursor()
            try:
                cursor.execute("DELETE FROM Usuarios WHERE id = %s", (user_id,))
                conexion.commit()
                messagebox.showinfo("Éxito", "Usuario eliminado correctamente")
                leer_usuarios()  # Actualizar la vista
            except Exception as e:
                conexion.rollback()
                messagebox.showerror("Error", f"No se pudo eliminar el usuario: {e}")
            finally:
                conexion.close()
        else:
            messagebox.showwarning("Selección", "Por favor, seleccione un usuario para eliminar.")

    # Función para actualizar los datos de un usuario
    def actualizar_usuario():
        selected_item = tree.selection()
        if selected_item:
            user_id = tree.item(selected_item)["values"][0]

            def guardar_actualizacion():
                nuevo_nombre = nombre_entry.get()
                nuevo_apellido = apellido_entry.get()
                nuevo_usuario = usuario_entry.get()
                nueva_contrasena = contrasena_entry.get()
                nuevo_rol = rol_entry.get()

                conexion = conectar_db()
                cursor = conexion.cursor()
                try:
                    cursor.execute("""UPDATE Usuarios SET Nombre = %s, Apellido = %s, Usuario = %s, Contrasena = %s, Rol = %s WHERE id = %s""", (nuevo_nombre, nuevo_apellido, nuevo_usuario, nueva_contrasena, nuevo_rol, user_id))
                    conexion.commit()
                    messagebox.showinfo("Éxito", "Usuario actualizado correctamente")
                    leer_usuarios()  # Actualizar la vista
                except Exception as e:
                    conexion.rollback()
                    messagebox.showerror("Error", f"No se pudo actualizar el usuario: {e}")
                finally:
                    conexion.close()

            # Ventana para editar datos
            editar_ventana = tk.Toplevel(admin)
            editar_ventana.geometry("400x300")
            editar_ventana.title("Editar Usuario")

            nombre_entry = tk.StringVar()
            apellido_entry = tk.StringVar()
            usuario_entry = tk.StringVar()
            contrasena_entry = tk.StringVar()
            rol_entry = tk.StringVar()

            # Rellenar los campos con los datos actuales
            conn = conectar_db()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Usuarios WHERE id = %s", (user_id,))
            user_data = cursor.fetchone()
            nombre_entry.set(user_data[1])
            apellido_entry.set(user_data[2])
            usuario_entry.set(user_data[3])
            contrasena_entry.set(user_data[4])
            rol_entry.set(user_data[5])

            tk.Label(editar_ventana, text="Nombre").pack()
            tk.Entry(editar_ventana, textvariable=nombre_entry).pack()

            tk.Label(editar_ventana, text="Apellido").pack()
            tk.Entry(editar_ventana, textvariable=apellido_entry).pack()

            tk.Label(editar_ventana, text="Usuario").pack()
            tk.Entry(editar_ventana, textvariable=usuario_entry).pack()

            tk.Label(editar_ventana, text="Contraseña").pack()
            tk.Entry(editar_ventana, textvariable=contrasena_entry, show="*").pack()

            tk.Label(editar_ventana, text="Rol").pack()
            tk.Entry(editar_ventana, textvariable=rol_entry).pack()

            tk.Button(editar_ventana, text="Guardar Cambios", command=guardar_actualizacion).pack()

        else:
            messagebox.showwarning("Selección", "Por favor, seleccione un usuario para editar.")

    # Botones para eliminar y editar
    tk.Button(admin, text="Eliminar Usuario", command=eliminar_usuario).pack()
    tk.Button(admin, text="Actualizar Usuario", command=actualizar_usuario).pack()

#----------------------------------------------------------------Empleado

def ventana_empleado():
    empleado = tk.Toplevel(ventana)
    empleado.geometry("600x400")
    empleado.title("Empleado")
    empleado.iconbitmap("Logo3.ico")

    tk.Label(empleado, text="Bienvenido Empleado").pack()

    # Crear el Treeview para mostrar los libros
    columns_libros = ("id", "titulo", "autor", "editorial", "ano_publicacion", "precio")
    tree_libros = ttk.Treeview(empleado, columns=columns_libros, show="headings")
    
    # Configurar los encabezados de las columnas
    for col in columns_libros:
        tree_libros.heading(col, text=col.capitalize())
        tree_libros.column(col, width=100)

    tree_libros.pack(fill=tk.BOTH, expand=True)

    # Función para leer los libros de la base de datos
    def leer_libros():
        conn = conectar_db()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM Libros")
            rows = cursor.fetchall()

            # Limpiar la tabla antes de insertar nuevos datos
            for item in tree_libros.get_children():
                tree_libros.delete(item)

            # Insertar cada fila de datos en el Treeview
            for row in rows:
                tree_libros.insert("", tk.END, values=row)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer los libros: {e}")
        finally:
            conn.close()

    leer_libros()  # Llamar para cargar los libros al inicio

    # Función para eliminar un libro
    def eliminar_libro():
        selected_item = tree_libros.selection()
        if selected_item:
            libro_id = tree_libros.item(selected_item)["values"][0]
            conn = conectar_db()
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE FROM Libros WHERE id = %s", (libro_id,))
                conn.commit()
                messagebox.showinfo("Éxito", "Libro eliminado correctamente")
                leer_libros()  # Refrescar la lista de libros
            except Exception as e:
                conn.rollback()
                messagebox.showerror("Error", f"No se pudo eliminar el libro: {e}")
            finally:
                conn.close()
        else:
            messagebox.showwarning("Selección", "Por favor, seleccione un libro para eliminar.")

    # Función para actualizar los datos de un usuario
    def actualizar_libro():
        selected_item = tree_libros.selection()
        if selected_item:
            user_id = tree_libros.item(selected_item)["values"][0]

            def guardar_actualizacion():
                nuevo_titulo = titulo_entry.get()
                nuevo_autor = autor_entry.get()
                nuevo_editorial = editorial_entry.get()
                nueva_ano_publicacion = ano_publicacion_entry.get()
                nuevo_precio = precio_entry.get()

                conexion = conectar_db()
                cursor = conexion.cursor()
                try:
                    cursor.execute("""UPDATE libros SET Titulo = %s, Autor = %s, Editorial = %s, Ano_Publicacion = %s, Precio = %s WHERE id = %s""", (nuevo_titulo, nuevo_autor, nuevo_editorial, nueva_ano_publicacion, nuevo_precio, user_id))
                    conexion.commit()
                    messagebox.showinfo("Éxito", "libro actualizado correctamente")
                    leer_libros()  # Actualizar la vista
                except Exception as e:
                    conexion.rollback()
                    messagebox.showerror("Error", f"No se pudo actualizar el libro: {e}")
                finally:
                    conexion.close()

            # Ventana para editar datos
            editar_ventana = tk.Toplevel(empleado)
            editar_ventana.geometry("400x300")
            editar_ventana.title("Editar libro")

            titulo_entry=tk.StringVar()
            autor_entry=tk.StringVar()
            editorial_entry=tk.StringVar()
            ano_publicacion_entry=tk.StringVar()
            precio_entry=tk.StringVar()

            # Rellenar los campos con los datos actuales
            conn = conectar_db()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM libros WHERE id = %s", (user_id,))
            user_data = cursor.fetchone()
            titulo_entry.set(user_data[1])
            autor_entry.set(user_data[2])
            editorial_entry.set(user_data[3])
            ano_publicacion_entry.set(user_data[4])
            precio_entry.set(user_data[5])

            tk.Label(editar_ventana, text="Título").pack()
            tk.Entry(editar_ventana, textvariable=titulo_entry).pack()

            tk.Label(editar_ventana, text="Autor").pack()
            tk.Entry(editar_ventana, textvariable=autor_entry).pack()

            tk.Label(editar_ventana, text="Editorial").pack()
            tk.Entry(editar_ventana, textvariable=editorial_entry).pack()

            tk.Label(editar_ventana, text="Año de Publicación").pack()
            tk.Entry(editar_ventana, textvariable=ano_publicacion_entry).pack()

            tk.Label(editar_ventana, text="Precio").pack()
            tk.Entry(editar_ventana, textvariable=precio_entry).pack()


            tk.Button(editar_ventana, text="Guardar Cambios", command=guardar_actualizacion).pack()
        else:
            messagebox.showwarning("Selección", "Por favor, seleccione un libro para editar.")

    # Botones para editar
    tk.Button(empleado, text="Actualizar libro", command=actualizar_libro).pack()

    # Función para agregar un libro
    def agregar_libro():
        def insertar_libro():
            titulo = titulo_entry.get()
            autor = autor_entry.get()
            editorial = editorial_entry.get()
            ano_publicacion = ano_publicacion_entry.get()
            precio = precio_entry.get()

            conn = conectar_db()
            cursor = conn.cursor()
            try:
                cursor.execute("""INSERT INTO Libros (titulo, autor, editorial, ano_publicacion, precio) VALUES (%s, %s, %s, %s, %s)""", (titulo, autor, editorial, ano_publicacion, precio))
                conn.commit()
                messagebox.showinfo("Éxito", "Libro agregado con éxito")
                agregar_ventana.destroy()
                leer_libros()  # Refrescar la lista de libros
            except Exception as e:
                conn.rollback()
                messagebox.showerror("Error", f"No se pudo agregar el libro: {e}")
            finally:
                conn.close()

        # Crear la ventana para agregar un nuevo libro
        agregar_ventana = tk.Toplevel(empleado)
        agregar_ventana.geometry("400x300")
        agregar_ventana.title("Agregar Libro")

        # Campos de entrada para los detalles del libro
        titulo_entry = tk.StringVar()
        autor_entry = tk.StringVar()
        editorial_entry = tk.StringVar()
        ano_publicacion_entry = tk.StringVar()
        precio_entry = tk.StringVar()

        tk.Label(agregar_ventana, text="Título").pack()
        tk.Entry(agregar_ventana, textvariable=titulo_entry).pack()

        tk.Label(agregar_ventana, text="Autor").pack()
        tk.Entry(agregar_ventana, textvariable=autor_entry).pack()

        tk.Label(agregar_ventana, text="Editorial").pack()
        tk.Entry(agregar_ventana, textvariable=editorial_entry).pack()

        tk.Label(agregar_ventana, text="Año de Publicación").pack()
        tk.Entry(agregar_ventana, textvariable=ano_publicacion_entry).pack()

        tk.Label(agregar_ventana, text="Precio").pack()
        tk.Entry(agregar_ventana, textvariable=precio_entry).pack()

        tk.Button(agregar_ventana, text="Agregar Libro", command=insertar_libro).pack()

    # Botones para agregar y eliminar libros
    tk.Button(empleado, text="Agregar Libro", command=agregar_libro).pack()
    tk.Button(empleado, text="Eliminar Libro", command=eliminar_libro).pack()

menu_acceso()