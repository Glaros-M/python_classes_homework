#! venv/bin/python3.10
from random import choice
from npc import classes
from names import Name


class Game(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, number_of_npc: int):
        self.number_of_NPC = number_of_npc
        self.players = []
        self.rounds = self.number_of_NPC * 5
        for _ in range(number_of_npc):
            selected_class = choice(classes)
            selected_name = Name()
            self.players.append(selected_class(selected_name.name))

    def delete_dead_bodies(self):
        """удаление трупов из игры"""
        temp = []
        for i in range(len(self.players)):
            if self.players[i].is_alive:
                temp.append(self.players[i])
        self.players = temp

    def check_for_winner(self) -> "NPC":
        if len(self.players) == 1:
            return self.players[0]
        else:
            raise Exception(f"ПОБЕДИТЕЛЬ ЕЩЕ НЕ ОПРЕДЕЛЕН! Осталось {len(self.players)} игроков")

    def start(self) -> "NPC":
        are_alive = True
        for round in range(1, self.rounds):
            self.delete_dead_bodies()
            # Определение победителя
            if len(self.players) > 1:
                print(f"\nСтартует раунд {round}")
                for npc in self.players:
                    if npc.is_alive:
                        npc.attack(target=npc.get_target(self.players))
            else:
                return self.check_for_winner()


if __name__ == "__main__":
    print("Welcome to the Game!")
    game = Game(int(input("Введите количество игроков: ")))
    winner = game.start()
    if winner:
        print(f"\n{winner.name} победил!!!")
    else:
        print("Победитель не определился.")

