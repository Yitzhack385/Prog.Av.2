import tkinter as tk
from tkinter import messagebox

class ProductoInvalidoException(Exception):
    
    def producto_invalido(nombre):
        if not nombre:
            raise ProductoInvalidoException("El nombre del producto no puede estar vacío.")
    

class PrecioInvalidoException(Exception):
    def precio_invalido(precio):
        if precio <= 0:
            raise PrecioInvalidoException("El precio debe ser mayor que cero.")

class CantidadInvalidaException(Exception):
    def cantidad_invalida(cantidad):
        if cantidad < 0:
            raise CantidadInvalidaException("La cantidad no puede ser negativa.")

class Producto:
    def __init__(self, nombre, precio, cantidad):
        
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_valor_total(self):
        return self.precio * self.cantidad

    def mostrar_detalles(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}, Valor Total: {self.calcular_valor_total()}"

class Interfaz:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestión de Productos")
        self.ventana.geometry("370x250")
        self.productos = []

        self.nombre_label = tk.Label(ventana, text="Nombre del Producto", bg="lightblue", fg="black", font=("Arial", 12, "bold"), relief="sunken", padx=10, pady=10)
        self.nombre_label.grid(row=0, column=0)
        self.nombre_entry = tk.Entry(ventana)
        self.nombre_entry.grid(row=0, column=1)

        self.precio_label = tk.Label(ventana, text="Precio del Producto", bg="lightblue", fg="black", font=("Arial", 12, "bold"), relief="sunken", padx=10, pady=10)
        self.precio_label.grid(row=1, column=0)
        self.precio_entry = tk.Entry(ventana)
        self.precio_entry.grid(row=1, column=1)

        self.cantidad_label = tk.Label(ventana, text="Cantidad en Inventario", bg="lightblue", fg="black", font=("Arial", 12, "bold"), relief="sunken", padx=10, pady=10)
        self.cantidad_label.grid(row=2, column=0)
        self.cantidad_entry = tk.Entry(ventana)
        self.cantidad_entry.grid(row=2, column=1)

        self.agregar_button = tk.Button(ventana, text="Agregar Producto", command=self.agregar_producto, bg="lightblue", fg="black", font=("Arial", 10, "bold"), relief="sunken", padx=10, pady=10)
        self.agregar_button.grid(row=3, column=0, columnspan=2)

        self.detalles_label = tk.Label(ventana, text="")
        self.detalles_label.grid(row=4, column=0, columnspan=2)

        self.mostrar_lista_button = tk.Button(ventana, text="Mostrar Lista de Productos", command=self.mostrar_lista_productos, bg="lightblue", fg="black", font=("Arial", 10, "bold"), relief="sunken", padx=10, pady=10)
        self.mostrar_lista_button.grid(row=5, column=0, columnspan=2)


    def agregar_producto(self):
        nombre = self.nombre_entry.get()
        try:
            precio = float(self.precio_entry.get())
            cantidad = int(self.cantidad_entry.get())
            producto = Producto(nombre, precio, cantidad)
            self.detalles_label.config(text=producto.mostrar_detalles())
            self.productos.append(producto)
        except ValueError:
            messagebox.showerror("Error", "Precio y cantidad deben ser números.")
        except (ProductoInvalidoException, PrecioInvalidoException, CantidadInvalidaException) as e:
            messagebox.showerror("Error", str(e))

    def mostrar_lista_productos(self):
        detalles = "\n".join(producto.mostrar_detalles() for producto in self.productos) or "No hay productos en la lista."
        messagebox.showinfo("Lista de Productos", detalles)
