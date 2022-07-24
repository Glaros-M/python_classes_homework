from random import choice
names = [
    "Порфирий",
    "Властислав",
    "Посейдон",
    "Елисей",
    "Ладамир",
    "Аристарх",
    "Илларион",
    "Иннокентий",
    "Лука",
    "Филарет"
]
surnames = [
    "Васильев",
    "Петров",
    "Соколов",
    "Михайлов",
    "Новиков",
    "Федоров",
    "Морозов"
]


class Name:

    def __init__(self):
        self._name = choice(names) + " " + choice(surnames)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value


if __name__ == "__main__":
    a = Name()
    print(a.name)