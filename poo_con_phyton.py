class Personaje:
    # Constructor de la clase
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida

    def imprimir_atributos(self):
        print(self.__nombre)
        print("-fuerza:", self.__fuerza)
        print("-inteligencia:", self.__inteligencia)
        print("-defensa:", self.__defensa)
        print("-vida:", self.__vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza += fuerza
        self.__inteligencia += inteligencia
        self.__defensa += defensa
    
    def esta_vivo(self):
        return self.__vida > 0
    
    def __morir(self): 
        return self.__vida <= 0
    
    def dmg(self, enemigo):
        return max(self.__fuerza - enemigo.__defensa, 1)
    
    def dmgRecibido(self, enemigo):
        dmg = self.dmg(enemigo)
        enemigo.__vida = max(enemigo.__vida - dmg, 0)
        print(self.__nombre, "Ha realizado", dmg, "puntos de daño a", enemigo.__nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.__nombre, "es", enemigo.__vida)
        else:
            print(enemigo.__nombre, "ha muerto")
    def get_fuerza(self):
        return self.__fuerza
    def set_fuerza(self, fuerza):
        if fuerza < 0:
            print("Error valor 0 o negativo")
        else:
            self.__fuerza = fuerza

# Variable de constructor vacío de la clase
mi_personaje = Personaje("Dante", 100, 3, 70, 100)
# mi_personaje.imprimir_atributos()
# print(mi_personaje.esta_vivo())
# print(mi_personaje.morir())

mi_enemigo = Personaje("Bergel", 70, 30, 70, 100)
# mi_personaje.dmgRecibido(mi_enemigo)
# mi_enemigo.imprimir_atributos()
mi_personaje.set_fuerza (100)
print(mi_personaje.get_fuerza())