from typing import Callable
from dataclasses import dataclass
from random import randint
from enum import Enum


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def magic_flow():
    "Рассовая способность кровавых эльфов"
    pass


def berserk():
    "Рассовая способность троллей"
    pass


@dataclass()
class Rase:
    name: str
    deskription: str
    rase_ability: Callable


class Races(Enum):
    BloodElv = Rase(name="Blood Elv", deskription="Horde race", rase_ability=magic_flow)
    Troll = Rase(name="Troll", deskription="Horde race", rase_ability=berserk)


class GameClasses:
    def __init__(self, endurance: float, strength: float, dexterity: float, intelligence: float):
        self.endurance = int(endurance)
        self.strength = int(strength)
        self.dexterity = int(dexterity)
        self.intelligence = int(intelligence)
        print("createdBASEClass")

    def simple_attack(self, target):
        pass

    def power_attack(self, target):
        pass

    def protect(self):
        pass


class Warior(GameClasses):
    def __init__(self, endurance: int, strength: int, dexterity: int, intelligence: int):
        endurance = endurance * 1.5
        strength = strength * 2
        dexterity = dexterity
        intelligence = intelligence / 3
        super(Warior, self).__init__(endurance, strength, dexterity, intelligence)
        self.rage = 0
        print("created Warior")

    def simple_attack(self, target):
        pass

    def power_attack(self, target):
        pass

    def protect(self):
        pass


class NPC(GameClasses):
    def __init__(self, class_name: GameClasses, race_name):
        endurance = randint(1, 100)
        strength = randint(1, 100)
        dexterity = randint(1, 100)
        intelligence = randint(1, 100)
        super(class_name, self).__init__(endurance, strength, dexterity, intelligence)

a = NPC(Warior,"123")

# короче добавлять рассу при помощи декоратора
#def race(race_name: str):
 #   def