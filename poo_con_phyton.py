class Character:
    def __init__(self, name, strength, intelligence, defense, life):
        self.name = name
        self.strength = strength
        self.intelligence = intelligence
        self.defense = defense
        self.life = life
        self.inventory = []

    def imprimir_atributos(self):
        print(self.name)
        print("Strength:", self.strength)
        print("Intelligence:", self.intelligence)
        print("Defense:", self.defense)
        print("Life:", self.life)
        print("Inventory:", self.inventory)

    def level_up(self, strength, intelligence, defense):
        self.strength += strength
        self.intelligence += intelligence
        self.defense += defense   

    def is_alive(self):
        return self.life > 0

    def die(self):
        self.life = 0
        print(f"{self.name} has died")

    def damage(self, enemy):
        return max(0, self.strength - enemy.defense)

    def attack(self, enemy):
        damage = self.damage(enemy)
        enemy.receive_damage(damage)
        print("------attack------")
        print(self.name, "has made", damage, "damage to", enemy.name)
        print("Life of", enemy.name, "is", enemy.life)

    def receive_damage(self, damage):
        self.life -= damage
        if self.life <= 0:
            self.die()

    def use_potion(self, potion):
        if potion in self.inventory:
            if potion == "life":
                self.life += 20
            elif potion == "strength":
                self.strength += self.strength * 0.5
            elif potion == "intelligence":
                self.intelligence += self.intelligence * 0.5
            self.inventory.remove(potion)
            print(f"{self.name} uso una {potion} potion!")
        else:
            print(f"{self.name} no uso {potion} potion!")

class Fighter(Character):
    def __init__(self, name, strength, intelligence, defense, life, sword, shield):
        super().__init__(name, strength, intelligence, defense, life)
        self.sword = sword
        self.shield = shield
        self.shield_life = defense * shield

    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("Sword:", self.sword)
        print("Shield Life:", self.shield_life)

    def damage(self, enemy):
        return max(0, self.strength + self.sword - enemy.defense)

    def receive_damage(self, damage):
        if self.shield_life > 0:
            if damage < self.shield_life:
                self.shield_life -= damage
                print(f"{self.name} El escudo absorbio el daño total de: {self.shield_life}")
            else:
                remaining_damage = damage - self.shield_life
                self.shield_life = 0
                print(f"{self.name} el escudo se ha roto: {remaining_damage}")
                super().receive_damage(remaining_damage)
        else:
            super().receive_damage(damage)

class Wizard(Character):
    def __init__(self, name, strength, intelligence, defense, life, book):
        super().__init__(name, strength, intelligence, defense, life)
        self.book = book

    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("Book:", self.book)

    def damage(self, enemy):
        return max(0, self.intelligence * self.book - enemy.defense)

goku = Fighter("Goku", 50, 20, 10, 100, 5, 2)
vegeta = Fighter("Vegeta", 55, 25, 15, 100, 6, 3)
piccolo = Wizard("Piccolo", 20, 50, 10, 100, 5)

goku.inventory.append("life")
vegeta.inventory.append("strength")
piccolo.inventory.append("intelligence")

goku.imprimir_atributos()
print("------------")
vegeta.imprimir_atributos()
print("------------")
piccolo.imprimir_atributos()

goku.attack(vegeta)
vegeta.attack(goku)
piccolo.attack(goku)

goku.use_potion("life")
vegeta.use_potion("strength")
piccolo.use_potion("intelligence")

goku.imprimir_atributos()
print("------------")
vegeta.imprimir_atributos()
print("------------")
piccolo.imprimir_atributos()
