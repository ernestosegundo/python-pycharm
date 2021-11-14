from Modelo.Contacto import *
from tkinter import messagebox

contacto = Contacto("")

def salir(raiz):
    respuesta = messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")

    if respuesta == "yes":
        raiz.destroy()

def setContacto(nick, nombre, apellidos):
    contacto.setNick(nick)
    contacto.setNombre(nombre)
    contacto.setApellidos(apellidos)

def getContacto(c):
    c.set(contacto)