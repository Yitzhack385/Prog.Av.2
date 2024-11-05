import tkinter as tk
from tkinter import messagebox

#---Suma-------------------------------------------------------------
 
def Sumar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        suma = num1 + num2
        messagebox.showinfo("Resultado", f"La suma es: {suma}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
 
#---Resta-----------------------------------------------------------------

def Restar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resta = num1 - num2
        messagebox.showinfo("Resultado", f"La resta es: {resta}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

#---Multiplicación-----------------------------------------------------------------

def Multiplicar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        multi = num1 * num2
        messagebox.showinfo("Resultado", f"La multiplicación es: {multi}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

#---División-----------------------------------------------------------------

def Dividir():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        div = num1 / num2
        messagebox.showinfo("Resultado", f"La división es: {div}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
 
ventana = tk.Tk()
ventana.title("Calculadora de Suma")
ventana.geometry("800x400")
 
label_num1 = tk.Label(ventana, text="Número 1:")
label_num1.pack(pady=5)
entry_num1 = tk.Entry(ventana)
entry_num1.pack(pady=5)
 
label_num2 = tk.Label(ventana, text="Número 2:")
label_num2.pack(pady=5)
entry_num2 = tk.Entry(ventana)
entry_num2.pack(pady=5)
 
boton_sumar = tk.Button(ventana, text="Sumar", command = Sumar)
boton_sumar.pack(pady=20)

boton_restar = tk.Button(ventana, text="Restar", command = Restar)
boton_restar.pack(pady=20)

boton_multiplicar = tk.Button(ventana, text="Multiplicar", command = Multiplicar)
boton_multiplicar.pack(pady=20)

boton_dividir = tk.Button(ventana, text="Dividir", command = Dividir)
boton_dividir.pack(pady=20)

ventana.mainloop()
