class Personaje:
    #Atributos de la clase
    nombre = "ChemaBeef"
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0
    #Indicar que no se haga nada en este momento
    pass
#Variable de constructoe vacio de la clase
mi_personaje = Personaje()
mi_personaje.nombre = "ChemaBeef"
mi_personaje.defensa = 42
mi_personaje.fuerza = 24
mi_personaje.inteligencia = 24
mi_personaje.vida = 212
print("El nombre de mi personaje es: ",mi_personaje.nombre)
print("La fuerza de mi personaje es: ",mi_personaje.fuerza)
print("La inteligencia de mi personaje es: ",mi_personaje.inteligencia)
print("La defensa de mi personaje es: ",mi_personaje.defensa)
print("La vida de mi personaje es: ",mi_personaje.vida)
