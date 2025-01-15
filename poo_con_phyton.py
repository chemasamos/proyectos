class Personaje:
    # Constructor de la clase
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def imprimir_atributos(self):
        print(self.nombre)
        print("-fuerza:", self.fuerza)
        print("-inteligencia:", self.inteligencia)
        print("-defensa:", self.defensa)
        print("-vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa
    
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self): 
        return self.vida <= 0
    
    def dmg(self, enemigo):
        return max(self.fuerza - enemigo.defensa, 1)
    
    def dmgRecibido(self, enemigo):
        dmg = self.dmg(enemigo)
        enemigo.vida = max(enemigo.vida - dmg, 0)
        print(self.nombre, "Ha realizado", dmg, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            print(enemigo.nombre, "ha muerto")

# Variable de constructor vacío de la clase
mi_personaje = Personaje("Dante", 100, 3, 70, 100)
mi_personaje.imprimir_atributos()
print(mi_personaje.esta_vivo())
print(mi_personaje.morir())
mi_enemigo = Personaje("Bergel", 70, 30, 70, 100)
mi_personaje.dmgRecibido(mi_enemigo)
mi_enemigo.imprimir_atributos()
