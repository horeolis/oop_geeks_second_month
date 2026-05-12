from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}")
        print(f"Мой уровень: {self.level}")
        print(f"Мое здоровье: {self.__health}")
        print(f"Моя сила: {self.strength}")

    def rest(self):
        print(f"{self.name} отдыхает...")
        self.__health += 1
        print(f"Здоровье восстановлено! Теперь здоровье: {self.__health}")

    @abstractmethod
    def attack(self):
        pass



class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print(f"{self.name} наносит мощный удар мечом!")


class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print(f"{self.name} кастует заклинание!")


class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print(f"{self.name} наносит удар ножом из тени!")


while True:
    print("\n" + "="*40)
    print("      СОЗДАНИЕ ГЕРОЯ")
    print("="*40)

    # Валидация выбора героя
    while True:
        print("\n1 - Warrior (Воин)")
        print("2 - Mage (Маг)")
        print("3 - Assassin (Ассасин)")
        user_hero_choice = input("\nВыберите вашего героя: ")
        if user_hero_choice in ["1", "2", "3"]:
            break
        else:
            print("❌ Неверный выбор. Введите 1, 2 или 3.")

    # Валидация имени героя
    while True:
        user_hero_name = input("Введите имя вашего героя: ")
        if user_hero_name.strip():
            break
        else:
            print("❌ Имя героя не может быть пустым.")

    # Валидация уровня
    while True:
        level_input = input("Введите уровень героя (1-100): ")
        if level_input.isdigit() and 1 <= int(level_input) <= 100:
            level = int(level_input)
            break
        else:
            print("❌ Уровень должен быть числом от 1 до 100.")

    # Валидация силы
    while True:
        strength_input = input("Введите силу героя (1-100): ")
        if strength_input.isdigit() and 1 <= int(strength_input) <= 100:
            strength = int(strength_input)
            break
        else:
            print("❌ Сила должна быть числом от 1 до 100.")

    # Тут создание героя 
    if user_hero_choice == "1":
        hero = Warrior(user_hero_name, level, 100, strength, stamina=30)
    elif user_hero_choice == "2":
        hero = Mage(user_hero_name, level, 80, strength, mana=100)
    elif user_hero_choice == "3":
        hero = Assassin(user_hero_name, level, 90, strength, stealth=70)

    
    print("\n" + "="*40)
    hero.greet()
    print("-"*40)
    hero.attack()
    print("-"*40)
    hero.rest()
    print("="*40)

    # Тупо выход 
    again = input("\nХотите создать другого героя? (да/нет): ")
    if again.strip().lower() != "да":
        print("\nДо свидания!")
        break