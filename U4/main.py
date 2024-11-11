import tkinter as tk
from Proyecto import Interfaz
from tkinter import messagebox

if __name__ == "__main__":
    try:
        ventana = tk.Tk()
        app = Interfaz(ventana)
        ventana.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error: {str(e)}")
        
