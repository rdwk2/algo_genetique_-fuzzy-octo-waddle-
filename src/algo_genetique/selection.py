

from abc import ABC, abstractmethod

from algo_genetique.individue import Individue


class Selection(ABC):

    @abstractmethod
    def select(self, parent: tuple[Individue, Individue], child: tuple[Individue, Individue]) -> tuple[Individue, Individue]: ...
