
import tkinter as tk
from tkinter import messagebox
import pymysql


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
    image = image.subsample(2,2)
    label = tk.Label(image=image)
    label.pack()

    tk.Label(text="Acceso al Sistema", bg="midnight blue", fg="white", height="3", font=("Calibri", 15)).pack()
    tk.Label(text="").pack()  # Salto de línea

    tk.Button(text="Iniciar Sesión", height="3", width="30", command=inicio_sesion).pack()
    tk.Label(text="").pack()  # Salto de línea

    tk.Button(text="Registrar", height="3", width="30", command=registrar).pack()

    ventana.mainloop()

def inicio_sesion():
    global ventana1
    ventana1 = tk.Toplevel(ventana)
    ventana1.geometry("400x250")
    ventana1.title("Inicia Sesión")
    ventana1.iconbitmap("Logo3.ico")

    tk.Label(ventana1, text="Ingrese Usuario y Contraseña").pack()
    tk.Label(ventana1, text="").pack()  # Salto de línea

    global nombreusuario_verify
    global contrasenausuario_verify

    nombreusuario_verify = tk.StringVar()
    contrasenausuario_verify = tk.StringVar()

    global nombre_usuario_entry
    global contrasena_usuario_entry

    tk.Label(ventana1, text="Usuario").pack()
    nombre_usuario_entry = tk.Entry(ventana1, textvariable=nombreusuario_verify)
    nombre_usuario_entry.pack()
    tk.Label(ventana1).pack()

    tk.Label(ventana1, text="Contraseña").pack()
    contrasena_usuario_entry = tk.Entry(ventana1, textvariable=contrasenausuario_verify, show="*")
    contrasena_usuario_entry.pack()
    tk.Label(ventana1).pack()

    tk.Button(ventana1, text="Iniciar Sesión", command=verificar_login).pack()

def registrar():
    global ventana2
    ventana2 = tk.Toplevel(ventana)
    ventana2.geometry("400x300")
    ventana2.title("Registro")
    ventana2.iconbitmap("Logo3.ico")

    global nombre_entry
    global apellido_entry
    global usuario_entry
    global contrasena_entry
    global rol_entry

    nombre_entry = tk.StringVar()
    apellido_entry = tk.StringVar()
    usuario_entry = tk.StringVar()
    contrasena_entry = tk.StringVar()
    rol_entry = tk.StringVar()

    tk.Label(ventana2, text="Ingrese los datos del nuevo usuario").pack()
    tk.Label(ventana2, text="").pack()  # Salto de línea

    tk.Label(ventana2, text="Nombre").pack()
    nombre_entry = tk.Entry(ventana2, textvariable=nombre_entry)
    nombre_entry.pack()

    tk.Label(ventana2, text="Apellido").pack()
    apellido_entry = tk.Entry(ventana2, textvariable=apellido_entry)
    apellido_entry.pack()

    tk.Label(ventana2, text="Usuario").pack()
    usuario_entry = tk.Entry(ventana2, textvariable=usuario_entry)
    usuario_entry.pack()

    tk.Label(ventana2, text="Contraseña").pack()
    contrasena_entry = tk.Entry(ventana2, textvariable=contrasena_entry, show="*")
    contrasena_entry.pack()

    tk.Label(ventana2, text="Rol (administrador/empleado)").pack()
    rol_entry = tk.Entry(ventana2, textvariable=rol_entry)
    rol_entry.pack()

    tk.Button(ventana2, text="Registrar", command=insertar_datos).pack()

def insertar_datos():
    conexion = conectar_db()
    cursor = conexion.cursor()

    sql = "INSERT INTO usuarios (Nombre, Apellido, Usuario, Contraseña, Rol) VALUES (%s, %s, %s, %s, %s)"
    valores = (nombre_entry.get(), apellido_entry.get(), usuario_entry.get(), contrasena_entry.get(), rol_entry.get())

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

def verificar_login():
    conexion = conectar_db()
    cursor = conexion.cursor()
    usuario = nombreusuario_verify.get()
    contrasena = contrasenausuario_verify.get()

    sql = "SELECT * FROM usuarios WHERE Usuario=%s AND Contraseña=%s"
    cursor.execute(sql, (usuario, contrasena))
    resultado = cursor.fetchone()
    conexion.close()

    if resultado:
        if resultado[5] == 'administrador':
            ventana_admin()
        else:
            ventana_empleado()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

def ventana_admin():
    admin = tk.Toplevel(ventana)
    admin.geometry("400x400")
    admin.title("Administrador")
    admin.iconbitmap("Logo3.ico")

    tk.Label(admin, text="Bienvenido Administrador").pack()
    # Aquí se pueden añadir más funcionalidades para gestionar empleados y libros
    admin.mainloop()

def ventana_empleado():
    empleado = tk.Toplevel(ventana)
    empleado.geometry("400x400")
    empleado.title("Empleado")
    empleado.iconbitmap("Logo3.ico")

    tk.Label(empleado, text="Bienvenido Empleado").pack()
    # Aquí se pueden añadir más funcionalidades para ver libros
    empleado.mainloop()

menu_acceso()
