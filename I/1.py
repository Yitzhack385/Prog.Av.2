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
    except ZeroDivisionError:
        messagebox.showerror("Error", "No se puede dividir por cero.")

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("255x200")
 
label_num1 = tk.Label(ventana, text="Número 1:", bg="lightblue", fg="black", font=("Calibri", 12, "bold"), relief="sunken", padx=10, pady=10)
label_num1.grid(row=0, column=0)
entry_num1 = tk.Entry(ventana)
entry_num1.grid(row=1, column=0)
 
label_num2 = tk.Label(ventana, text="Número 2:", bg="lightblue", fg="black", font=("Calibri", 12, "bold"), relief="sunken", padx=10, pady=10)
label_num2.grid(row=0, column=1)
entry_num2 = tk.Entry(ventana)
entry_num2.grid(row=1, column=1)
 
boton_sumar = tk.Button(ventana, text="Sumar", command = Sumar, bg="lightgreen", fg="black", font=("Arial", 10), relief="raised", padx=10, pady=10)
boton_sumar.grid(row=2, column=0, pady=10)

boton_restar = tk.Button(ventana, text="Restar", command = Restar, bg="lightgreen", fg="black", font=("Arial", 10), relief="raised", padx=10, pady=10)
boton_restar.grid(row=2, column=1, pady=10)

boton_multiplicar = tk.Button(ventana, text="Multiplicar", command = Multiplicar, bg="lightgreen", fg="black", font=("Arial", 10), relief="raised", padx=10, pady=10)
boton_multiplicar.grid(row=3, column=0, pady=10)

boton_dividir = tk.Button(ventana, text="Dividir", command = Dividir, bg="lightgreen", fg="black", font=("Arial", 10), relief="raised", padx=10, pady=10)
boton_dividir.grid(row=3, column=1, pady=10)

ventana.mainloop()