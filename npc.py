from characteristics import Characteristics
from random import randint, choice

# Создать класс(?) генератор имен и фамилий

class NPC(object):
    def __init__(self, name: str):
        self.characteristics = Characteristics()
        self.name = name
        self.is_alive = True
        self.characteristics.endurance = randint(1, 20)
        self.characteristics.strenght = randint(1, 15)
        self.characteristics.dexterity = randint(1, 15)
        self.characteristics.intelligence = randint(1, 15)
        print(f"Новый боец по имени: {self.name}, {self}\n")
        self.characteristics.get_base_characteristics()
        self.characteristics.get_secondary_characteristics()

    def get_target(self, players: list):
        while True:
            target = choice(players)
            if not target == self and target.is_alive:
                print(f"{self.name} выбрал цель {target.name}")
                return target

    def attack(self, target: "NPC"):
        for i in range(self.characteristics.attack_speed):
            if target.is_alive:
                print(f"Аттака №{i+1}: {self.name} нанес  {target.name}  {self.characteristics.damage} урона")
                target.attacked(self.characteristics.damage)

    def attacked(self, damage: int):
        if self.characteristics.health > damage:
            self.characteristics.health = self.characteristics.health - damage
        else:
            self.is_alive = False
            print(f"{self.name} died!")


if __name__ == "__main__":
    a = NPC("test")
