class BaseCharacteristic:

    def __init__(self, characteristic: str):
        """"""
        self.name = characteristic

    def __set__(self, instance, value):
        """Тут описываются зависимости второстепенных характеристик от базовых"""
        instance.__dict__[self.name] = value
        match self.name:
            case "endurance":
                instance.__dict__["health"] = value // 5 * 100 + value % 5
            case "strenght":
                instance.__dict__["damage"] = value * 5
            case "dexterity":
                if value >= 5:
                    instance.__dict__["attack_speed"] = value // 5
                else:
                    instance.__dict__["attack_speed"] = 1
            case "intelligence":
                instance.__dict__["mana"] = value * 10
            case _:
                raise Exception("Указанный параметр отсутствует")

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class Characteristics:
    endurance = BaseCharacteristic("endurance")
    strenght = BaseCharacteristic("strenght")
    dexterity = BaseCharacteristic("dexterity")
    intelligence = BaseCharacteristic("intelligence")

    def __init__(self, endurance = 0, health = 0,  strenght = 0,  damage = 0,
                 dexterity = 0,  attack_speed = 0,  intelligence = 0,  mana = 0):
        self.endurance = endurance
        self.health = health
        self.strenght = strenght
        self.damage = damage
        self.dexterity = dexterity
        self.attack_speed = attack_speed
        self.intelligence = intelligence
        self.mana = mana

    def get_base_characteristics(self):
        print(f"Выносливость: {self.endurance}",
              f"Сила: {self.strenght}",
              f"Ловкость: {self.dexterity}",
              f"Интеллект: {self.intelligence}",
              )

    def get_secondary_characteristics(self):
        print(f"Здоровье: {self.health}",
              f"Урон: {self.damage}",
              f"Скорость атаки: {self.attack_speed}",
              f"Мана: {self.mana}",
              )


if __name__ == "__main__":
    char = Characteristics()

    print("+- обычный персонаж с основными характеристиками до 10. ПРИМЕР: всего по 7")
    char.endurance = 7
    print(f"{char.endurance} выносливости",
          f"{char.endurance = }",
          f"{char.health = }",
          sep="\n",
          end="\n"
          )

    char.strenght = 7
    print(f"{char.strenght} силы",
          f"{char.strenght = }",
          f"{char.damage = }",
          sep="\n",
          end="\n"
          )

    char.dexterity = 7
    print(f"{char.dexterity} ловкости",
          f"{char.dexterity = }",
          f"{char.attack_speed = }",
          sep="\n",
          end="\n"
          )

    char.intelligence = 7
    print(f"{char.intelligence} интеллекта",
          f"{char.intelligence = }",
          f"{char.mana = }",
          sep="\n",
          end="\n"
          )

    char.health = 15
    print(f"{char.health = }")

    char2 = Characteristics()

    char2.endurance = 12
    print(f"{char.endurance} выносливости",
          f"{char.endurance = }",
          f"{char.health = }",
          sep="\n",
          end="\n"
          )

    print(f"{char2.endurance} выносливости",
          f"{char2.endurance = }",
          f"{char2.health = }",
          sep="\n",
          end="\n"
          )