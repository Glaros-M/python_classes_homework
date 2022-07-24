#! venv/bin/python3.10
from random import randint, choice
from npc import classes


names = [
    'Иван',
    'Дима',
    'Максим',
    'Коля',
    'Михаил',
    'Терентий',
    'Маша'
]


class Game(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, number_of_npc: int):
        self.number_of_NPC = number_of_npc
        self.players = []
        for i in range(number_of_npc):
            selected_class = choice(classes)
            self.players.append(selected_class(choice(names) +"_"+ str(i+1)))

    def delete_dead_bodies(self):
        """удаление трупов из игры"""
        temp = []
        for i in range(len(self.players)):
            if self.players[i].is_alive:
                temp.append(self.players[i])
        self.players = temp

    def check_for_winner(self) -> "NPC":
        """Если игрок остался один - вернуть его как победителя.
        Вопрос: необходимо ли делать проверку тут? что возвращать если функция вызвана до конца игры?
        Ввести рейтинг для битв с несколькими выжившими?
        """
        if len(self.players) == 1:
            return self.players[0]
        else:
            raise Exception(f"ПОБЕДИТЕЛЬ ЕЩЕ НЕ ОПРЕДЕЛЕН! Осталось {len(self.players)} игроков")

    def start(self) -> "NPC":
        are_alive = True
        for round in range(10):
            self.delete_dead_bodies()
            # Определение победителя
            if len(self.players) > 1:
                print(f"Стартует раунд {round}")
                for npc in self.players:
                    if npc.is_alive:
                        npc.attack(target=npc.get_target(self.players))
            else:
                return self.check_for_winner()


if __name__ == "__main__":
    print("Welcome to the Game!")
    game = Game(int(input("Введите количество игроков: ")))
    #game = Game(2)
    winner = game.start()
    if winner:
        print(f"{winner.name} победил!!!")
    else:
        print("В живых не остался никто!")

