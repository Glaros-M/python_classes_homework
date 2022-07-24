from typing import Callable


class HitsStatistic:
    """"""
    def __init__(self, function: Callable):
        self.function = function
        self._hits = 0

    def __call__(self, *args, **kwargs):
        self.function(*args, **kwargs)
        self._hits += 1
        print(f"{self._hits = }")

    @property
    def hits(self):
        return self._hits


