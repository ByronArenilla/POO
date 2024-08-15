class Equipo():
    def __init__(self, nombre,pais):
        self.__nombre = nombre
        self.__pais = pais
        self.__listaCiclistas = [] #Esto en java es un vector 
        self.__totalTiempo = None

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def __getPais(self):
        return self.__pais
    
    #Añade un ciclista a la lista de ciclistas (cada ciclista es un objeto)
    def añadirCiclista(self, ciclista):
        self.__listaCiclistas.append(ciclista)

    def listarEquipo(self):
        # recorre la lista de ciclistas y para cada elemento imprime el nombre del ciclista
        for ciclista in self.__listaCiclistas:
            print(ciclista._getNombre())

    #Método que busca un ciclista ingresado por teclado
    def buscarCiclista(self):
        nombreCiclista = input("Ingrese el nombre del ciclista: ")
        for ciclista in self.__listaCiclistas:
            if ciclista._getNombre() == nombreCiclista:
                print (ciclista._getNombre())
        print ("Ciclista no encontrado")

    #Método que calcula el tiempo total de un equipo acumulando el tiempo obtendio por cada uno de los ciclistas
    def calcularTotalTiempo(self):
        self.__totalTiempo = 0
        #Recorre la lista de ciclistas y acumula el tiempo del equipo
        for ciclista in self.__listaCiclistas:
            self.__totalTiempo += ciclista._getTiempoAcumulado()
        print (f"Tiempo total del equipo: {self.__totalTiempo} minutos")

    #Método que muestra en pantalla los datos del equipo
    def imprimir(self):
        print(f"Nombre del equipo: {self.getNombre()}\nPaís: {self.__getPais()}\nTotal Tiempo del equipo: {self.__totalTiempo}")





    
