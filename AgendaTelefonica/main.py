from tkinter import *
from Negocio.Contacto import *

root = Tk()

root.title("Contactos")
root.resizable(0, 0)
root.geometry("240x210")

frameDatos = Frame(root)
frameDatos.pack()

nick = StringVar()
nombre = StringVar()
apellidos = StringVar()

Label(frameDatos, text="Nick").grid(row=0, column=0, sticky="e")
Label(frameDatos, text="Nombre").grid(row=1, column=0, sticky="e")
Label(frameDatos, text="Apellidos").grid(row=2, column=0, sticky="e")

entryNick = Entry(frameDatos, width=25)
entryNick.grid(row=0, column=1, padx=10, pady=10)
entryNick.config(bg="pink", justify="center", textvariable=nick)
entryNick.focus()
entryNombre = Entry(frameDatos, width=25)
entryNombre.grid(row=1, column=1, padx=10, pady=10)
entryNombre.config(textvariable=nombre)
entryApellidos = Entry(frameDatos, width=25)
entryApellidos.grid(row=2, column=1, padx=10, pady=10)
entryApellidos.config(textvariable=apellidos)

frameBotones = Frame(root)
frameBotones.pack()

contacto = StringVar()

buttonGuardar = Button(frameBotones, text="Guardar", width=7, command=lambda: setContacto(nick.get(), nombre.get(),
                                                                                          apellidos.get()))
buttonGuardar.grid(row=0, column=0, padx=10, pady=10)
buttonGuardar.config(bg="#28a745", fg="white")
buttonVer = Button(frameBotones, text="Ver", width=7, command=lambda: getContacto(contacto))
buttonVer.grid(row=0, column=1, padx=10, pady=10)
buttonVer.config(bg="#007bff", fg="white")
buttonSalir = Button(frameBotones, text="Salir", width=7, command=lambda: salir(root))
buttonSalir.grid(row=0, column=2, padx=10, pady=10)
buttonSalir.config(bg="#dc3545", fg="white")
labelContacto = Label(frameBotones, text="", wraplength=240)
labelContacto.grid(row=1, column=0, columnspan=3)
labelContacto.config(textvariable=contacto)

root.mainloop()
