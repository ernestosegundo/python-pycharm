class Contacto:
    def __init__(self, nick):
        self.__nick = nick
        self.__nombre = ""
        self.__apellidos = ""

    def __str__(self):
        return "El contacto {} tiene por nombre completo: {} {}".format(self.__nick, self.__nombre, self.__apellidos)

    def getNick(self):
        return self.__nick

    def getNombre(self):
        return self.__nombre

    def getApellidos(self):
        return self.__apellidos

    def setNick(self, nick):
        self.__nick = nick

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setApellidos(self, apellidos):
        self.__apellidos = apellidos