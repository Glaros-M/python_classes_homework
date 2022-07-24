"""
        self.endurance = int(endurance)
        self.strength = int(strength)
        self.dexterity = int(dexterity)
        self.intelligence = int(intelligence)
"""


class Endurance:
    def __init__(self, value: int = 0.0):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value
        instance.health = value // 5 * 100 + value % 5



class Strenght:
    def __init__(self, value: int = 0.0):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value


class Dexterity:
    def __init__(self, value: int = 0.0):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value


class Intelligence:
    def __init__(self, value: int = 0.0):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value


class Health:
    """Сложная характеристика. При создании зависит от выносливости,
     но в дальнейшем уменьшается не уменьшая выносливость. Аналогично будет с маной"""
    # Пока что оставил прямую инициализацию от выносливости при создании
    _instance = None

    def __init__(self, endurance: int = 0):
        self.value = endurance // 5 * 100 + endurance % 5

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value

class Damage:
    def __set__(self, instance, value):
        instance.strenght = value // 5

    def __get__(self, instance, owner):
        return instance.strenght*5


class AttackSpeed:
    def __set__(self, instance, value):
        instance.dexterity = value * 5

    def __get__(self, instance, owner):
        return instance.dexterity // 5


class Mana:
    def __set__(self, instance, value):
        instance.intelligance = value // 10

    def __get__(self, instance, owner):
        return instance.intelligence * 10


class Characteristics:
    endurance = Endurance()
    health = Health(endurance.value)
    strenght = Strenght()
    damage = Damage()
    dexterity = Dexterity()
    attack_speed = AttackSpeed()
    intelligence = Intelligence()
    mana = Mana()


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