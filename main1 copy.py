# import tkinter as tk
# from tkinter import ttk

# class Aplicacion:
#     def __init__(self):
#         self.valor=1
#         self.ventana1=tk.Tk()
#         self.ventana1.title("Controles Button y Label")
#         self.label1=ttk.Label(self.ventana1, text=self.valor)
#         self.label1.grid(column=0, row=0)
#         self.label1.configure(foreground="red")

#         self.boton1=ttk.Button(self.ventana1, text="Incrementar", command=self.incrementar)
#         self.boton1.grid(column=0, row=1)

#         self.boton2=ttk.Button(self.ventana1, text="Decrementar", command=self.decrementar)
#         self.boton2.grid(column=0, row=2)
#         self.progressbar = ttk.Progressbar(self)
#         self.progressbar.place(x=30, y=60, width=200)
#         self.ventana1.mainloop()


#     def incrementar(self):
#         self.valor=self.valor+1
#         self.label1.config(text=self.valor)

#     def decrementar(self):
#         self.valor=self.valor-1
#         self.label1.config(text=self.valor)        


# aplicacion1=Aplicacion()



import tkinter as tk
from tkinter import ttk
class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        self.valor=1
        main_window.title("Barra de progreso en Tk")
        self.progressbar = ttk.Progressbar(self, maximum=100, value=self.valor)
        self.progressbar.place(x=30, y=60, width=200)
        self.place(width=300, height=200)
        main_window.geometry("300x200")

        self.label1=ttk.Label(main_window, text=self.valor)
        self.label1.grid(column=0, row=0)
        self.label1.configure(foreground="red")

        self.boton1=ttk.Button(main_window, text="Incrementar", command=self.incrementar)
        self.boton1.grid(column=0, row=1)

        self.boton2=ttk.Button(main_window, text="Decrementar", command=self.decrementar)
        self.boton2.grid(column=0, row=2)


    def incrementar(self):
        self.valor=self.valor+1
        self.label1.config(text=self.valor)
        self.progressbar.config(value=self.valor)

    def decrementar(self):
        self.valor=self.valor-1
        self.label1.config(text=self.valor)
        self.progressbar.config(value=self.valor)
        



main_window = tk.Tk()
app = Application(main_window)
app.mainloop()