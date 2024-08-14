from Animales import *
animales = []

#Creando cada animal
gato = Gato()
perro = Perro()
lobo = Lobo()
leon = Leon()


#Añadiendo los animales (objetos) a la lista de objetos animales
animales.append(gato)
animales.append(perro)
animales.append(lobo)
animales.append(leon)

for i in range(0,len(animales),1):
    print(f"{animales[i].getNombreCientifico()}\nSonido: {animales[i].getSonido()}\nAlimentos: {animales[i].getAlimentos()}\nHabitat: {animales[i].getHabitad()}\n ")