class Hero():
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}\nМой уровень {self.level}\nМое здоровье {self.health}\nМоя сила {self.strength}")


    def attack(self):
        print(f"{self.name} наносит удар!")

    def rest(self):
        print(f"{self.name} отдыхает...")
        self.health += 1


class Pell():
    def __init__(self, name ="Pell", level=1, health=20, strength=0):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength




tanjirou = Hero("Tanjirou", 1, 100, 10)
zenitsu = Hero("Zenitsu", 1, 80, 8)
pell = Pell()


tanjirou.greet()
print('----------------------------------')
zenitsu.greet()
print('----------------------------------')


print(f"{tanjirou.name} vs {pell.name}")
tanjirou.attack()
pell.health -= tanjirou.strength
print(f"{pell.name} получил {tanjirou.strength} урона, его здоровье теперь {pell.health}")
tanjirou.strength -= 1
print('----------------------------------')


print(f"{zenitsu.name} vs {pell.name}")
zenitsu.attack()
pell.health -= zenitsu.strength
print(f"{pell.name} получил {zenitsu.strength} урона, его здоровье теперь {pell.health}")
zenitsu.strength -= 1
print('----------------------------------')


print("Время отдыха:")
tanjirou.rest()
zenitsu.rest()
print('----------------------------------')


print("После атаки и отдыха:")
tanjirou.greet()
print('----------------------------------')
zenitsu.greet()

