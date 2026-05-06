from random import randint

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


# Класс для Воина
class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print(f"{self.name} наносит мощный удар мечом!")


# Класс для Мага
class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print(f"{self.name} кастует заклинание!")


# Класс для Ассасина
class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print(f"{self.name} наносит удар ножом из тени!")


while True:
    # Валидация выбора героя
    while True:
        user_hero_choice = input("Выберите вашего героя (Warrior - 1 / Mage - 2 / Assassin - 3): ")
        if user_hero_choice in ["1", "2", "3"]:
            break
        else:
            print("Неверный выбор героя.")

    # Валидация имени героя
    while True:
        name_of_hero = input("Введите имя вашего героя: ")
        if name_of_hero.strip():
            break
        else:
            print("Имя героя не может быть пустым. Пожалуйста, введите имя.")

    # Создание героя
    if user_hero_choice == "1":
        hero = Warrior(name_of_hero, 1, 100, 10, 50)
    elif user_hero_choice == "2":
        hero = Mage(name_of_hero, 1, 80, 5, 100)
    elif user_hero_choice == "3":
        hero = Assassin(name_of_hero, 1, 90, 7, 80)

    # Создание врага
    enemy_choice = randint(1, 3)
    if enemy_choice == 1:
        enemy = Warrior("Враг-Воин", 1, 100, 10, 50)
    elif enemy_choice == 2:
        enemy = Mage("Враг-Маг", 1, 80, 5, 100)
    elif enemy_choice == 3:
        enemy = Assassin("Враг-Ассасин", 1, 90, 7, 80)

    print("\nВаш герой:")
    hero.greet()
    print("\nВаш противник в сегодняшней битве:")
    enemy.greet()

    print()
    hero.attack()
    enemy.attack()
    print()

    # Определение победителя
    if user_hero_choice == enemy_choice:
        print("Битва закончилась ничьей!")
    elif (user_hero_choice == "1" and enemy_choice == 3) or \
         (user_hero_choice == "2" and enemy_choice == 1) or \
         (user_hero_choice == "3" and enemy_choice == 2):
        print(f"🏆 {hero.name} победил!")
    else:
        print(f"💀 {enemy.name} победил!")

    # Выбор продолжения игры
    play_again = input("\nХотите сыграть еще раз? (да/нет): ")
    if play_again.lower() != "да":
        print("Спасибо за игру! До свидания!")
        break