from abc import ABC, abstractmethod

from algo_genetique.individue import Individue


class Crossover(ABC):

    @abstractmethod
    def doCrossover(self, ind1: Individue, ind2: Individue) -> tuple[Individue, Individue]: ...
