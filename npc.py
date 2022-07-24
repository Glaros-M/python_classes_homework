from characteristics import Characteristics
from random import randint, choice


class NPC(object):

    def __init__(self, name: str):
        self.characteristics = Characteristics()
        self.name = name
        self.is_alive = True
        self._set_base_characteristic()
        print(f"Новый {self.class_name} по имени: {self.name}, {self}")
        self.characteristics.get_base_characteristics()
        self.characteristics.get_secondary_characteristics()
        print()

    def _set_base_characteristic(self):
        self.class_name = "noclass"
        self.characteristics.endurance = randint(1, 20)
        self.characteristics.strenght = randint(1, 15)
        self.characteristics.dexterity = randint(1, 15)
        self.characteristics.intelligence = randint(1, 15)

    def get_target(self, players: list):
        while True:
            target = choice(players)
            if not target == self and target.is_alive:
                print(f"{self.name} выбрал цель {target.name}")
                return target

    def attack(self, target: "NPC"):
        for i in range(self.characteristics.attack_speed):
            if target.is_alive:
                print(f"Аттака №{i+1}: {self.name}({self.characteristics.health}) нанес  {target.name}({target.characteristics.health})  {self.characteristics.damage} урона")
                target.attacked(self.characteristics.damage)

    def attacked(self, damage: int):
        if self.characteristics.health > damage:
            self.characteristics.health = self.characteristics.health - damage
        else:
            self.is_alive = False
            print(f"{self.name} умерает!")


class Warior(NPC):

    def __init__(self, name):
        super().__init__(name)

    def _set_base_characteristic(self):
        self.class_name = "Воин"
        self.characteristics.endurance = randint(10, 30)
        self.characteristics.strenght = randint(10, 25)
        self.characteristics.dexterity = randint(1, 15)
        self.characteristics.intelligence = 0


class Rogue(NPC):
    def __init__(self, name):
        super().__init__(name)

    def _set_base_characteristic(self):
        self.class_name = "Разбойник"
        self.characteristics.endurance = randint(1, 15)
        self.characteristics.strenght = randint(1, 15)
        self.characteristics.dexterity = randint(20, 40)
        self.characteristics.intelligence = randint(1, 10)


class Paladin(NPC):
    def __init__(self, name):
        super().__init__(name)

    def _set_base_characteristic(self):
        self.class_name = "Паладин"
        self.characteristics.endurance = randint(15, 35)
        self.characteristics.strenght = randint(10, 20)
        self.characteristics.dexterity = randint(1, 10)
        self.characteristics.intelligence = randint(1, 15)


classes = [Paladin, Warior, Rogue]

if __name__ == "__main__":
    a = NPC("test")
    b = Warior("War")
    c = Rogue("Roga")
    d = Paladin("ProtoPal")
