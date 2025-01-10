class Personaje:
    # Atributos de la clase (pueden ser opcionalmente inicializados en el constructor)
    # nombre = "ChemaBeef"
    # fuerza = 0
    # inteligencia = 0
    # defensa = 0
    # vida = 0

    # Constructor de la clase
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
#Que es self?: referencia al mismo objeto
#Que es init?: inicializa el producto del objeto
#Porque utiliza __: porque es un metodo magico, dunder
#En que momento se ejecucta el metodo __init__: cuando se crea un objeto
#snake_case y CamelCase
    def imprimir_atributos(self):
        print(self.nombre)
        print("-fuerza:",self.fuerza)
        print("-inteligencia:",self.inteligencia)
        print("-defensa:",self.defensa)
        print("-vida:",self.vida)

    def subir_nivel(self, fuerza, inteligencia,defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
    
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self): 
        return self.vida <= 0
    
    def dmg(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def dmgRecibido(self, enemigo):
        dmg = self.dmg(enemigo)
        enemigo.vida = enemigo.vida - dmg
        print(self.nombre,"Ha realizado ",dmg,"Puntos de daño a", enemigo.nombre)
        print("Vida de",enemigo.vida, "Es", enemigo.vida)

    #Variable de constructoe vacio de la clase
mi_personaje = Personaje("Dante",100,3,70,100)
mi_personaje.imprimir_atributos()
print(mi_personaje.esta_vivo())
print(mi_personaje.morir())
mi_enemigo = Personaje("Bergel",70,30,70,100)
mi_personaje.dmgRecibido(mi_enemigo)
mi_enemigo.imprimir_atributos()

# print(mi_personaje.dmg(mi_enemigo))


# mi_personaje.subir_nivel(10,1,5)
# print("_______________________")
# mi_personaje.imprimir_atributos()
# mi_personaje.nombre = "ChemaBeef"
# mi_personaje.defensa = 42
# mi_personaje.fuerza = 24
# mi_personaje.inteligencia = 24
# mi_personaje.vida = 212

