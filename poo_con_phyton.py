class Character:
    #Constructor de la clase(Atributos)
    name = "Default"
    strength = 0
    intelligence = 0
    defense = 0
    life = 0
    
    #Constructor de la clase
    def __init__(self, name, strength, intelligence, defense, life):
        self.name = name
        self.strength = strength
        self.intelligence = intelligence
        self.defense = defense 
        self.life = life

    def imprimir_atributos(self):
        print(self.name)
        print("Strength: ",self.strength)
        print("Inteligence: ",self.intelligence)
        print("Defense: ",self.defense)
        print("Life: ",self.life)

    def level_up(self, strength, intelligence, defense):
        self.strength = self.strength + strength
        #self.strength += strength
        self.intelligence = self.intelligence + intelligence
        self.defense = self.defense + defense   

    def is_alive(self):
        return self.life > 0
    
    def die(self):
        self.life = 0
        print("self.name has died")
        #return self.life <= 0

    def damage(self, enemy):
        return self.strength - enemy.defense
    
    def attack(self, enemy):
        damage = self.damage(enemy)
        enemy.life = enemy.life - damage
        #enemy.life -= damage
        print("------attack------")
        print(self.name, "has made", damage, "damage to", enemy.name)
        print("life of" , enemy.name , "is", enemy.life)
    
class Figther(Character):
     #Sobreescribir constructor
    def __init__(self, name, strength, intelligence, defense, life, sword):
        super().__init__(name, strength, intelligence, defense, life)
        self.sword = sword

    #Sobreescribir impresión
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("Sword: ", self.sword)

    def elegir_arma(self):
        opcion = int(input("Choose your weapon: \n 1.obsidian spear, daño 10 \n 2.chaya spear, daño 5 \n:"))
        if opcion == 1:
            self.sword = 10
        elif opcion == 2:
            self.sword = 5
        else:
            print("Invalid option")
            self.elegir_arma()

    #Sobreescribir calculo de daño
    def damage(self, enemy):
        return self.strength + self.sword - enemy.defense

class Wizard(Character):
     #Sobreescribir constructor
    def __init__(self, name, strength, intelligence, defense, life, book):
        super().__init__(name, strength, intelligence, defense, life)
        self.book = book

    #Sobreescribir impresión
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("Book: ", self.book)

    def elegir_arma(self):
        opcion = int(input("Choose your weapon: \n 1.Programming Spells, daño 10 \n 2.Chaya book, daño 5 \n:"))
        if opcion == 1:
            self.book = 10
        elif opcion == 2:
            self.book = 5
        else:
            print("Invalid option")
            self.elegir_arma()

    #Sobreescribir calculo de daño
    def damage(self, enemy):
        return self.intelligence*self.book - enemy.defense

michael_jackson = Character("Michael jackson", 20, 15, 10, 100)
tlatoani = Figther("Apocalipto", 50,70,30,100,5)
merlin = Wizard("Merlin", 20, 15, 10, 100, 5)

# Imprimikr atributos antes de la pelea
tlatoani.imprimir_atributos()
print("------------")
merlin.imprimir_atributos()
print("------------")
michael_jackson.imprimir_atributos()

#Ataque masivos
michael_jackson.attack(tlatoani,merlin)
tlatoani.attack(michael_jackson,merlin)
merlin.attack(michael_jackson,tlatoani) 

tlatoani.imprimir_atributos()
print("------------")
merlin.imprimir_atributos()
print("------------")
michael_jackson.imprimir_atributos()


# tlatoani.elegir_arma()
# merlin.elegir_arma()
# print(tlatoani.sword)


# #Variable del constructor vacio que almacena la clase
# print("------------Character------------")
# my_character = Character("Dante", 100, 3, 70, 100)
# my_character.imprimir_atributos()

# my_enemy = Character("Vergil", 70, 30, 70, 100)
# # print(my_character.damage(my_enemy))

# my_character.attack(my_enemy)
# print("------------Enemy after attack------------")
# my_enemy.imprimir_atributos()


    


#print(my_character.is_alive())

# print("------------Level up------------")
# my_character.level_up(10, 1, 5)
# my_character.imprimir_atributos()

# my_character.name = "Pompompurin"
# my_character.strength = 10
# my_character.intelligence = 10
# my_character.defense = 10
# my_character.life = 100

#Imprimir la variable con su respectivo atributo
# print("The name of my character is:" ,my_character.name)
# print("The strength of my character is:" ,my_character.strength)
# print("The intelligence of my character is:" ,my_character.intelligence)   
# print("The defense of my character is:" ,my_character.defense)
# print("The life of my character is:" ,my_character.life)    